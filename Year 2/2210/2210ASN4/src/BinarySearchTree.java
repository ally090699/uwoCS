/**
 * Class represents a binary search tree
 * @author allisonso
 * 11/17/2023
 */
public class BinarySearchTree {

	private BSTNode root;
	
	public BinarySearchTree() {
		/**
		 * Constructor that creates a leaf node
		 * as the root of the tree
		 */
		this.root = new BSTNode(null);
	}
	
	BSTNode getRoot() {
		/**
		 * @return root node of this binary search tree
		 */
		return this.root;
	}
	
	BSTNode get(BSTNode r, Key k) {
		/**
		 * @param r, tree to be checked for node
		 * @param k, key to be found in tree r
		 * @return node in tree with root r storing
		 * the given key
		 * @return null, otherwise
		 */
		if (r.isLeaf()==true) {
			return r;
		}
		else {
			if (r.getRecord().getKey()==k) {
				return r;
			}
			else {
				if (r.getRecord().getKey().compareTo(k)<0) {
					return get(r.getRightChild(),k);
				}
				else {
					return get(r.getLeftChild(), k);
				}
			}
		}
	}
	
	boolean insert(BSTNode r, Record d) throws DictionaryException {
		/**
		 * Adds record to tree with root r
		 * Throws a DictionaryException if the tree
		 * already stores a record with the same key
		 * as d.
		 */
		BSTNode p = get(r, d.getKey());
		if (p.isLeaf()==false) {
			return false;
		}
		else if (p.getRecord().getKey().compareTo(d.getKey())==0) {
			throw new DictionaryException("Key already stored in tree.");
		}
		else {
			Record newRec = new Record(d.getKey(),d.getDataItem());
			BSTNode newNode = new BSTNode(null);
			p.setRecord(newRec);
			p.setLeftChild(newNode);
			p.setRightChild(newNode);
			return true;
		}
		
	}
	
	boolean remove(BSTNode r, Key k) {
		/**
		 * Deletes the node with the given key from the tree with root r. Throws a DictionaryException if the tree does not store a record with the given key.
		 */
		BSTNode p = get(r, k);
		if (p.isLeaf()==true) {
			return false;
		}
		else {
			if (p.getLeftChild().isLeaf()==true) {
				BSTNode child2 = p.getRightChild();
				BSTNode parent2 = p.getParent();
				if (parent2!=null) {
					if (parent2.getLeftChild()==null) {
						child2 = parent2.getRightChild();
					}
					else {
						child2 = parent2.getLeftChild();
					}
				}
				else {
					r = child2;
				}
				return true;
			}
			else {
				BSTNode s = smallest(p.getRightChild());
				Record newRec = new Record(s.getRecord().getKey(),s.getRecord().getDataItem());
				p.setRecord(newRec);
				return remove(s,s.getRecord().getKey());
				
				
			}
		}
		
	}
	
	BSTNode successor(BSTNode r, Key k) {
		/**
		 * @return node storing the successor of the given key in the tree with root r; 
		 * @return null if the successor does not exist.
		 */
		BSTNode p = get(r, k);
		if (p.getRightChild().getLeftChild()!=null||p.getRightChild().getRightChild()!=null) {
			return smallest(p.getRightChild());
		}
		else {
			p = p.getParent();
			while ((p!=null)&&(p.getRecord().getKey().compareTo(k)<0)) {
				p = p.getParent();
			}
			return p;
		}
	}
	
	BSTNode predecessor(BSTNode r, Key k) {
		/**
		 * @return the node storing the predecessor of the given key in the tree with root r; 
		 * @return null if the predecessor does not exist.
		 */
		BSTNode p = get(r, k);
		if (p.getLeftChild().getLeftChild()!=null||p.getLeftChild().getRightChild()!=null) {
			return largest(p.getLeftChild());
		}
		else {
			p = p.getParent();
			while ((p!=null)&&(p.getRecord().getKey().compareTo(k)<0)) {
				p = p.getParent();
			}
			return p;
		}
	}
	
	BSTNode smallest(BSTNode r) {
		/**
		 * @return the node with the smallest key in tree with root r.
		 */
		if (r==null) {
			return null;
		}
		else {
			BSTNode p = r;
			while (p.isLeaf()==false) {
				p = p.getLeftChild();
			}
			return p.getParent();
		}
	}
	
	BSTNode largest (BSTNode r) {
		/**
		 * @return the node with the largest key in tree with root r.
		 */
		if (r==null) {
			return null;
		}
		else {
			BSTNode p = r;
			while (p.isLeaf()==false) {
				p = p.getRightChild();
			}
			return p.getParent();
		}
	}
}
