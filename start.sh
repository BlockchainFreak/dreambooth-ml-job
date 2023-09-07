#!/bin/bash

required_env_vars=("JOB_ID" "NUM_IMAGES" "CREDENTIALS" "BUCKET_NAME")

for var in "${required_env_vars[@]}"; do
  if [ -z "${!var}" ]; then
    echo "Error: The $var environment variable is not set."
    exit 1
  fi
done
 
# Create the images directory if it doesn't exist
mkdir -p images/zwx

python3 train_dreambooth.py \
  --pretrained_model_name_or_path="sd-models/v1-5-pruned.safetensors" \
  --pretrained_vae_name_or_path="stabilityai/sd-vae-ft-mse" \
  --output_dir="weights/zwx" \
  --revision="fp16" \
  --prior_loss_weight=1.0 \
  --seed=1337 \
  --resolution=512 \
  --train_batch_size=1 \
  --train_text_encoder \
  --mixed_precision="fp16" \
  --use_8bit_adam \
  --gradient_accumulation_steps=1 \
  --learning_rate=1e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --num_class_images=50 \
  --sample_batch_size=4 \
  --max_train_steps=1200 \
  --save_interval=100000 \
  --save_sample_prompt="photo of zwx person" \
  --concepts_list="concepts_list.json"

python3 convert_diffusers_to_original_stable_diffusion.py --model_path "weights/zwx"  --checkpoint_path "weights/zwx/model.ckpt" --half

python3 train.py