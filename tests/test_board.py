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

    #Check horizontally from right to left
    def test_rook_right_to_left(self):
        boardGUI = BoardGuiTk ()

        boardGUI.board.field [1][3] = boardGUI.board.field [0][0]

        curr_pos = 1
        for x in [1,2,3,4]:
            for y in [0,1,2]:
                assert boardGUI.board.field [curr_pos][3].check_move_possible((curr_pos,3), (x, y), boardGUI.board) == True
            
            boardGUI.board.field [curr_pos][3] = 0
            curr_pos += 1
            boardGUI.board.field [curr_pos][3] = boardGUI.board.field [0][0]

    #Check horizontally from top to bottom
    def test_rook_top_to_bottom(self):
        boardGUI = BoardGuiTk ()

        boardGUI.board.field [1][0] = boardGUI.board.field [0][0]

        curr_pos = 0
        for y in [0,1,2,3]:
            for x in [2,3,4]:
                assert boardGUI.board.field [1][curr_pos].check_move_possible((1,curr_pos), (x, y), boardGUI.board) == True
            
            if curr_pos < 3:
                boardGUI.board.field [1][curr_pos] = 0
                curr_pos += 1
                boardGUI.board.field [1][curr_pos] = boardGUI.board.field [0][0]

    #Check horizontally from bottom to top
    def test_rook_bottom_to_top(self):
        boardGUI = BoardGuiTk ()

        boardGUI.board.field [4][0] = boardGUI.board.field [0][0]

        curr_pos = 0
        for y in [0,1,2,3]:
            for x in [1,2,3]:
                assert boardGUI.board.field [4][curr_pos].check_move_possible((4,curr_pos), (x, y), boardGUI.board) == True
            
            if curr_pos < 3:
                boardGUI.board.field [4][curr_pos] = 0
                curr_pos += 1
                boardGUI.board.field [4][curr_pos] = boardGUI.board.field [0][0]


##BISHOP TESTS
    #Check diagonally
    def test_bishop_main_diagonals(self):
        boardGUI = BoardGuiTk ()

        boardGUI.board.field [1][0] = boardGUI.board.field [0][1]
        moves = ((2,1),(3,2),(4,3))


        for x,y in moves:
            assert boardGUI.board.field [1][0].check_move_possible((1,0), (x, y), boardGUI.board) == True
        

        moves = ((3,1),(2,2),(1,3))
        boardGUI.board.field [1][0] = 0
        boardGUI.board.field [4][0] = boardGUI.board.field [0][1]

        for x,y in moves:
            assert boardGUI.board.field [4][0].check_move_possible((4,0), (x, y), boardGUI.board) == True

##KNIGHT TESTS
    #Check some initial L moves
    def test_knight_l_moves(self):
            boardGUI = BoardGuiTk ()

            boardGUI.board.field [2][1] = boardGUI.board.field [0][2]
            moves = ((1,3),(3,3),(4,2),(4,0))


            for x,y in moves:
                assert boardGUI.board.field [2][1].check_move_possible((2,1), (x, y), boardGUI.board) == True

##PAWN TESTS
    #Check some initial L moves
    def test_pawn_moves(self):
            boardGUI = BoardGuiTk ()

            boardGUI.board.field [1][0] = boardGUI.board.field [0][3]

            assert boardGUI.board.field [1][0].check_move_possible((1,0), (2,0), boardGUI.board) == True





    
        
        

        
