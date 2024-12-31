
/**
 * Class representing a word in the game that is comprised of any 
 * number of letters. Each letter is represented by a Letter object. 
 * The Letter objects are stored in a linked list formed by objects of
 * the class LinearNode. Each node in the linked list stores an object 
 * of the class Letter. 
 * @author Allison So
 * @version 1.0
 */
public class Word {
	private LinearNode<Letter> firstLetter;
	
	public Word(Letter[ ] letters) { 
		/**
		 * Constructor initializes firstLetter as the first node of 
		 * the linked list by creating a linked list according
		 * to the array of Letter Objects provided.
		 * @param letters, array of Letter Objects provided
		 */
		LinearNode<Letter> front = null;
		LinearNode<Letter> newNode;
		for (int i = letters.length-1; i >= 0; i--) {
			newNode = new LinearNode<Letter> (letters[i]);
			newNode.setNext(front);
			front = newNode;
		}
		this.firstLetter = front;
	}
	
	public String toString() {
		/**
		 * @return string representation of this object instance
		 * starting with "Word: ", followed by each Letter object
		 * surrounded by each Letter's decorators.
		 */
		String result = "Word: ";
		LinearNode <Letter> front = this.firstLetter;
		LinearNode <Letter> current = front;
		while (current.getElement()!=null) {
			result += current.getElement().toString() + " ";
			if (current.getNext()==null) {
				current = front;
				break;
			}
			current = current.getNext();
		}
		return result;
	}
	
	public boolean labelWord(Word mystery) {
		/**
		 * Checks if this object instance matches the mystery word
		 * given and if the position of the Letter within the array
		 * matches, labelling the Letter object accordingly.
		 * If the content matches but the position differs, the Letter
		 * is given the label, USED.
		 * If the content matches and the position matches, the Letter
		 * is given the label, CORRECT.
		 * If the content does not match, the Letter is given the 
		 * label, UNUSED.
		 * @return true, if this Word object matches the mystery Word
		 * @return false, otherwise
		 * @param mystery, Word object representing the mystery word
		 */
		int i=0;
		int j=0;
		int count = 0;
		LinearNode <Letter> front = this.firstLetter;
		LinearNode <Letter> current = front;
		LinearNode <Letter> mystFront = mystery.firstLetter;
		LinearNode <Letter> mystCurrent = mystFront;
		
		String compString = "";
		String mystString = "";
		LinearNode <Letter> newCopy = front;
		LinearNode <Letter> newMyst = mystFront;
		while (newCopy.getElement()!=null) {
			/*
			 * Creates a string representation of the Word, removing the decorators and adding a "|"
			 */
			compString += newCopy.getElement().toString().replace(newCopy.getElement().decorator(), "")+"|";
			if (newCopy.getNext()==null) {
				newCopy = front;
				break;
			}
			newCopy = newCopy.getNext();
		}
		
		while (newMyst.getElement()!=null) {
			mystString += newMyst.getElement().toString().replace(newMyst.getElement().decorator(), "")+"|";
			if (newMyst.getNext()==null) {
				newMyst = mystFront;
				break;
			}
			newMyst = newMyst.getNext();
		}
		/*
		 *  creates a new string array using the string representation of Word, replacing the "|" with 
		 *  spaces that will be used as separators
		 */
		String[] arrCompare = compString.replace("|", " ").split(" ");
		String[] arrMystery = mystString.replace("|", " ").split(" ");
		
		while (current.getElement()!=null) {
			while (mystCurrent.getElement()!=null) {
					if (current.getElement().equals(mystCurrent.getElement())) {
						if (i<arrCompare.length && j<arrMystery.length) {
							if (arrCompare[i].equals(arrMystery[j]) && i==j) {
								current.getElement().setCorrect();
								count+=1;
								mystCurrent = mystFront;
								j=0;
								break;
							}
							else if (arrCompare[i].equals(arrMystery[j])) {
								current.getElement().setUsed();
								mystCurrent = mystFront;
								j=0;
								break;
							}
						}
					}
					else {
						current.getElement().setUnused();
					}
					if (mystCurrent.getNext()!=null) {
						mystCurrent = mystCurrent.getNext();
						++j;
					}
					else {
						j=0;
						mystCurrent = mystFront;
						break;
					}
					
			}
			if (current.getNext()!=null) {
				current = current.getNext();
				++i;
			}
			else {
				current = front;
				break;
			}	
		}
		if (count-1==i) {
			return true;
		}
		
		return false;		
	}
}
