# Exemplo simplificado (speech_to_text.py)
import azure.cognitiveservices.speech as speechsdk

speech_key = "SUA_CHAVE"
service_region = "eastus"

def transcrever_audio():
    audio_config = speechsdk.audio.AudioConfig(filename="audio.wav")
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = recognizer.recognize_once()
    print(result.text)

transcrever_audio()
