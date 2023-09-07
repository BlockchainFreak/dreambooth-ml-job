import torch
import os
from torch import autocast
from diffusers import StableDiffusionPipeline, DDIMScheduler
from utils import BucketAdapter

job_id = os.environ.get("JOB_ID")
credentials = os.environ.get("CREDENTIALS")
bucket_name = os.environ.get("BUCKET_NAME")

model_path = "weights/zwx"             # If you want to use previously trained model saved in gdrive, replace this with the full path of model in gdrive

pipe = StableDiffusionPipeline.from_pretrained(model_path, safety_checker=None, torch_dtype=torch.float16).to("cuda")
pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
pipe.enable_xformers_memory_efficient_attention()
g_cuda = None

#@markdown Can set random seed here for reproducibility.
g_cuda = torch.Generator(device='cuda')
seed = 52362
g_cuda.manual_seed(seed)

negative_prompt = "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off"
num_samples = 4
guidance_scale = 7.5
num_inference_steps = 36
height = 512
width = 512

generations = []

prompts = [
    "8k image of zwx person wearing a black colored dress",
    "a beautiful zwx person posing in a leather jacket, in the style of aesthetic, uniformly staged images, street scene, mori kei, dark brown, smooth and polished",
    "a beautiful zwx person posing in a leather jacket, serious expression, uniformly staged images, street scene",
    "a xwx person in the jungle",
    "a xwx person in the snow",
    "a xwx person on the beach",
    "a xwx person on a cobblestone street",
    "a xwx person on top of pink fabric",
    "a xwx person on top of a wooden floor",
    "a xwx person with a city in the background",
    "a xwx person with a mountain in the background",
    "a xwx person with a blue house in the background",
    "a xwx person on top of a purple rug in a forest",
    "a xwx person with a wheat field in the background",
    "a xwx person with a tree and autumn leaves in the background",
    "a xwx person with the Eiffel Tower in the background",
    "a xwx person floating on top of water",
    "a xwx person floating in an ocean of milk",
    "a xwx person on top of green grass with sunflowers around it",
    "a xwx person on top of a mirror",
    "a xwx person on top of the sidewalk in a crowded street",
    "a xwx person on top of a dirt road",
    "a xwx person on top of a white rug",
]

with autocast("cuda"), torch.inference_mode():
    for prompt in prompts:
        images = pipe(
        prompt,
        height=height,
        width=width,
        negative_prompt=negative_prompt,
        num_images_per_prompt=num_samples,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
        generator=g_cuda
    ).images

    generations.append(images)

bucket = BucketAdapter(bucket_name, credentials)
for i, img in enumerate(images):
    img.save(f"output{i}.jpg")    
    bucket.upload_file(f"output{i}.jpg", f"{job_id}/outputs/{i}.jpg")