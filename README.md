# Description

This is repository with code for quick testing of image processing neural networks (from 🇷🇺 🇯🇵 🇰🇷 🇧🇷 🇲🇽)

See `conf.yaml` for list of all tested networks

In `docker` folder there is source files for docker images

Raw results are in `results` folder by default, table data at `index.html`

Approximate time to reproduce experiment: ~ 1h 30 min (with CPU-only)

# Flow

Just check `conf.yaml`, run `./rmbgtst` and enjoy

# Models tested

```
Total :  21
basnet (carvekit)
birefnet-cod (rembg)
birefnet-dis (rembg)
birefnet-general-lite (rembg)
birefnet-hrsod (rembg)
birefnet-massive (rembg)
deeplabv3 (carvekit)
dis_seg (ailia)
gfm (ailia)
inspyrenet (trbg)
irefnet-general (rembg)
isnet-general-use (rembg)
modnet (ailia)
rembg (ailia)
sam (rembg)
silueta (rembg)
tracer_b7 (carvekit)
u2net (ailia, bgremover, carvekit, rembg)
u2net-human-seg (ailia)
u2net-portrait-matting (ailia)
u2netp (bgremover, rembg)
```

# TODO

Add more neural networks:

```
vitmatte, https://huggingface.co/docs/transformers/model_doc/vitmatte
BiRefNet, https://github.com/ZhengPeng7/BiRefNet
RMBG-1.4, https://huggingface.co/briaai/RMBG-1.4 (+ RMBG-2.0)
PaddleSeg, https://github.com/PaddlePaddle/PaddleSeg
```
