from app.views.figures.Figure import Figure as Figure

class Rook(Figure):
    def __init__(self, x, y):
        Figure.__init__(self, "S", x, y)