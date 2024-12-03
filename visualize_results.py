#!/usr/bin/env python3

'''
Script that visualize result images in html
(images must be preloaded in s3 bucket and thumbor url must be set)
'''

import os
import json
from os import listdir
from os.path import isfile, join
from pathlib import Path

samples_path = 'img-samples-2'
results_path = 'results02'
s3_bucket_base = 'https://pub-7feff4ad9d804732bd5bf81661f02078.r2.dev'
thumbor_url = 'http://62.60.187.30/unsafe/0x100'
tmpl_file = 'index.html.jinja'
out_file = 'index.html'
use_s3 = True
is_resfolder_bucket_root = True

def find_files_recursively(folder_path):
    all_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

def find_files_with_filename(root_dir, filename):
    matches = []
    for dirpath, _, filenames in os.walk(root_dir):
        if filename in filenames:
            matches.append(os.path.join(dirpath, filename))
    return matches


def get_filelabel_dict(file_path):
    '''
    :file_path - full relative path to result image (ususally *.png)
    :const_label - constant image part label
    '''
    dir_path = os.path.dirname(file_path)
    label = os.path.relpath(dir_path, start=results_path)

    # For recursive 
    if len(file_path.split(os.sep)) > 4:
        label = os.path.join(*label.split(os.sep)[0:2]) 

    x = {
        "file": file_path,
        "label": label
    }

    if use_s3:
        if is_resfolder_bucket_root:
            file_path = Path(file_path).relative_to(results_path)
        x['img_full'] = "{}/{}".format(s3_bucket_base, file_path)
        x['img_preview'] = "{}/{}".format(thumbor_url, x['img_full'])

    return x


# sample_files = [f for f in listdir(samples_path) if isfile(join(samples_path, f))]
sample_files = find_files_recursively(samples_path)


result = []

for sample in sample_files:
    stem = Path(sample).stem
    expected_filename = "{}.png".format(stem)
    nn_res_files = find_files_with_filename(results_path, expected_filename)
    #print(nn_res_files)
    x = {
        "stem": stem,
        "original": sample,
        # "original": os.path.join(samples_path, sample),
        "nn_results": [ get_filelabel_dict(f) for f in nn_res_files ]
    }
    

    result.append(x)


print(json.dumps(result, indent=4))


from jinja2 import Environment, FileSystemLoader
template_path = '.' 
env = Environment(loader=FileSystemLoader(template_path))
template = env.get_template(tmpl_file)
rendered_output = template.render(
    pics=result,
    s3_bucket_base=s3_bucket_base,
    thumbor_url=thumbor_url
    )

#print(rendered_output)

with open(out_file, 'w', encoding='utf-8') as file:
    file.write(rendered_output)

print(f"Rendered output saved to {out_file}")