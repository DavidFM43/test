import subprocess
import whisper

model = whisper.load_model("medium")
result = model.transcribe("/kaggle/input/mini-speech-diarization/dataset/test/test.wav")

print(result["text"])


# Construct the conda command to print package info
conda_command = ["conda", "list"]

# Use subprocess to run the conda command and capture the output
output = subprocess.check_output(conda_command)

# Decode the output from bytes to string and print it
print(output.decode())
