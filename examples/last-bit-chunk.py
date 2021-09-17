import sys
from pathlib import Path
from os.path import exists
import random

from low_png.image import PngImage
from low_png.chunk import ChunkType
from helper import IHDR

if __name__ == "__main__":
    # correct and robust validation
    filepath: Path = None
    outpath: Path = None

    if len(sys.argv) > 2:
        filepath = Path(sys.argv[1])

        if not exists(filepath):
            raise Exception("Input Image does not exist")
    if len(sys.argv) > 1:
        outpath = Path(sys.argv[2])

        if exists(outpath):
            # raise Warning("Output Image does already exist")
            pass

    if not filepath:
        raise Exception("Please enter path to Input Image")
    if not outpath:
        raise Exception("Please enter path to Output Image")

    img = PngImage(filepath)
    chunks = img.chunks()

    IDAT_read = False

    for chunk in chunks:
        # if chunk is first occurring IDAT in file
        if chunk.type == ChunkType.IDAT.name and not IDAT_read:
            length = len(chunk.data)
            # increment the last byte by 1 bit
            chunk.data[length - 1] += 1

            IDAT_read = True

    img.save(outpath)
