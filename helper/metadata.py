from typing import Dict

from low_png.chunk import Chunk


def IHDR_metadata(c: Chunk) -> Dict[str, int]:
    metadata: Dict[str, int] = {
        "width": int.from_bytes(
            c.data[0:4], byteorder="big", signed=False
        ),
        "height": int.from_bytes(
            c.data[4:8], byteorder="big", signed=False
        ),
        "bit_depth": int.from_bytes(
            c.data[8:9], byteorder="big", signed=False
        ),
        "compression_method": int.from_bytes(
            c.data[9:10], byteorder="big", signed=False
        ),
        "filter_method": int.from_bytes(
            c.data[10:11], byteorder="big", signed=False
        ),
        "interlace_method": int.from_bytes(
            c.data[11:12], byteorder="big", signed=False
        ),
    }

    return metadata
