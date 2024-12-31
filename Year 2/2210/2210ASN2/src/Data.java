/**
 * Class represents the records that will be stored in the HashDictionary.
 * @author Allison So
 * @version 1.0
 */
public class Data {
	
	public String key;
	public int num;
	
	public Data(String config, int score) {
		/**
		 * Constructor initializes new Data object with given configuration
		 * and score. 
		 * @param config, string variable containing current board layout.
		 * @param score
		 */
		this.key = config;
		this.num = score;
	}
	
	public String getConfiguration() {
		/**
		 * @return configuration of this Data object
		 */
		return this.key;
	}
	
	public int getScore() {
		/**
		 * @return score of this Data object
		 */
		return this.num;
	}
}
