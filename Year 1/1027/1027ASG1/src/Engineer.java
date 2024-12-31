/*
 * A class representing the rival engineer and includes methods for marking its 
 * move based on the selected difficulty level and blocking the player’s path.
 * @author Allison So
 * @version 1.0
*/

import java.util.Random;

public class Engineer extends Player {
	private char token;		//the engineer's token to be placed on the board
	private boolean hardMode;	//false if 'easy' mode, true if 'hard' mode
	private static Random rnd = new Random();	//rnd object created
	
	public Engineer(boolean hardMode) {
		/*
		 * Constructor initializing the token and hardMode value provided.
		 * @param hardMode true/false, representing difficulty (2/1) chosen
		 */
		this.hardMode = hardMode;
		this.token = '0';
	}
	@Override
	public void makeMove(GameBoard board, int playerLastRow, int playerLastCol) {
		/*
		 * Places rival engineer's token on board either randomly (1) or 
		 * strategically (2), based on the difficulty (1/2) chosen.
		 * @param board, the board created for this instance (this game)
		 * @param playerLastRow, the row value of the player's last move
		 * @param playerLastCol, the column value of the player's last move
		 */
		int i;
		if (this.hardMode==false) {
			boolean isTokenDown = false;
			/*
			 * searches for a random position on the board that is empty
			 * once found, places token and exits method.
			 */
			while (!isTokenDown) {
				int randRow = rnd.nextInt(board.getSize());
				int randCol = rnd.nextInt(board.getSize());
				if (board.isPositionEmpty(randRow, randCol)==true) {
					board.placeToken(randRow, randCol, this.token);
					isTokenDown = true;
					return;
				}
			}
		}
		else {
			/*
			 * Strategically places the token to the right of the player's 
			 * last move. Once placed, the method is exited.
			 */
			for (i=1; i<board.getSize();++i) {
				if (board.isPositionEmpty(playerLastRow, playerLastCol+i)==true) {
					board.placeToken(playerLastRow, playerLastCol+i, this.token);
					return;
				}
				else if (board.isPositionEmpty(playerLastRow-i, playerLastCol)==true) {
					board.placeToken(playerLastRow-i, playerLastCol, this.token);
					return;
				}
			}
			/*
			 * If no space to the right of the player's last move, goes into 
			 * this loop, where token is placed above the player's last move.
			 * Once placed, the method is exited.
			 */
		}
	}
	@Override
	public char getToken() {
		/*
		 * @return engineer's token.
		 */
		return this.token;
	}
}
