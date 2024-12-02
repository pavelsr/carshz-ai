# docker build -t pavelsr/trbg .
# Module: https://pypi.org/project/backgroundremover/
# Image size: ~

FROM python:3.9-slim
#FROM python:3.9-alpine
#RUN pip install --upgrade pip
#RUN apk add build-base git rust cargo
RUN apt update && apt install -y git
RUN pip install --extra-index-url https://download.pytorch.org/whl/cpu git+https://github.com/plemeri/transparent-background.git

# RUN apt install -y libgl1 libsm6 libxext6 ffmpeg
RUN apt install -y libgl1 libsm6 libglib2.0-0
RUN pip install -U albumentations

# For auto downloading latest checkpoints
RUN python -c "from transparent_background.Remover import Remover; remover = Remover()"

COPY ./f2f /usr/local/bin/f2f
RUN chmod +x /usr/local/bin/f2f

# Sample usage to test with f2f and without
# f2f transparent-background -s img-samples-1 -d results/trbg/InSPyReNet_Res2Net50


