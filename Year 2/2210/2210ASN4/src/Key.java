/**
 * Class represents the key of the data items stored in the internal nodes of the binary search
 * tree implementing the ordered dictionary
 * @author allisonso
 * 11/17/2023
 */
public class Key {

	private String label;
	private int type;
	
	public Key(String theLabel, int theType) { 
		/**
		 * Constructor that initializes key instance
		 * variables label and type with the given 
		 * values.
		 * @param theLabel, the label to initialize
		 * the instance variable label
		 * @param theType, the integer to initialize 
		 * the instance variable type
		 */
		this.label = theLabel.toLowerCase();
		this.type = theType;
	}
	
	public String getLabel() { 
		/**
		 * @return the value of instance variable label.
		 */
		return this.label;
	}
	
	public int getType() { 
		/**
		 * @return the value of instance variable type.
		 */
		return this.type;
	}
	
	public int compareTo(Key k) { 
		/**
		 * Compares this key instance with the key given
		 * @param k, the key to be compared
		 * @return 0, if this key instance is equal 
		 * to the key given
		 * @return -1, if this key instance is smaller
		 * than the key given
		 * @return 1, otherwise
		 */
		if ((this.label.compareTo(k.label)==0)&&(this.type==k.type)) {
			return 0;
		}
		else if ((this.label.compareTo(k.label))<0) {
			return -1;
		}
		else if ((this.label.compareTo(k.label)==0)&&(this.type<k.type)) {
			return -1;
		}
		return 1;
	}
	
}
