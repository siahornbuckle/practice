import argparse

from classes.rectangle import AsciiRectangle as Rect
from classes.rectangleParser import RectangleParser as RectPars

#_______________________________________________________________________
if __name__ == '__main__':
    print('\n\n\n')

    # parse command line arguments
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    RectPars.init_parser(parser)
    args: argparse.Namespace = parser.parse_args()

    h: int = args.height
    w: int = args.width

    # create rectangle
    r: Rect = Rect(h, w)

    print('\n\n\n')