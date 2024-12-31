
/**
 * Class representing a central repository for information about a 
 * WordLL game: It stores a mystery word and all word guesses 
 * tried so far. It keeps a history of the past word guesses in
 * a linked structure.
 * @author Allison So
 * @version 1.0
 */
public class WordLL {
	private Word mysteryWord;
	private LinearNode<Word> history;
	
	public WordLL(Word mystery) {
		/**
		 * Constructor initializing the history and mysteryWord
		 * attributes of this instance variable.
		 * @param mystery, Word object representing the mystery word
		 */
		this.history = null;
		this.mysteryWord = mystery;
	}
	
	public boolean tryWord(Word guess) {
		/**
		 * Checks if the Word object given (guess) matches the mystery
		 * Word, updating the labels of the guess and adding a copy of
		 * guess to the front of the history list.
		 * @param guess, Word object representing the word guessed
		 * @return true, if the word guessed matches the mysteryWord
		 * @return false, otherwise
		 */
		LinearNode<Word> newNode = new LinearNode<Word>(guess);
		newNode.setNext(this.history);
		this.history = newNode;
		if (guess.labelWord(this.mysteryWord)) {
			return true;
		}
		else {
			return false;
		}
		
	}
	
	public String toString() {
		/**
		 * @return string representation of the various Word objects
		 * held within the history linked list, separated by a newline.
		 */
		String result = "";
		LinearNode<Word> copy = this.history;
		while (this.history!=null) {
			result += this.history.getElement().toString() + "\n";
			if (this.history.getNext()==null) {
				this.history = copy;
				break;
			}
			else {
				this.history = this.history.getNext();
			}
		}
		return result;
	}
	
	/**
	 * I began by working on the Letter class as it was a superclass to ExtendedLetter, and because it 
	 * was the simplest of the four. After testing that the Letter class was alright using the first 
	 * three tests in the TestWordLL file, I began working on the ExtendedLetter class. Afterwards I 
	 * focused on filling any simpler methods like getters, setters, string returns etc., so that when 
	 * it came to testing, the program would not stop simply because the method was undefined. Then came 
	 * the challenge of understanding and working on the labelWord and tryWord methods. The biggest 
	 * challenge I faced was understanding how to move along the linked list as I was stuck for a period 
	 * of time trying to create new methods simply to return to the first node of the list after traversing 
	 * the entirety of it. Once I received TA help and better understood how to reference the node I 
	 * wanted, it was much easier to work my way through each test in the TestWordLL file and make the 
	 * necessary adjustments through the debugging view of Eclipse.
	 */
}
