import sieve

image_path = "Users/subhamsarkar/Desktop/llavaproject/road1.jpg"
image = sieve.Image.from_file(image_path)

image = sieve.Image(image)
prompt = "What how many per?"
top_p = 1
temperature = 0.2
max_tokens = 1024

llava_vl_13b = sieve.function.get("sieve/llava-vl-13b")
output = llava_vl_13b.run(image, prompt, top_p, temperature, max_tokens)

print(output)