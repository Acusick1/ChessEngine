from chessboard import display
import chess
from time import sleep
import random


def main():

    board = chess.Board()
    display.start(board.fen())
    while not board.is_game_over(claim_draw=True):
        move_list = board.generate_legal_moves()

        if move_list:

            num_moves = board.legal_moves.count()
            chosen_move = random.randint(0, num_moves - 1)

            i = 0
            while i <= chosen_move:
                move = next(move_list)
                i += 1

            board.push(move)
            display.update(board.fen())
            sleep(1)

    display.terminate()


if __name__ == '__main__':
    main()
