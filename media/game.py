class GameOfLifeTorus:
    def __init__(self, board):
        self.board = board
        self.n = len(board)

    def neighbourSum(self, i, j):
        """Compute and return the number of live neighbours of cell (i,j)."""
        return (self.board[(i-1+self.n)%self.n][(j-1+self.n)%self.n] +
                self.board[(i-1+self.n)%self.n][j] + 
                self.board[(i-1+self.n)%self.n][(j+1)%self.n] +
                self.board[i][            (j+1)%self.n] +
                self.board[(i+1)%self.n][(j+1)%self.n] +
                self.board[(i+1)%self.n][j] +
                self.board[(i+1)%self.n][(j-1+self.n)%self.n] +
                self.board[i][            (j-1+self.n)%self.n])

    def nextPattern(self):
        """Update the board to the next pattern according to the game's rules."""
        new_board = [[0]*self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                live_neighbours = self.neighbourSum(i,j)
                if self.board[i][j] == 1:
                    # Cell is alive
                    if live_neighbours in (2,3):
                        new_board[i][j] = 1
                else:
                    # Cell is dead
                    if live_neighbours == 3:
                        new_board[i][j] = 1
        self.board = new_board

    def printBoard(self):
        """Print the current board, replacing zeros with spaces and ones with asterisks."""
        for row in self.board:
            print(' '.join(['*' if x else ' ' for x in row]))
        print('')

# Driver program
    def main():
        # Create initial patterns
        pattern1 = [[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,1,1,1,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]]

        pattern2 = [[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,1,1,1,0,0,0,0],
                    [0,0,0,1,0,1,0,0,0,0],
                    [0,0,0,1,1,1,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]]

        pattern3 = [[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]]

        # Print the patterns and ask user to choose one
        print("Choose a pattern to play with:")
        print("1. Pattern 1")
        print("2. Pattern 2")
        print("3. Pattern 3")
        choice = int(input("Enter your choice: "))

        if(choice==1):
            game_board = pattern1
        elif(choice==2):

            game_board = pattern2
        elif choice == 3:
            game_board = pattern3
        else:
            print("Invalid choice. Exiting the game...")
            return
        print("Starting game...\n")

        # Play the game
        play_game = True
        while play_game:
            game_board.printBoard()
            choice = input("Press 'n' to show next generation, 'q' to quit: ")
            if choice == 'n':
                game_board.nextPattern()
            elif choice == 'q':
                play_game = False
            else:
                print("Invalid choice. Please try again.")

        print("Game over.")
