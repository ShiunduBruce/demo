from app.views.figures.Figure import Figure as Figure

class Pawn(Figure):
    def __init__(self, x, y):
        Figure.__init__(self, 'SorD', x, y)