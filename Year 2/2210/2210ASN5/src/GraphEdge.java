/**
 * Class represents an edge of the graph
 * @author allisonso
 * 12/07/2023
 */
public class GraphEdge {
	
	private GraphNode[] endpoints = new GraphNode[2];
	private int type;
	private String label;
	
	public GraphEdge(GraphNode u, GraphNode v, int type, String label) {
		/**
		 * the constructor for the class. 
		 * @param u and v, end points of the edge
		 * @param type, number of coins required by the edge
		 * @param label, "corridor" or "door"
		 */
		this.endpoints[0] = u;
		this.endpoints[1] = v;
		this.type = type;
		this.label = label;
		
	}
	
	public GraphNode firstEndpoint() {
		/**
		 * @return the first end point of the edge.
		 */
		return this.endpoints[0];
	}
	
	public GraphNode secondEndpoint() {
		/**
		 * @return the second end point of the edge.
		 */
		return this.endpoints[1];
	}
	
	public int getType() {
		/**
		 * @return the type of the edge.
		 */
		return this.type;
	}
	
	public void setType(int newType) {
		/**
		 * sets the type of the edge to the specified value.
		 */
		this.type = newType;
	}
	
	public String getLabel() {
		/**
		 * @return the label of the edge.
		 */
		return this.label;
	}
	
	public void setLabel(String newLabel) {
		/**
		 * @set the label of the edge to the specified value.
		 */
		this.label = newLabel;
	}
}
