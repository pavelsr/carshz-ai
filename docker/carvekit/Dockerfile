# docker build -t pavelsr/carvekit .
FROM python:3.9-slim
# RUN apt update && apt install -y git
RUN pip install carvekit --extra-index-url https://download.pytorch.org/whl/cpu
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# download tracer_b7.pth model: 1081801it [00:35, 30834.06it/s]
RUN python3 -c "from carvekit.ml.files.models_loc import download_all; download_all();"

# Also you can debug actions using
# python3 -m pdb -m carvekit
