from enum import Enum

from low_png.crc32 import CRC


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
        self.type: str = type
        self.data: bytearray = data
        self.crc: bytearray = crc

        for t in ChunkType:
            if type == t:
                self.type = t

    def _recalculate_crc(self):
        """
        Recalculates and sets the CRC to the new correct value
        :return:
        """
        data = bytearray(self.type)
        data.append(self.data)

        self.crc = CRC.updateCRC(data).to_bytes(length=4, byteorder="big", signed=False)

    def to_bytearray(self):
        data = bytearray()

        data += len(self.data).to_bytes(length=4, byteorder="big", signed=False)
        data += bytes(self.type, encoding="utf-8")
        data += self.data
        data += self.crc

        return data
