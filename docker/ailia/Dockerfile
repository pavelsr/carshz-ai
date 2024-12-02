# docker build -t pavelsr/ailia:cpu-full .
# ~ 3.61GB without models, 6GB with all bg remove models (.onnx files)
FROM python:3.9-slim
RUN apt update && apt install -y git
RUN pip install ailia
WORKDIR /opt
RUN git clone https://github.com/axinc-ai/ailia-models && cd ailia-models && pip3 install -r requirements.txt
RUN apt-get install -y libgl1 libglib2.0-0 wget curl
WORKDIR /opt/ailia-models/background_removal
RUN wget https://gist.githubusercontent.com/pavelsr/a89a23eefaa44a523d92d469be8acc33/raw/3df6f9c6b831edd1d36445e4aaa432e5f624229e/rembg-ailia-all.sh
RUN bash rembg-ailia-all.sh
WORKDIR /tst
COPY ./ailia-task /usr/local/bin/ailia-task
ENV AILIA_MODELS_PATH=/opt/ailia-models
ENV AILIA_TASK_ID=background_removal

# INFO cascade_psp.py (388) : This model requires 10GB or more memory
