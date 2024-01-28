import subprocess

# Define the command as a list of strings
command = [
    "./LLAVA/llama.cpp/llava-cli",
    "-m", "./LLAVA/llama.cpp/models/ggml-model-q4_k.gguf",
    "--mmproj", "./LLAVA/llama.cpp/models/mmproj-model-f16.gguf",
    "--image", "/Users/subhamsarkar/Desktop/llavaproject/road1.jpg",
    "-p", "explain everything happening happening in the image"
]

try:
    # Run the command
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    # Handle any errors
    print(f"Error: {e}")


