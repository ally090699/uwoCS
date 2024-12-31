/**
 * Class represents a node of the binary search tree
 * @author allisonso
 * 11/17/2023
 */
public class BSTNode {

	private Record rec;
	private BSTNode left;
	private BSTNode right;
	private BSTNode parent;
	
	public BSTNode(Record item) {
		/**
		 * The constructor for the class.
		 */
		this.rec = item;
		this.left = null;
		this.right = null;
		this.parent = null;
	}
	
	public Record getRecord() { 
		/**
		 * @return Record object stored in this node.
		 */
		return this.rec;
	}
	
	public void setRecord (Record d) {
		/**
		 * Stores the given record in this node.
		 */
		this.rec = d;
	}
	
	public BSTNode getLeftChild() {
		/**
		 * @return left child.
		 */
		return this.left;
		
	}
	
	public BSTNode getRightChild() { 
		/**
		 * @return right child.
		 */
		return this.right;
	}
	
	public BSTNode getParent() {
		/**
		 * @return the parent.
		 */
		return this.parent;
	}
	
	public void setLeftChild(BSTNode u) {
		/**
		 * Sets the left child to the specified value.
		 */
		this.left = u;
	}
	
	public void setRightChild(BSTNode u) {
		/**
		 * Sets the right child to the specified value.
		 */
		this.right = u;
	}
	
	public void setParent(BSTNode u) {
		/**
		 * Sets the parent to the specified value.
		 */
		this.parent = u;
	}
	
	public boolean isLeaf() {
		/**
		 * @return true if this node is a leaf; 
		 * @return false otherwise
		 */
		if ((this.left==null)&&(this.right==null)) {
			return true;
		}
		return false;
	}
	
}
