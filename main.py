import chess
import chess.svg
import chess.engine
import numpy as np

class chess_board:

    def __init__(self,):
        self.chess_board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("C:\\Users\\Desktop\\PycharmProjects\\RLChess\\stockfish_15_x64_avx2.exe")

    def render_board(self):
        chess.svg.board(self.chess_board).__str__()

    def reset_board(self):
        self.chess_board.reset()

    def current_board_state(self):
        string_board = list(self.chess_board.__str__())
        print(string_board)
        board_arr = np.asarray(string_board, dtype='str')
        print(board_arr.reshape((8,16)))

        return board_arr

    def get_move(self, move):
        return move.uci()

    def move(self,int_move_to_take):
       move = list(self.chess_board.legal_moves)[int_move_to_take]
       self.chess_board.push(move)
       score = self.engine.analyse(self.chess_board, chess.engine.Limit(depth=20))['score'].relative.score()
       n_actions = len(list(self.chess_board.legal_moves))
       return score, self.chess_board.is_game_over(), self.chess_board, n_actions

    def get_legal_moves(self):
        return self.chess_board.legal_moves

if __name__ == '__main__':
    chess_board = chess_board()
    chess_board.render_board()
    print(chess_board.current_board_state())
    # print(chess_board.chess_board)
    print(chess_board.get_legal_moves())

