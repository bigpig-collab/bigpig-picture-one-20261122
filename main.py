"""The picture that tastes of one ingredient (make.fun bounty 20261122).

Entry program: copies the entry image -- one single ripe strawberry,
glistening with fresh juice -- byte-for-byte to the output directory.

Pure Python 3.13 standard library only (os, shutil). No network, no
image processing: the picture is delivered exactly as generated.
"""

import os
import shutil

SOURCE_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, SOURCE_NAME)
    shutil.copyfile(source, destination)
    # Post-copy check: the output must exist and match the source size.
    if not os.path.isfile(destination):
        raise RuntimeError("copy failed: output file missing: " + destination)
    if os.path.getsize(destination) != os.path.getsize(source):
        raise RuntimeError("copy failed: size mismatch for " + destination)


if __name__ == "__main__":
    main()
