import chess
import random
import numpy as np
from chessboard import display
from pettingzoo.classic import chess_v5
from time import sleep


def main():
    env = chess_v5.env()
    env.reset()

    board = get_board_from_env(env)
    display.start(board.fen())
    for agent in env.agent_iter():

        observation, reward, done, info = env.last()

        if done:
            break
        else:
            action = policy(observation, agent)
            env.step(action)
            display.update(board.fen())


def policy(observation, agent):

    action = random.choice(np.flatnonzero(observation['action_mask']))
    return action


def get_board_from_env(env):
    """Get board from petting zoo environment. Petting zoo wraps env multiple times, with board existing only at the
    'raw_env' level, so dropping recursively down environment levels to reach raw state with board.
    Only have to call this once for a given environment, will automatically update from then on"""
    if hasattr(env, 'board'):
        return env.board
    else:
        return get_board_from_env(env.env)


def random_move_game():

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
