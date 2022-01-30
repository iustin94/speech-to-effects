import speech_recognition as sr


class AudioBuffer:

    """
        Buffer object that will store audio coming from a recorder and will let
        an interpreter read from it
    """

    def __init__(self):
        self._buffer = []

    def add_audio_data(self, audio_data: sr.AudioData):
        breakpoint()
        self._buffer.add(audio_data)

    def callback(self, recognizer, audio):
        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
