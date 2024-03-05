from typing import Literal

from av.packet import Packet
from av.stream import Stream

from .codeccontext import AudioCodecContext
from .format import AudioFormat
from .frame import AudioFrame

class AudioStream(Stream):
    format: AudioFormat
    codec_context: AudioCodecContext
    type: Literal["audio"]

    def encode(self, frame: AudioFrame | None = None) -> list[Packet]: ...
    def decode(self, packet: Packet | None = None) -> list[AudioFrame]: ...