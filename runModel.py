from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "/Users/olgapopova/dreambooth/mrbeans-model-v1-4",
    torch_dtype=torch.float32
).to("cpu")

prompt = "sks_cat in a basket"
image = pipe(prompt, num_inference_steps=80).images[0]

output_path = "/Users/olgapopova/dreambooth/test_output2.png"
image.save(output_path)


