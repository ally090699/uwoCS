/*
 * A class representing the construction zone and includes methods for
 * displaying the board and checking the game status.
 * @author Allison So
 * @version 1.0
*/

public class GameBoard {
	
	private char[][] board;	//board array representing the construction zone
	private int size;		//size of the board array
	
	public GameBoard(int size) { 
		/*
		 * Constructor initializing board to a 2D character array of '.'
		 * representing empty positions.
		 * @param size, size of each side of the board array (square grid)
		 */
		int i;
		int j;
		this.size = size;
		this.board = new char[this.size+1][this.size+1];
		//creates a board instance that is one size larger than the size given
		//done to allow space for row and column labels to be stored and printed
		for (i=1; i<=this.size; ++i) {
			for (j=1; j<=this.size; ++j) {
				this.board[i][j] = '.';
			}
		}
	}
	
	public void placeToken(int row, int col, char token) {
		/*
		 * Places the given character token at the given row and column
		 * on the gameboard.
		 * @param row, the row value where the token is to be placed
		 * @param col, the column value where the token is to be placed
		 * @param token, the token character to be placed
		 */
		this.board[row+1][col+1] = token;
	}
	
	public boolean isPositionEmpty(int row, int col) {
		/*
		 * Checks whether the specified position on the board is empty
		 * denoted by '.'.
		 * @param row, the row value of the position to be checked
		 * @param col, the column value of the position to be checked
		 * @return true if empty or false if not empty
		 */
		if ((row+1>=this.size+1) || (row<0) || (col<0) || (col+1>=this.size+1)) {
			return false;
		}
		else if (this.board[row+1][col+1]=='.') {
			return true;
		}
		else {
			return false;
		}
	}
	
	public int getSize() {
		/*
		 * @return size of game board.
		 */
		return this.size;
	}
	
	public void displayBoard() {
		/*
		 * Prints the game board on the console, including row and 
		 * column labels.
		 */
		int i;
		int j;
		for (i=0; i<this.size+1; ++i) {
			for (j=0; j<this.size+1; ++j) {
				// prints all board labels before printing board values
				if ((i==0)&&(j==0)) {	
					//prints initial space at the top left corner of the board
					this.board[i][j] = ' ';
					System.out.print(this.board[i][j]);
					continue;
				}
				else if (i==0) {
					//prints column labels starting from letter A
					this.board[i][j] = (char) ('A' + j - 1);
					System.out.print(this.board[i][j]);
					continue;
				}
				else if (j==0) {
					//prints row labels starting from 0
					System.out.print(i-1);
				}
				System.out.print(this.board[i][j]);
			}
			//prints a new line whenever a row is complete
			System.out.println();
		}
	}
	
	public int checkForWinDirection(Player player) {
		/*
		 * Checks whether the player specified, won the game in any direction
		 * (left to right, bottom to top, diagonal from top left to 
		 * bottom right).
		 * @param player, the player making the moves
		 * @return 1, won by placing consecutive tokens left to right
		 * @return 2, won by placing consecutive tokens bottom to top
		 * @return 3, won by placing tokens from top left to bottom right
		 * @return 0, no win
		 */
		int i;
		int j;
		int count=0;
		//checks left-right
		for (i=1;i<this.size+1;++i) {
			for (j=1; j<this.size+1; ++j) {
				if (this.board[i][j]==player.getToken()) {
					++count;
				}
			}
			if (count==this.size) {
				return 1;
			}
			else {
				count=0;
			}
		}
		//checks bottom-top
		for (i=1;i<this.size+1;++i) {
			for (j=1; j<this.size+1; ++j) {
				if (this.board[j][i]==player.getToken()) {
					++count;
				}
			}
			if (count==this.size) {
				return 2;
			}
			else {
				count=0;
			}
		}

		//checks diagonal; final check, if no win here, returns 0
		for (i=1;i<this.size+1;++i) {
			if (this.board[i][i]==player.getToken()) {
				++count;
			}
		}
		if (count==this.size) {
			return 3;
		}
		else {
			return 0;
		}
	}
		
	public boolean checkForTie() {
		/*
		 * Checks whether the game board is full, indicating a tie.
		 * @return true if tie, false if not a tie
		 */
		int i;
		int j;
		int count=0;
		for (i=1;i<this.size+1;++i) {
			for (j=1; j<this.size+1; ++j) {
				if (this.board[i][j]!='.') {
					++count;
				}
			}
		}
		if (count==(this.size*this.size)) {
			return true;
		}
		else {
			return false;
		}
	}
	/*
	 * Initially, I began with the GameBoard class constructor and its 
	 * displayBoard() method as the two were closely related and would be the 
	 * foundation of the game. This challenged me initially as I wanted to store 
	 * all values before printing, including row and column labels. However, 
	 * after some trial and error, as well as speaking to a TA during live lab 
	 * hours, I realized I did not have to store these values before printing. 
	 * Next, I focused on filling all methods that were not as logically complex 
	 * like the getters, placeToken, and isPositionEmpty methods. Afterwards, I 
	 * focused on more logically complex methods like the makeMove, 
	 * CheckforWinDirection and CheckforTie method. This posed a challenge for 
	 * me during testing as several issues arose, however after seeking TA help I 
	 * was able to find a solution by placing several print lines within my loops 
	 * to find the infinite loop error and index errors. 
	 */
}
