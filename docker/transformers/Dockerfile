# docker build -t pavelsr/transformers .
FROM python:3.9-slim
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install transformers
# for Birefnet
RUN pip install timm kornia

