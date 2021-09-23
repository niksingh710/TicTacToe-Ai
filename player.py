import random
import math


class Player:
    # Base Class of Player Type takes the player Playing Input ['X','O'] and initializes it.
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        pass


class RandomComputerPlayer(Player):
    # This Class inherits from the Player class
    def __init__(self, letter):
        super().__init__(letter)

    # Base class function is overridden and in prameter the game instance is passed.
    # Returns random value from the available spaces in the game board.
    def get_move(self, game):
        return random.choice(game.available_space())


class HumanPlayer(Player):
    # Also Inherits from the Player class. but asks value from the user.
    def __init__(self, letter):
        super().__init__(letter)

    # Till the input is not a integer and in range (0-8) it will ask ask input
    def get_move(self, game) -> int:
        valid_move = False
        while not valid_move:
            move = input("Enter your move in between (0-8): ")
            try:
                move = int(move)
                if move not in game.available_space():
                    raise ValueError
                valid_move = True
            except ValueError:
                print("Invalid Input please Try again")
        return move


class SuperComputerPlayer(Player):
    # Also Inherits from the Player class. uses minimax algorithm to get the position.
    def __init__(self, letter):
        super().__init__(letter)

    # Test all the possibilities and the return the most optimal position to win
    def get_move(self, game) -> int:
        # return random value if the board is empty
        if game.available_space_count() == 9:
            return random.choice(game.available_space())
        else:
            return self.minmax(game, self.letter)['position']

    def minmax(self, state, player) -> dict:
        # assigning current player as the max_player and other the other letter
        max_player = self.letter
        other_player = 'O' if player == 'X' else "X"

        if state.winner == other_player:
            # returning score value with positive if i am the other player and negative if m not
            return {'position': None, 'score': 1*(state.available_space_count()+1) if other_player == max_player else -1*(state.available_space_count()+1)}
        elif not state.available_space():
            # returning zero as a tie state if no state left
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_space():
            state.make_move(possible_move, player)

            sim_score = self.minmax(state, other_player)

            state.board[possible_move] = ' '
            state.winner = None
            sim_score['position'] = possible_move

            if (
                player == max_player
                and sim_score['score'] > best['score']
                or player != max_player
                and sim_score['score'] < best['score']
            ):
                best = sim_score
        return best
