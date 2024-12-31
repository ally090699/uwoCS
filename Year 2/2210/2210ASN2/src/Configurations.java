/**
 * Class describes methods for the game
 * @author Allison So
 * @version 1.0
 */
public class Configurations {
	
	private char[][] board;
	private int size;
	private int winLen;
	
	public Configurations (int board_size, int lengthToWin, int max_levels) {
		/**
		 * Constructor creates an empty board.
		 * @param board_size, dictates the dimensions of the game board
		 * @param lengthToWin, the number of tiles in a shape needed to win
		 * @param max_levels, the max level of the game tree to be used
		 */
		this.board = new char[board_size][board_size];
		for (int i=0; i<board_size; i++) {
			for (int j=0; j<board_size; j++) {
				this.board[i][j] = ' ';
			}
		}
		this.size = board_size;
		this.winLen = lengthToWin;
	}
	
	public HashDictionary createDictionary() {
		/**
		 * @return empty dictionary
		 */
		HashDictionary emptyDict = new HashDictionary(9973);
		return emptyDict;
	}
	
	public int repeatedConfiguration(HashDictionary hashTable) {
		/**
		 * Creates a string representation of the game board
		 * @return score of string if string exists in the hashTable, otherwise
		 * @return -1
		 */
		String config = "";
		int score;
		for (int i=0; i<this.size; i++) {
			for (int j=0; j<this.size; j++) {
				config += this.board[i][j];
			}
		}
		score = hashTable.get(config);
		return score;
	}
	
	public void addConfiguration(HashDictionary hashDictionary, int score) {
		/**
		 * Creates and inserts string representation of game board
		 * and the associated score into the hashDictionary
		 */
		String config = "";
		for (int i=0; i<this.size; i++) {
			for (int j=0; j<this.size; j++) {
				config += this.board[i][j];
			}
		}
		Data newData = new Data(config, score);
		hashDictionary.put(newData);
	}
	
	public void savePlay(int row, int col, char symbol) {
		/**
		 * Stores symbol in board[row][col].
		 */
		this.board[row][col] = symbol;
		return;
	}
	
	public boolean squareIsEmpty(int row, int col) {
		/**
		 * @return true if board tile is empty
		 * @return false otherwise
		 */
		if (this.board[row][col]==' ') {
			return true;
		}
		
		return false;
	}
	
	private boolean checkX(int row, int col, char symbol) {
		/**
		 * @return true, if X-shape found
		 * @return false, otherwise
		 */
		int count = 1;
		boolean foundX = false;
		if ((row-1>=0)&&(col-1>=0)&&(row+1<this.size)&&(col+1<this.size)) {
			if ((this.board[row-1][col-1]==symbol)&&
					(this.board[row+1][col+1]==symbol)&&
					(this.board[row-1][col+1]==symbol)&&
					(this.board[row+1][col-1]==symbol)) {									
				count+=4;
				foundX = true; //initial check for base Xshape
			}
		}
		
		boolean d1 = false;
		boolean d2 = false;
		boolean d3 = false;
		boolean d4 = false;
		
		if (foundX) {
			for (int k=2; k<=this.winLen; k++) {
				if ((row-k>=0)&&(col-k>=0)) {
					if (k==2 && this.board[row-k][col-k]==symbol) {
						d1 = true;
						count+=1;
					}
					else if (d1==true && this.board[row-k][col-k]==symbol) {
						count+=1;
					}
				}
				if ((row+k<this.size)&&(col+k<this.size)) {
					if (k==2 && this.board[row+k][col+k]==symbol) {
						d2 = true;
						count+=1;
					}
					else if (d2==true && this.board[row+k][col+k]==symbol) {
						count+=1;
					}
				}
				if ((row-k>=0)&&(col+k<this.size)) {
					if (k==2 && this.board[row-k][col+k]==symbol) {
						d3 = true;
						count+=1;
					}
					else if (d3==true && this.board[row-k][col+k]==symbol) {
						count+=1;
					}
					
				}
				if ((row+k<this.size)&&(col-k>=0)) {
					if (k==2 && this.board[row+k][col-k]==symbol) {
						d4 = true;
						count+=1;
					}
					else if (d4==true && this.board[row+k][col-k]==symbol) {
						count+=1;
					}
				}
				if (count==this.winLen) {
					return true;
				}
			}
		}
		
		return false;
	}
	
	private boolean checkPlus(int row, int col, char symbol) {
		/**
		 * @return true, if plus-shape found
		 * @return false, otherwise
		 */
		int count = 1;
		boolean foundPlus = false;
		if (((row-1)>=0)&&((col-1)>=0)&&((row+1)<this.size)&&((col+1)<this.size)) {
			if ((this.board[row-1][col]==symbol)&&
					(this.board[row+1][col]==symbol)&&
					(this.board[row][col+1]==symbol)&&
					(this.board[row][col-1]==symbol)) {
				count+=4; 	//initial check for base plus shape
				foundPlus = true;				
			}
		}
		
		boolean p1 = false;
		boolean p2 = false;
		boolean p3 = false;
		boolean p4 = false;
		
		if (foundPlus) {
			for (int k=2; k<=this.winLen; k++) {
				if ((row-k)>=0) {
					if (this.board[row-k][col]==symbol) {
						count+=1;
						p1 = true;
					}
					else if (p1==true && this.board[row-k][col]==symbol) {
						count+=1;
						if (count==this.winLen) {
							return true;
						}
					}
				}
				if ((row+k)<this.size) {
					if (this.board[row+k][col]==symbol) {
						count+=1;
						p2 = true;
					}
					else if (p2==true && this.board[row+k][col]==symbol) {
						count+=1;
						if (count==this.winLen) {
							return true;
						}
					}
				}
				if ((col+k)<this.size) {
					if (this.board[row][col+k]==symbol) {
						count+=1;
						p3 = true;
					}
					else if (p3==true && this.board[row][col+k]==symbol) {
						count+=1;
						if (count==this.winLen) {
							return true;
						}
					}
				}
				if ((col-k)>=0) {
					if (this.board[row][col-k]==symbol) {
						count+=1;
						p4 = true;
					}
					else if (p4==true && this.board[row][col-k]==symbol) {
						count+=1;
						if (count==this.winLen) {
							return true;
						}
					}
				}
			}
		}
		
		return false;
	}
	
	public boolean wins(char symbol) {
		/**
		 * @return true, if x-shape or +shape of the symbol specified, 
		 * it must be the length of lengthToWin
		 * @return false, otherwise
		 */
		for (int i=0; i<this.size; i++) {
			for (int j=0; j<this.size; j++) {
				if (this.board[i][j]==symbol) {
					if ((checkX(i, j, symbol) || (checkPlus(i, j, symbol)))) {
						return true;
					}
				}
			}
		}
		return false;
	}
	
	public boolean isDraw() {
		/**
		 * @return true, if board is full and no one has won the game.
		 */
		int count = 0;
		for (int i=0; i<this.size; i++) {
			for (int j=0; j<this.size; j++) {
				if (this.board[i][j]==' ') {
					count += 1;
				}
			}
		}
		if (count==0 && wins('O')==false && wins('X')==false) {
			return true;
		}
		return false;
	}
	
	public int evalBoard() {
		/**
		 * @return 3, if computer wins
		 * @return 2, if draw game
		 * @return 0, if player wins
		 * @return 1, otherwise
		 */
		if (wins('O')==true) {
			return 3;
		}
		else if (wins('X')==true) {
			return 0;
		}
		else if (isDraw()==true) {
			return 2;
		}
		else {
			return 1;
		}
	}
	
}
