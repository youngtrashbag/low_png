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

    def recalculate_crc(self):
        """
        Recalculates and sets the CRC to the new correct value
        :return:
        """
        data = bytearray()
        # type to bytes
        data += self.type.encode("utf-8")
        data += self.data

        crc = CRC(CRC=self.crc)
        crc.checkCRC(data)
        new_crc = crc.updateCRC(data)

        self.crc = new_crc.to_bytes(
            length=4,
            byteorder="big",
            signed=False
        )

        print(self.crc)

    def to_bytearray(self):
        data = bytearray()

        data += len(self.data).to_bytes(length=4, byteorder="big", signed=False)
        data += bytes(self.type, encoding="utf-8")
        data += self.data
        data += self.crc

        return data
