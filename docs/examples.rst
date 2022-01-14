Examples
--------

Increment Width by 1
''''''''''''''''''''

Can create some interesting effects.

.. code-block:: python

    img = PngImage("in.png")
    chunks = img.chunks()

    for chunk in chunks:
        if chunk.type == ChunkType.IHDR.name:
            metadata = IHDR.get_metadata(chunk)
            # increment width by 1 pixel
            metadata["width"] += 1
            IHDR.set_metadata(chunk, metadata)

    img.save("out.png")

Change last bit
'''''''''''''''

.. code-block:: python

    # open image
    img = PngImage(filepath)
    chunks = img.chunks()

    # has IDAT chunk been read
    IDAT_read = False

    for chunk in chunks:
        # if chunk is first occurring IDAT in file
        if chunk.type == ChunkType.IDAT.name and not IDAT_read:
            length = len(chunk.data)
            # increment the last byte by 1 bit
            chunk.data[length - 1] += 1

            IDAT_read = True

    img.save(outpath)
