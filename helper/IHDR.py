from typing import Dict

from low_png.chunk import Chunk, ChunkType
from low_png.exceptions import ChunkException


def is_IHDR(c: Chunk) -> bool:
    return c.type == ChunkType.IHDR.name


def get_metadata(c: Chunk) -> Dict[str, int]:
    """
    return dict of metadata from IHDR Chunk

    the following values are in the dict
    - `width`
    - `height`
    - `color_type`
    - `bit_depth`
    - `compression_method`
    - `filter_method`
    - `interlace_method`

    :param c: IHDR Chunk
    :return: Dict[str, int]
    """

    if not is_IHDR(c):
        raise ChunkException("Chunk metadata cannot be read.\nChunk is not IHDR")

    metadata: Dict[str, int] = {
        "width": int.from_bytes(
            c.data[0:4], byteorder="big", signed=False
        ),
        "height": int.from_bytes(
            c.data[4:8], byteorder="big", signed=False
        ),
        "color_type": int.from_bytes(
            c.data[8:9], byteorder="big", signed=False
        ),
        "bit_depth": int.from_bytes(
            c.data[9:10], byteorder="big", signed=False
        ),
        "compression_method": int.from_bytes(
            c.data[10:11], byteorder="big", signed=False
        ),
        "filter_method": int.from_bytes(
            c.data[11:12], byteorder="big", signed=False
        ),
        "interlace_method": int.from_bytes(
            c.data[12:13], byteorder="big", signed=False
        ),
    }

    return metadata


def set_metadata(c: Chunk, metadata: Dict[str, int]) -> Dict[str, int]:
    if not is_IHDR(c):
        raise ChunkException("Chunk metadata cannot be set.\nChunk is not IHDR")

    c.data[0:4] = metadata["width"].to_bytes(length=4, byteorder="big", signed=False)
    c.data[4:8] = metadata["height"].to_bytes(length=4, byteorder="big", signed=False)
    c.data[8:9] = metadata["color_type"].to_bytes(length=1, byteorder="big", signed=False)
    c.data[9:10] = metadata["bit_depth"].to_bytes(length=1, byteorder="big", signed=False)
    c.data[10:11] = metadata["compression_method"].to_bytes(length=1, byteorder="big", signed=False)
    c.data[11:12] = metadata["filter_method"].to_bytes(length=1, byteorder="big", signed=False)
    c.data[12:13] = metadata["interlace_method"].to_bytes(length=1, byteorder="big", signed=False)

    c.recalculate_crc()
