/**
 * A class representing a single letter that will be used in the game. 
 * Each game letter also has an accompanying integer label which 
 * indicates whether it is used, unused, or correct with respect to 
 * the mystery word.
 * @author Allison So
 * @version 1.0
 */
public class Letter {
	private char letter;						
	private int label;		// label attribute with optional values declared below
	private static final int UNSET = 0;
	private static final int UNUSED = 1;
	private static final int USED = 2;
	private static final int CORRECT = 3;
	
	public Letter(char c) { 
		/**
		 * Constructor initializing label instance variable to unset
		 * and the letter instance variable to the character (c) given.
		 * @param character to be used to initialize letter
		 */
		this.label = UNSET;
		this.letter = c;
	}
	
	public boolean equals(Object otherObject) {
		/**
		 * Checks if otherObject is an object of the Letter class first,
		 * then it checks if the letter attribute of this instance is
		 * equal to that of the otherObject instance.
		 * @return true, if the otherObject is a Letter object and 
		 * the letter attributes match
		 * @param otherObject is an Object instance variable of the
		 * Object class
		 */
		if (otherObject instanceof Letter) {
			if (this.letter== ((Letter) otherObject).letter) {
				return true;
			}
			else {
				return false;
			}
		}
		else {
			return false;
		}
	}
	
	public String decorator() {
		/**
		 * @return string representing the decorator associated with 
		 * the instance variable's label value
		 */
		if (this.label == USED) {
			return "+";
		}
		else if (this.label == UNUSED) {
			return "-";
		}
		else if (this.label == CORRECT) {
			return "!";
		}
		else if (this.label == UNSET) {
			return " ";
		}
		else {
			return "this.label has invalid value";
		}
	}
	
	@Override
	public String toString() {
		/**
		 * @return string representation of the instance variable's
		 * letter and label in the order of the decorator, the letter
		 * and the decorator again.
		 */
		String result = "";
		result = decorator() + this.letter + decorator();
		return result;
	}
	
	public void setUnused() {
		/**
		 * Sets the value of label to UNUSED
		 */
		this.label = UNUSED;
	}
	
	public void setUsed() {
		/**
		 * Sets the value of label to USED
		 */
		this.label = USED;
	}
	
	public void setCorrect() {
		/**
		 * Sets the value of label to CORRECT
		 */
		this.label = CORRECT;
	}
	
	public boolean isUnused() {
		/**
		 * Checks if the label of this instance variable is UNUSED
		 * @return true, if label is UNUSED
		 * @return false, if label is not UNUSED
		 */
		if (this.label == UNUSED) {
			return true;
		}
		else {
			return false;
		}
	}
	
	public static Letter[] fromString(String s) {
		/**
		 * Creates an array of objects using the given string s.
		 * One Letter object is created and stored per character in
		 * the string s.
		 * @return array of Letter objects
		 * @param s, string to be converted to an array
		 */
		Letter[] arrayObj = new Letter[s.length()];
		for (int i=0; i<s.length(); ++i) {
			Letter obj = new Letter(s.charAt(i));
			arrayObj[i] = obj;
		}
		return arrayObj;
	}
	
}
