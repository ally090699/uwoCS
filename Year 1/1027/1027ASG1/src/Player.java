/*
 * A class representing the player and includes methods for marking a move 
 * and calculating the score.
 * @author Allison So
 * @version 1.0
*/

public class Player {
	
	private char token;	//the player's token to be placed on the board
	private int score;	//the player's score
	
	public Player() {
		/*
		 * Constructor initializes the token and the score of the player.
		 */
		this.token = '+';
		this.score = 0;
	}
	
	public void makeMove(GameBoard board, int row, int col) {
		/*
		 * Places the player's token on the board at the given row and column.
		 * @param board, the board created for this instance (this game)
		 * @param row, the row value of the move to be made
		 * @param col, the column value of the move to be made
		 */
		board.placeToken(row, col, this.token);
	}
	
	public char getToken() {
		/*
		 * @return player's token
		 */
		return this.token;
	}

	public int getScore() {
		/*
		 * @return player's current score
		 */
		return this.score;
	}

	public void addScore(int increment) {
		/*
		 * Increases the player's score by the given increment value.
		 */
		this.score+=increment;
	}
}
