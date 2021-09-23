class TicTacToe:
    # This class will be the instance of the game
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    # print the Default Board Index for user to map moves
    @staticmethod
    def default_board():
        for row in [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]:
            print(f" | {' | '.join(row)} | ")
        '''
        The output will look like this
        | 0 | 1 | 2 |
        | 3 | 4 | 5 |
        | 6 | 7 | 8 |
        '''

    def __str__(self):
        '''
        The output will look like this
        |   |   |   |
        |   |   |   |
        |   |   |   |
        '''
        # The String returned here will be displayed on the screen in when printing the instance of the class
        return "".join(
            f" | {' | '.join(row)} | \n"
            for row in [
                [self.board[i] for i in range(j * 3, (j + 1) * 3)]
                for j in range(3)
            ]
        )

    def available_space(self):
        # Returning a list containing the available index to play
        return [idx for idx, val in enumerate(self.board) if val == ' ']

    def available_space_count(self):
        # Returns the count of the available space in the board
        return self.board.count(' ')

    def make_move(self, pos, letter):
        # Does to move on the board as the pos argument
        if self.board[pos] == ' ':
            self.board[pos] = letter
            if self.check_win(pos, letter):
                self.winner = letter
            return True
        return False

    def check_win(self, pos, letter):

        # getting row index e.g if pos=4 4//3=1 hence we are in first row
        row_idx = pos//3

        # taking whole row in list [0,1,2
        #                           3,4,5
        #                           6,7,8]
        # [1*3:(1+1)*3]=[3:6] = [3,4,5] list slice

        row = self.board[row_idx*3:(row_idx+1)*3]
        if all(spot == letter for spot in row):
            return True

        # getting column index e.g if pos=4 4%3=1 hence we are in first column
        col_idx = pos % 3

        # taking whole column in list [0,1,2
        #                              3,4,5
        #                              6,7,8]
        # [col_idx+i*3] here i will be [0,1,2] for every itterattion
        # col=[1+0*3,1+1*3,1+2*3]=[1,4,7]

        col = [self.board[col_idx+i*3] for i in range(3)]
        if all(spot == letter for spot in col):
            return True

        # if pos is even the move done by the player is at a diagnol

        if pos % 2 == 0:
            # Hard input of diagonal value
            diagnol = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagnol):
                return True

            diagnol = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagnol):
                return True
        # If none true the the move was not a winning move
        return False

    def contains_space(self):
        return ' ' in self.board
