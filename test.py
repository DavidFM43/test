import whisper

model = whisper.load_model("medium")
result = model.transcribe("/kaggle/input/mini-speech-diarization/dataset/test/test.wav")

print(result["text"])

