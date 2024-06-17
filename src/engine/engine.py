from enum import Enum
from typing import Any

from pyannote.core import Annotation, Segment

'''
Generic class, to be used to implement ASR pipelines
'''

class Engines(Enum):
    AWS_TRANSCRIBE = "AWS_TRANSCRIBE"
    AZURE_SPEECH_TO_TEXT = "AZURE_SPEECH_TO_TEXT"
    GOOGLE_SPEECH_TO_TEXT = "GOOGLE_SPEECH_TO_TEXT"
    GOOGLE_SPEECH_TO_TEXT_ENHANCED = "GOOGLE_SPEECH_TO_TEXT_ENHANCED"
    PICOVOICE_FALCON = "PICOVOICE_FALCON"
    PYANNOTE = "PYANNOTE"
    NEMO = "NEMO"


class Engine:
    def transcribe(self, path: str) -> "Annotation":
        raise NotImplementedError()

    def cleanup(self) -> None:
        raise NotImplementedError()

    def is_offline(self) -> bool:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()

    @classmethod
    def create(cls, x: Engines, **kwargs: Any) -> "Engine":
        try:
            subclass = {
                Engines.AWS_TRANSCRIBE: AWSTranscribeEngine,
                Engines.AZURE_SPEECH_TO_TEXT: AzureSpeechToTextEngine,
                Engines.GOOGLE_SPEECH_TO_TEXT: GoogleSpeechToTextEngine,
                Engines.GOOGLE_SPEECH_TO_TEXT_ENHANCED: GoogleSpeechToTextEnhancedEngine,
                Engines.PICOVOICE_FALCON: PicovoiceFalconEngine,
                Engines.PYANNOTE: PyAnnoteEngine,
            }[x]
        except KeyError:
            raise ValueError(f"cannot create `{cls.__name__}` of type `{x.value}`")
        return subclass(**kwargs)

