import argparse

#_______________________________________________________________________
class RectangleParser:
    """
    This class is used to create the command line argument parser.
    """

    PROGRAM_NAME: str = 'rectangleParser.py'
    PROGRAM_DESC: str = str(
        'Prints rectangle to the screen based on user '
        'inputs.'
    )
    HEIGHT_DESC: str = 'Is the height of rectangle.'
    WIDTH_DESC: str = 'Is the width of rectangle.'



    #___________________________________________________________________
    def init_parser(parser: argparse.ArgumentParser) -> None:
        """
        Initializes argument parser.

        Parameters
            parser: argument parser

        Side Effects
            None

        Returns
            None
        """

        parser.prog = RectangleParser.PROGRAM_NAME
        parser.description = RectangleParser.PROGRAM_DESC

        parser.add_argument('--height'
            , help=RectangleParser.HEIGHT_DESC
            , action='store'
            , type=int
            , required=False
            , default=2
        )


        parser.add_argument('--width'
            , help=RectangleParser.WIDTH_DESC
            , action='store'
            , type=int
            , required=False
            , default=4
        )
        return




