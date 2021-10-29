"""
Unit tests for the board
"""
#We add all the files in the app directory so that they can be found
#from sys import path
#path.append('..\\EASYCHESS')
#path.append('app\\views')

from app.views.BoardGuiTk import BoardGuiTk

class TestBoard:


    """
        Every test here is based on the board.field coordinates, where we check if some initial moves are possible to be made
    """

##ROOK TESTS
    #Check horizontally from left to right
    def test_rook_left_to_right(self):
        boardGUI = BoardGuiTk ()

        boardGUI.board.field [1][0] = boardGUI.board.field [0][0]

        curr_pos = 1
        for x in [1,2,3,4]:
            for y in [1,2,3]:
                assert boardGUI.board.field [curr_pos][0].check_move_possible((curr_pos,0), (x, y), boardGUI.board) == True
            
            boardGUI.board.field [curr_pos][0] = 0
            curr_pos += 1
            boardGUI.board.field [curr_pos][0] = boardGUI.board.field [0][0]
