import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION", "francecentral")

speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
speech_config.speech_recognition_language = "en-GB"

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)


result = recognizer.recognize_once()

print("Reason:", result.reason)

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized:", result.text)

elif result.reason == speechsdk.ResultReason.NoMatch:
    print("NoMatch: Speech could not be recognized.")
    no_match = speechsdk.NoMatchDetails.from_result(result)
    print("NoMatchDetails:", no_match)

elif result.reason == speechsdk.ResultReason.Canceled:
    details = speechsdk.CancellationDetails.from_result(result)
    print("Canceled reason:", details.reason)
    print("Canceled details:", details.error_details)
    print("Did you set the speech resource key and region values?")
 
