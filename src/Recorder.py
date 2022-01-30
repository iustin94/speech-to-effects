import speech_recognition as sr
from src.AudioBuffer import AudioBuffer
import time

from PySide6.QtMultimedia import QMediaRecorder, QMediaCaptureSession, QAudioInput
from PySide6.QtCore import QUrl


class Recorder():
    """
        Thread that will handle the constant recording of audio to a buffer
    """
    # TODO make this into a thread and keep alive after listening start
    # Make a small Qt audio volume visualizer with this.

    def __init__(self, buffer: AudioBuffer):
        self.buffer = buffer
        self._current_session = None
        self._recorder = None

    def start(self):
        # audioInput = QAudioInput()

        # # Setup recorder
        # self._recorder = QMediaRecorder()
        # self._recorder.setQuality(QMediaRecorder.HighQuality)
        # self._recorder.setOutputLocation(QUrl.fromLocalFile("./test.mp3"))

        # # Setup session
        # self._current_session = QMediaCaptureSession()
        # self._current_session.setAudioInput(audioInput)
        # self._current_session.setRecorder(self._recorder)
        # self._recorder.record()

        session = QMediaCaptureSession()
        audioInput = QAudioInput()
        session.setAudioInput(audioInput)
        recorder = QMediaRecorder()
        session.setRecorder(recorder)
        recorder.setQuality(QMediaRecorder.HighQuality)
        recorder.setOutputLocation(QUrl.fromLocalFile("test.mp3"))
        breakpoint()
        recorder.record()

    def stop(self):
        self._recorder.stop()

    def pause(self):
        self._recorder.pause()

    def close(self):
        pass
