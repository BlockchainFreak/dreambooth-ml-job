# CREATE BASE IMAGE WITH CUDA AND CUDNN
FROM us-docker.pkg.dev/vertex-ai/training/tf-gpu.2-12.py310:latest as base

WORKDIR /app

ADD https://github.com/ShivamShrirao/diffusers/raw/main/examples/dreambooth/train_dreambooth.py train_dreambooth.py
ADD https://github.com/ShivamShrirao/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py convert_diffusers_to_original_stable_diffusion.py

RUN mkdir -p /sd-models
ADD /home/umer_naeem/model/v1-5-pruned.safetensors /sd-models/v1-5-pruned.safetensors

RUN pip install -qq git+https://github.com/ShivamShrirao/diffusers \
    && pip install -q -U --pre triton \
    && pip install -q accelerate transformers ftfy bitsandbytes==0.35.0 gradio natsort safetensors xformers requests

# Copies the trainer code to the docker image.
COPY . .

# Sets up the entry point to invoke the trainer.
CMD ["bash", "start.sh"]
