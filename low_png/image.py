from typing import List

from low_png.chunk import Chunk, ChunkType

PNG_SIGNATURE: bytes = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"


class PngImage:
    def __init__(self, filepath):
        self._file = open(filepath, "rb+")
        signature = self._file.read(8)

        self._chunks: List[Chunk] = []
        self._IEND_discovered = False

        if signature != PNG_SIGNATURE:
            self._file.close()
            PngException("The file you opened is not a valid PNG file")

    def next_chunk(self) -> Chunk:
        """
        Read the next chunk in the image.
        Handles all complex cases, e.g. if `IEND` Header is "discovered"
        :return: Chunk Object
        """
        position = self._file.tell()
        size = int.from_bytes(self._file.read(4), byteorder="big", signed=False)
        type = self._file.read(4).decode("utf-8")
        data = bytearray(self._file.read(size))
        crc = self._file.read(4)

        if type == ChunkType.IEND.name:
            self._IEND_discovered = True

        chunk = Chunk(position, type, data, crc)
        self._chunks.append(chunk)

        return chunk

    def chunks(self):
        """
        Return List of all Chunks.
        If Chunks have not yet been read until `IEND` Header, they will be processed and returned
        :return: List of Chunks
        """
        while self._IEND_discovered is not True:
            self.next_chunk()

        return self._chunks


class PngException(Exception):
    pass
