import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Class represents an undirected graph
 * @author allisonso
 * 12/07/2023
 */
public class Graph implements GraphADT {
	
	private List<GraphNode> setV;
	private List<GraphEdge> setE;
	private int size;
	
	public Graph(int n) {
		/**
		 * creates an empty graph with n nodes and no edges. The 
		 * names of the nodes are 0, 1, . . . ,n−1.
		 * @param n is the size of the graph
		 */
		this.size = n;
		setV = new ArrayList<GraphNode>(this.size);
		setE = new ArrayList<GraphEdge>(((this.size-1)*2)+((this.size+1)*2));
		
		for (int i=0; i<this.size; i++) {
			GraphNode node = new GraphNode(i);
			setV.add(node);
		}
	}
	 
	public void insertEdge(GraphNode u, GraphNode v, int edgeType, String label) throws GraphException {
		/**
		 * Adds to the graph an edge connecting nodes u and v. 
		 * Throws a GraphException if 
		 * either node does not exist or if there is already
		 * an edge connecting the given nodes.
		 * @param u, the first endpoint of the edge
		 * @param v, the second endpoint of the edge
		 * @param edgeType, the number of coins taken by this edge
		 * @param label, whether or not it is a door or a corridor
		 */
		
		GraphEdge edge = new GraphEdge(u, v, edgeType, label);
		if (setE.contains(edge)==true) {
			throw new GraphException("Edge already exists.");
		}
		else if (setV.contains(u)==false || setV.contains(v)==false) {
			throw new GraphException("Node does not exist.");
		}
		setE.add(edge);
	}
	
	public GraphNode getNode(int name) throws GraphException {
		/**
		 * @return node with the specified name. 
		 * Throws a GraphException, if no node with 
		 * this name exists.
		 * @param name, the name of the node to be found
		 */
		for (GraphNode node: setV) {
			if (node.getName()==name) {
				return node;
			}
		}
		throw new GraphException("Node " + name + "does not exist.");
	}
	
	public Iterator incidentEdges(GraphNode u) throws GraphException {
		/**
		 * @return list iterator storing all the edges incident on
		 * node u. 
		 * @return null if u does not have any edges 
		 * incident on it. 
		 * Throws a GraphException if u is not a node of the graph
		 * @param u, the first edgepoint to be found
		 */
		if (setV.contains(u)==false) {
			throw new GraphException("Node does not exist.");
		}
		List<GraphEdge> incidentedges = new ArrayList<>();
		for (GraphEdge edge : setE) {
			if (edge.firstEndpoint().equals(u)) {
				incidentedges.add(edge);
			}
		}
		
		return incidentedges.iterator();
	}
	
	public GraphEdge getEdge(GraphNode u, GraphNode v) throws GraphException {
		/**
		 * @return the edge connecting nodes u and v.  
		 * Throws a GraphException if there is no edge between u and 
		 * v or if u or v are not nodes of the graph.
		 * @param u, the first edgepoint
		 * @param v, the second edgepoint
		 */
		if (setV.contains(u)==false || setV.contains(v)==false) {
			throw new GraphException("Edge does not exist.");
		}
		
		for (GraphEdge edge: setE) {
			if (edge.firstEndpoint().equals(u) && edge.secondEndpoint().equals(v)) {
				return edge;
			}
		}
		throw new GraphException("Edge does not exist.");
	}
	
	public boolean areAdjacent(GraphNode u, GraphNode v) throws GraphException {
		/**
		 * @return true if nodes u and v are adjacent; 
		 * @return false otherwise. 
		 * Throws a GraphException if u or v are not 
		 * nodes of the graph.
		 * @param u, first edgepoint
		 * @param v, second edgepoint
		 */
		if (setV.contains(u)==false || setV.contains(v)==false) {
			throw new GraphException("Node does not exist.");
		}
		
		for (GraphEdge edge: setE) {
			if ((edge.firstEndpoint().equals(u) && edge.secondEndpoint().equals(v)) || (edge.firstEndpoint().equals(v) && edge.secondEndpoint().equals(u))) {
				return true;
			}
		}
		return false;
		
	}
	
}
