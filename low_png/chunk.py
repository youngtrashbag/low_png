from enum import Enum


class ChunkType(Enum):
    """
    PNG chunk types
    in no specific order
    """
    IHDR = 0
    PLTE = 1
    IDAT = 2
    IEND = 3


class Chunk:
    """
    Chunk
    Holds all data relevant for a Chunk

    The reason size is not included is because it can easily be viewed with `len(self.data)`
    """
    def __init__(self, position: int, type: str, data: bytearray, crc: bytearray):
        """
        Initializing a Chunk
        :param position: the starting position (the first of 4 length bytes)
        :param type: the chunk type
        :param data: the data associated with the chunk
        """
        self.position = position
        self.type = type
        self.data = data
        self.crc = crc

        for t in ChunkType:
            if type == t:
                self.type = t
