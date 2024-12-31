/**
 * Class implements all methods needed to create a dictionary
 * @author Allison So
 * @version 1.0
 */

import java.util.LinkedList;

public class HashDictionary implements DictionaryADT{
		
	private LinkedList<Data>[] hash;
	private int hsize;
	
	private int polyHashing(String config, int x, int M) {
		/**
		 * @returns the location in the hashtable that config will be stored
		 * @param x, integer value that results in least collisions, to be determined
		 * @param M, prime number denoting the size of the hash table
		 */
		int val = config.charAt(0);
		for (int i=0; i<config.length(); i++) {
			val = (val * x + config.charAt(i)) % M;
		}
		return val;
	}
	
	public HashDictionary(int size) {
		/**
		 * Creates an empty dictionary of the given size
		 */
		this.hash = new LinkedList[size];	
		this.hsize = size;
	}
	
	public int put (Data record) throws DictionaryException {
		/**
		 * Adds record to the dictionary and throws DictionaryException
		 * if the record already exists.
		 * @return 1, if adding a record produces a collision
		 * @return 0, otherwise
		 */
		int hlocation = polyHashing(record.getConfiguration(),36,this.hsize);
		
		if (hash[hlocation] == null) {
			hash[hlocation] = new LinkedList<Data>();
		}
		
		for (Data value : hash[hlocation]) {
			if (value.getConfiguration().equals(record.getConfiguration())) {
				throw new DictionaryException();
			}
		}
		
		hash[hlocation].add(record);
		return (hash[hlocation].size()>1) ? 1 : 0;
	}
	
	public void remove (String config) throws DictionaryException {
		/**
		 * Removes the Data record with the given configuration from
		 * the dictionary. If the configuration is not found in the
		 * hash table, then a DictionaryException is thrown.
		 */
		
		for (int i=0; i<this.hash.length; i++) {
			if (this.hash[i]==null) {
				continue;
			}
			for (int j=0; j<this.hash[i].size(); j++)
				if (this.hash[i].get(j).getConfiguration().equals(config)) {
					this.hash[i].remove(j);
					return;
				}
		}
		
		throw new DictionaryException();
	}
	
	public int get (String config) {
		/**
		 * @return score stored in record of dictionary with the given
		 * configuration
		 * @return -1, if configuration not found in dictionary
		 */
		
		for (int i=0; i<this.hash.length; i++) {
			if (this.hash[i]==null) {
				continue;
			}
			for (int j=0; j<this.hash[i].size(); j++)
				if (this.hash[i].get(j).getConfiguration().equals(config)) {
					return this.hash[i].get(j).getScore();
				}
		}
		
		return -1;
	}
	
	public int numRecords() {
		/**
		 * @return number of Data objects stored in the hash dictionary
		 */
		return this.hash.length;
	}
}
