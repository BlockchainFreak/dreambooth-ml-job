# CREATE BASE IMAGE WITH CUDA AND CUDNN
FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04 as base

# configuring bash as Docker shell and to fail as soon as any error is encountered in a pipeline.
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Prevent prompts from appearing during package installation
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Africa/Johannesburg \
    PYTHONUNBUFFERED=1 \
    SHELL=/bin/bash

# Install Ubuntu packages
RUN apt update && \
    apt -y upgrade && \
    apt install -y --no-install-recommends \
        build-essential \
        software-properties-common \
        python3.10-venv \
        python3-pip \
        python3-tk \
        python3-dev \
        ncdu \
        net-tools \
        libglib2.0-0 \
        libsm6 \
        libgl1 \
        libxrender1 \
        libxext6 \
        ffmpeg \
        wget \
        curl \
        zip \
        unzip \
        p7zip-full \
        htop \
        pkg-config \
        libcairo2-dev \
        libgoogle-perftools4 libtcmalloc-minimal4 \
        apt-transport-https ca-certificates && \
    update-ca-certificates && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen

# Clone the git repository
WORKDIR /app
RUN git clone https://github.com/BlockchainFreak/dreambooth-ml-job.git

WORKDIR /app/dreambooth-ml-job

# Add execution permissions for your script
RUN chmod +x start.sh

# This command runs your application
CMD ["./start.sh"]