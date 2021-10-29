"""
Unit tests for the board
"""
#We add all the files in the app directory so that they can be found
#from sys import path
#path.append('..\\EASYCHESS')
#path.append('app\\views')
import tkinter
from app.views.Board import Board
from app.views.BoardGuiTk import BoardGuiTk
from app.views.figures.Figure import Figure as Figure
from app.views.figures.Figure import Rook as Rook
from app.views.figures.Figure import Bishop as Bishop
from app.views.figures.Figure import Knight as Knight
from app.views.figures.Figure import Pawn as Pawn

class TestBoard:


    """
        Every test here is based on the board.field coordinates, where we check if some initial moves are possible to be made
    """

##ROOK TESTS
    #Check horizontally from left to right
    def test_rook_left_to_right(self):
        #figures = [Figure.Rook("white"), Figure.Bishop("white"), Figure.Knight("white"), Figure.Pawn("white"),
        #                Figure.Rook("blue"), Figure.Bishop("blue"), Figure.Knight("blue"), Figure.Pawn("blue")]

        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),
                        Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]
        board = Board(figures)

        board.field [1][0] = board.field [0][0]

        curr_pos = 1
        for x in [1,2,3,4]:
            for y in [1,2,3]:
                assert board.field [curr_pos][0].check_move_possible((curr_pos,0), (x, y), board) == True
            
            board.field [curr_pos][0] = 0
            curr_pos += 1
            board.field [curr_pos][0] = board.field [0][0]

    