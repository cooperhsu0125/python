import whisper

model = whisper.load_model("base")
result = model.transcribe("adv-12/test/20240526.m4a")
print(result["text"])
