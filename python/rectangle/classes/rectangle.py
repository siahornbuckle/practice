class AsciiRectangle:
    """
    This class is used to construct a ascii rectangle.
    """
    
    #___________________________________________________________________
    def __init__(self, height: int, width: int):
        """
        Parameters
            height: height of the rectangle
            width : width  of the rectangle 
        """
        self.height_: int = height
        self.width_ : int = width
        self.drawShape()


        return 
    #___________________________________________________________________
    def drawShape(self):
        """
        Draws ASCII shape.

        Parameters
            none

        Side Effects
            Prints shape to screen.

        Returns
            none
        """
        self.drawHoriz()
        self.drawSides()
        self.drawHoriz()
        
        return
    
    #___________________________________________________________________
    def drawHoriz(self):
        """
        Prints top or bottom of rectangle to screen.

        Parameters
            none

        Side Effects
            Draws horizontal line.

        Returns
            none
        """
        out_str: str = ' ' + '-' * self.width_
        print(out_str)
        return
    
    #___________________________________________________________________
    def drawSides(self):
        """
        Prints side of rectangle to screen.

        Parameters
            none

        Side Effects
            Draws two vertical line.

        Returns
            none
        """
        out_str: str = f'|{' ' * self.width_}|\n'
        print(out_str * self.height_)
        return

    
