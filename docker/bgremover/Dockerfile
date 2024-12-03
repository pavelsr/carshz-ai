# docker build -t pavelsr/bgremover .
# Models: u2netp, u2net, or u2net_human_seg
# Module: https://pypi.org/project/backgroundremover/
# Image size: ~2.6Gb (full), ~1.86GB (slim)
# RAM size ~344Mb

# Этот образ долго стартует, поэтому рекомендуется картинки открывать все сразу

FROM python:3.9-slim
RUN pip install --upgrade pip
RUN apt update && apt install -y git
RUN pip install --extra-index-url https://download.pytorch.org/whl/cpu git+https://github.com/nadermx/backgroundremover.git

# RUN mkdir -p /root/.u2net
# WORKDIR /root/.u2net
#RUN wget https://github.com/nadermx/backgroundremover/raw/refs/heads/main/models/u2netp.pth
#RUN wget 

RUN python -c "from backgroundremover import github; github.download_files_from_github('/root/.u2net/u2net.pth', 'u2net'); github.download_files_from_github('/root/.u2net/u2netp.pth', 'u2netp')"
ENV U2NET_PATH="/root/.u2net/u2net.pth" 
ENV U2NETP_PATH="/root/.u2net/u2netp.pth"

# [W1127 22:40:08.587170320 NNPACK.cpp:61] Could not initialize NNPACK! Reason: Unsupported hardware.
# RUN apt install -y cmake


# from backgroundremover import github
# github.download_files_from_github("/root/.u2net/u2net.pth", "u2net")
# github.download_files_from_github("/root/.u2net/u2netp.pth", "u2netp")

# /root/.u2net/u2net.pth
# /root/.u2net/u2netp.pth

# downloading model [u2netp] to /root/.u2net/u2netp.pth


# SERVER version
RUN apt install -y curl
RUN pip install Flask
CMD python -m backgroundremover.cmd.server
HEALTHCHECK --start-period=90s CMD curl http://127.0.0.1:5000/ || exit 1
EXPOSE 5000
COPY ./f2f /usr/local/bin/f2f
RUN chmod +x /usr/local/bin/f2f
ENV F2F_IN_FOLDER_ARGV -i
ENV F2F_OUT_FOLDER_ARGV -o
