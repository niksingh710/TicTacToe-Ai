import argparse
from player import HumanPlayer, RandomComputerPlayer, SuperComputerPlayer
from tictactoe import TicTacToe

__author__ = 'Nikhil Singh'
__email__ = 'nik.singh710@gmail.com'
__github__ = 'https://github.com/niksingh710'
__telegram__ = 'https://t.me/niksingh710'


def play(game, x_player, o_player, verbose=False):
    if verbose:
        game.default_board()
    letter = 'X'
    while game.contains_space():
        move = x_player.get_move(
            game) if letter == "X" else o_player.get_move(game)

        if game.make_move(move, letter):
            if verbose:
                print(f"{letter} has made the move {move}")
                print(game)
            if game.winner:
                if verbose:
                    print(f"{letter} has won!")
                return letter
            letter = "O" if letter == "X" else "X"
    if verbose:
        print("It's a tie.")


def test(n=10, verbose=False):
    x, o, t = 0, 0, 0
    for _ in range(n):
        x_player, o_player = RandomComputerPlayer(
            "X"), SuperComputerPlayer("O")
        game = TicTacToe()
        win = play(game, x_player, o_player, verbose)
        if win == 'X':
            x += 1
        elif win == 'O':
            o += 1
        else:
            t += 1
    print(f"Total Games played       : {n}")
    print(f"X wins (Super Computer)  : {o}")
    print(f"O wins (Random Computer) : {x}")
    print(f"Times it tied            : {t}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Common Options')
    parser.add_argument('-v', '--verbose', dest='verbose',
                        help='Put the game in verbose mode', action='store_true',)
    parser.add_argument('-t', '--test', dest='times', type=int,
                        help='Runs the test case with the given value')
    parser.add_argument('-r', '--random', dest='random',
                        help='Set the against player to Random Player', action='store_true')
    args = parser.parse_args()

    if args.times:
        test(args.times, args.verbose)
    else:
        if not args.random:
            x_player, o_player = HumanPlayer("X"), SuperComputerPlayer("O")
        else:
            x_player, o_player = HumanPlayer("X"), RandomComputerPlayer("O")
        game = TicTacToe()
        play(game, x_player, o_player, args.verbose)
