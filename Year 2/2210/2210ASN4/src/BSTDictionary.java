/**
 * Class implements an ordered dictionary using a binary search tree
 * @author allisonso
 * 11/17/2023
 */
public class BSTDictionary implements BSTDictionaryADT{
	
	private BSTNode root;
	
	public BSTDictionary() {
		/**
		 * Constructor for the class
		 */
		this.root = new BSTNode(null);
	}
	
	public Record get (Key k) {
		/**
		 * @return record with key k
		 * @return null if record is not in the dictionary
		 */
		BSTNode node = this.root;
		while (node.getRecord()!=null) {
            int nvk = node.getRecord().getKey().compareTo(k);

            if (nvk == 0) {
                return node.getRecord();
            } 
            else if (nvk > 0) {
            		if (node.getLeftChild()==null) {
            			return null;
            		}
                	node = node.getLeftChild();
            }
            else {
            		if (node.getRightChild()==null) {
            			return null;
            		}
                node = node.getRightChild();
            }
		}
		return null;
	}
	
    public void put (Record d) throws DictionaryException {
    	/**
    	 * Inserts record d into the ordered dictionary. 
    	 * throws a DictionaryException if a record with the same key as the one given, is already
    	 * in the dictionary
    	 */
    		BSTNode newNode = new BSTNode(d);
        if (root==null || root.getRecord() == null) {
            root = new BSTNode(d);
            return;
        }
        BSTNode current = root;
        while (true) {
            int dvc = d.getKey().compareTo(current.getRecord().getKey());

            if (dvc == 0) {
                throw new DictionaryException("Duplicate key found.");
            } else if (dvc < 0) {
                if (current.getLeftChild() == null || current.getLeftChild().getRecord() == null) {
                		current.setLeftChild(newNode);
                    newNode.setParent(current);
                    break;
                } else {
                		current = current.getLeftChild();
                }
            } else {
                if (current.getRightChild() == null || current.getRightChild().getRecord() == null) {
                		current.setRightChild(newNode);
                    newNode.setParent(current);
                    break;
                } else {
                		current = current.getRightChild();
                }
            }
        }

    }

   public void remove (Key k) throws DictionaryException {
	   	/**
	   	 * Removes record with the same Key attribute as k from the dictionary. 
	   	 * throws a DictionaryException if such a Record is not in the dictionary.
	   	 */
    	BSTNode node = this.root;
		while (node!=null && node.getRecord()!=null) {
			BSTNode parent = node.getParent();
			int nvk = node.getRecord().getKey().compareTo(k);
			if (nvk == 0) {
	            if (node.getLeftChild() == null && node.getRightChild() != null) {
	                // Node with only right child
	                if (parent != null) {
	                    if (parent.getLeftChild() == node) {
	                        parent.setLeftChild(node.getRightChild());
	                    } 
	                    else {
	                        parent.setRightChild(node.getRightChild());
	                    }
	                    node.getRightChild().setParent(parent);
	                } 
	                else {
	                    // Node is root
	                    root = node.getRightChild();
	                    root.setParent(null);
	                }
	            } 
	            else if (node.getRightChild() == null && node.getLeftChild() != null) {
	                // Node with only left child
	                if (parent != null) {
	                    if (parent.getLeftChild() == node) {
	                        parent.setLeftChild(node.getLeftChild());
	                    } else {
	                        parent.setRightChild(node.getLeftChild());
	                    }
	                    node.getLeftChild().setParent(parent);
	                } else {
	                    // Node is root
	                    root = node.getLeftChild();
	                    root.setParent(null);
	                }
	            } 
	            else if (node.getLeftChild() != null && node.getRightChild() != null) {
	                // Node with two children
	                BSTNode successor = new BSTNode(smallest(node.getRightChild()));
	                node.setRecord(successor.getRecord());
	                remove(successor.getRecord().getKey());
	            } 
	            else {
	                // Node with no children
	                if (parent != null) {
	                    if (parent.getLeftChild() == node) {
	                        parent.setLeftChild(null);
	                    } 
	                    else {
	                        parent.setRightChild(null);
	                    }
	                } 
	                else {
	                    // Node is root
	                    root = null;
	                }
	            }
	            return;
	        } 
			else if (nvk < 0) {
				if (node.getRightChild()!=null) {
        				node = node.getRightChild();
        				continue;
        			}
				break;
	        } 
			else {
	            if (node.getLeftChild()!=null) {
        				node = node.getLeftChild();
        				continue;
        			}
	            break;
	        }
	    }
	    throw new DictionaryException("No record found.");
	}

    public Record successor (Key k) {
    	/**
    	 * @return Record from the ordered dictionary with smallest key larger than k); 
    	 * @return null if the given key has no successor.
    	 */
    	BSTNode node = this.root;
    	BSTNode successor = null;
		while (node.getRecord()!=null) {
			int nvk = node.getRecord().getKey().compareTo(k);
            if (nvk > 0) {
            		successor = node;
            		node = node.getLeftChild();
            }
            else if (nvk < 0) {
            		node = node.getRightChild();
            }
            else {
            		if (node.getRightChild()!=null) {
            			node = node.getRightChild();
                    while (node.getLeftChild() != null) {
                    	node = node.getLeftChild();
                    	}
                    successor = node;
            		}
            		break;
            }
		}
		
		if (successor!=null) {
			return successor.getRecord();
		}
		return null;
    }

    public Record predecessor (Key k) {
    	/**
    	 * @return Record from the ordered dictionary with largest key smaller than k; 
    	 * @return null if the given key has no predecessor.
    	 */
    	BSTNode node = this.root;
		BSTNode pred = null;
		while (node!=null && node.getRecord()!=null) {
			int nvk = node.getRecord().getKey().compareTo(k);
	        if (nvk < 0) {
	        		pred = node;
	        		node = node.getRightChild();
	        }
	        else if (nvk > 0) {
	        		node = node.getLeftChild();
	        }
	        else {
	        		if (node.getLeftChild()!=null) {
	        			node = node.getLeftChild();
	        			while (node.getRightChild() != null) {
	        		        node = node.getRightChild();
	        		    }
	        		    pred = node;
	        		}
	        		break;
	        }
		}
	
		if (pred!=null) {
			return pred.getRecord();
		}
		return null;
    }

    public Record smallest () {
    	/**
    	 * @return the Record with smallest key in the ordered dictionary. 
    	 * @return null if the dictionary is empty.
    	 */
    	BSTNode node = this.root;
    	while (node!=null && node.getLeftChild() != null) {
   	        node = node.getLeftChild();
   	    }
   	    return node.getRecord();
    }
    
    private Record smallest(BSTNode r) {
    	/**
    	 * helper function for remove function
    	 * @return the Record with smallest key in the ordered dictionary. 
    	 * @return null if the dictionary is empty.
    	 */
    	BSTNode node = r;
		while (node!=null && node.getLeftChild() != null) {
	        node = node.getLeftChild();
	    }
	    return node.getRecord();
    }

    public Record largest () {
    	/**
    	 * @return the Record with largest key in the ordered dictionary. 
    	 * @return null if the dictionary is empty.
    	 */
    	BSTNode node = this.root;
		while (node!=null && node.getRightChild() != null) {
	        node = node.getRightChild();
	    }
	    return node.getRecord();
    }
    	
}
   
