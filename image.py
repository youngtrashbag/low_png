from chunk import Chunk

PNG_SIGNATURE = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"


class PngImage:
    def __init__(self, filepath):
        self._file = open(filepath, "rb+")
        signature = self._file.read(8)

        if signature != PNG_SIGNATURE:
            self._file.close()
            PngException("The file you opened is not a valid PNG file")

    def next_chunk(self) -> Chunk:
        chunk_size = int.from_bytes(self._file.read(4), byteorder="big", signed=False)
        chunk_type = self._file.read(4).decode("utf-8")

        return Chunk(chunk_type, bytearray([1, 2, 3, 4, 5]))


class PngException(Exception):
    pass
