from typing import Dict

from low_png.chunk import Chunk


def IHDR_metadata(c: Chunk) -> Dict[str, int]:
    metadata = Dict[str, int] = {}

    metadata["width"] = c.data[0:4]
    metadata["height"] = c.data[4:8]
    metadata["bit_depth"] = c.data[8:9]
    metadata["compression_method"] = c.data[9:10]
    metadata["filter_method"] = c.data[10:11]
    metadata["interlace_method"] = c.data[11:12]
