/**
 * Class represents a node of the graph
 * @author allisonso
 * 12/07/2023
 */
public class GraphNode {
	
	private int name;
	private boolean mark;
	
	public GraphNode(int n) {
		/**
		 * the constructor for the class. Creates a node with the 
		 * given name. 
		 * @param n, the name of the node
		 */
		this.name = n;
	}
	
	public void mark(boolean mark) {
		/**
		 * marks the node with the specified value.
		 */
		this.mark = mark;
	}
	
	public boolean isMarked() {
		/**
		 * @return the value with which the node has been marked.
		 */
		return this.mark;
	}
	
	public int getName() {
		/**
		 * @return the name of the node.
		 */
		return this.name;
	}
}
