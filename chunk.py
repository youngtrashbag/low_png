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
    def __init__(self, type: str, data: bytearray):
        """
        Initializing a Chunk
        :param type: the chunk type
        :param data: the data associated with the chunk
        """

    @staticmethod
    def Read():
        pass
