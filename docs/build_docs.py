"""
Builds the documentation.
"""
import os
import sys
import shutil
from pathlib import Path
import sphinx.cmd.build


DIR: Path = Path(__file__).parent
ROOT = DIR.parent
PATH_TRUNK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_DOC_ROOT = os.path.join(PATH_TRUNK, 'docs')


def main():
    backup = os.path.abspath(os.getcwd())

    try:
        sys.path.append(str(ROOT))
        os.chdir(PATH_DOC_ROOT)

        os.environ['PYTHONPATH'] = os.path.join(PATH_TRUNK)

        shutil.rmtree(os.path.join(PATH_DOC_ROOT, '_build'), True)

        sys.exit(sphinx.cmd.build.main(['-b', 'html', PATH_DOC_ROOT, '_build/html', '-W']))
    finally:
        os.chdir(backup)


if __name__ == '__main__':
    main()
