/**
 * Class represents the records to be stored in the internal nodes of the binary search tree. 
 * @author allisonso
 * 11/17/2023
 */
public class Record {
	
	private Key theKey;
	private String data;
	
	public Record(Key k, String theData) { 
		/**
		 * Constructor initializes new Record object 
		 * with given parameters
		 * @param k, key given
		 * @param theData, data given
		 */
		this.theKey = k;
		this.data = theData;
	}
	
	public Key getKey() {
		/**
		 * @return value of this instance variable key
		 */
		return this.theKey;
	}
	
	public String getDataItem() {
		/**
		 * @return value of this instance variable data
		 */
		return this.data;
	}
}
