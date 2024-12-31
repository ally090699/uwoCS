import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

/**
 * Class represents the maze
 * @author allisonso
 * 12/07/2023
 */
public class Maze {
	
	private Graph maze;
	private GraphNode entrance;
	private GraphNode exit;
	private int coinK;
	
	public Maze(String inputFile) throws MazeException{
	/**
	 * constructor that reads the input file and builds the 
	 * graph representing the maze. If the input file does not 
	 * exist, or the format of the input file is incorrect this 
	 * method should throw a MazeException. Read below to learn 
	 * about the format of the input file.
	 * @param inputFile is the string name of the file including extension
	 */
		try {
			FileInputStream file = new FileInputStream(inputFile);
			Scanner inFS = new Scanner(file);
			int scaleS = inFS.nextInt();
			int widthA = inFS.nextInt();
			int lengthL = inFS.nextInt();
			this.coinK = inFS.nextInt();
			
			int lenM = widthA * lengthL;
			this.maze = new Graph(lenM);
			int room = 0, master = 0;
			inFS.nextLine();
			
			while (inFS.hasNextLine()) {
				String lineM1 = inFS.nextLine();
				int i=0;
				room = master;
				char R = lineM1.charAt(i);
				while (R!=' ') {		//loop handles RHRHRH... line
					i++;
					if (R=='s') {
						try {
							this.entrance = this.maze.getNode(room);
						} catch (GraphException e) {
							System.out.println(e);
						}
					}
					else if (R=='x') {
						try {
							this.exit = this.maze.getNode(room);
						} catch (GraphException e) {
							System.out.println(e);
						}
					}
					if (i>lineM1.length()-1) {
						if (room==lenM-1) {
							master+=widthA;
						}
						break;
					}
					char H = lineM1.charAt(i);
					if (H!=' ') {
						if (H=='c') {	//marks a corridor
							try {
								this.maze.insertEdge(this.maze.getNode(room), this.maze.getNode(room+1), 0, "corridor");
								this.maze.insertEdge(this.maze.getNode(room+1), this.maze.getNode(room), 0, "corridor");
							} catch (GraphException e) {
								System.out.println(e);
							}
						}
						else if (H=='w') {	//marks a wall
							i++;
							room++;
							R = lineM1.charAt(i);
							continue;
						}
						int check  = (int) H;
						if (check<58) {
							check-=48;
							for (int j=0; j<10; j++) {		
								if (j==check) {	//marks # coins needed to open a door
									try {
										this.maze.insertEdge(this.maze.getNode(room), this.maze.getNode(room+1), j, "door");
										this.maze.insertEdge(this.maze.getNode(room+1), this.maze.getNode(room), j, "door");
										break;
									} catch (GraphException e) {
										System.out.println(e);
									}
								}
							}
						}
					}
					room++;
					i++;
					R = lineM1.charAt(i);	//next R value
				}
				if (inFS.hasNextLine()) {
					String lineM2 = inFS.nextLine();
					int k=0;
					room=master;
					char V = lineM2.charAt(k);
					while (V!=' ') {		//loop handles VWVWVW... line
						k++;
						if (V=='c') {	//marks a corridor
							try {
								this.maze.insertEdge(this.maze.getNode(room), this.maze.getNode(room+widthA), 0, "corridor");
								this.maze.insertEdge(this.maze.getNode(room+widthA), this.maze.getNode(room), 0, "corridor");
							} catch (GraphException e) {
								System.out.println(e);
							}
						}
						int check  = (int) V;
						if (check<58) {
							check-=48;
							for (int j=0; j<10; j++) {										
								if (check==j) {	//marks # coins needed to open a door
									try {
											this.maze.insertEdge(this.maze.getNode(room), this.maze.getNode(room+widthA), j, "door");
											this.maze.insertEdge(this.maze.getNode(room+widthA), this.maze.getNode(room), j, "door");
										break;
									} catch (GraphException e) {
										System.out.println(e);
									}
								}
							}
						}
						if (k>lineM2.length()-1) {
							master+=widthA;
							break;
						}
						
						k++;
						room++;
						V = lineM2.charAt(k);	//next V value
					}
				}
				if (master>=lenM) {
					break;
				}
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			System.out.println(e);
			throw new MazeException("Invalid file input.");
		} catch (InputMismatchException e) {
            throw new MazeException("Invalid file input format.");
        }
	}
	
	public Graph getGraph() {
	/**
	 * @return a reference to the Graph object representing the maze. 
	 * Throws a MazeException if the graph is null.
	 */
		return (this.maze!=null) ? this.maze : null;
	}
	
	public Iterator solve() {
	/**
	 * returns a java Iterator containing the nodes of the path from 
	 * the entrance to the exit of the maze, if such a path exists. 
	 * If the path does not exist, this method returns the value 
	 * null. For example for the maze described below the Iterator 
	 * returned by this method should contain the 
	 * nodes 0, 1, 5, 6, and 10
	 * @return list iterator of solution from helper function
	 */
		return solve_helper(this.entrance, this.exit, this.coinK);
	}
	
	private Iterator solve_helper(GraphNode enter, GraphNode exit, int money) {
		/**
		 * Recursive helper function to return maze solution
		 * @param enter is the updated entrance of the maze
		 * @param exit is the updated exit of the maze
		 * @param money is the updated coin amount available for use
		 * @return list iterator of solution
		 * @return null if no solution found
		 */
	    List<GraphNode> solution = new ArrayList<>();
	    int cash = money;	    
	    if (enter.equals(exit)) {
	    		exit.mark(true);
	    		solution.add(exit);
	        return solution.iterator();
	    }

	    enter.mark(true);
	    try {
	        Iterator<GraphEdge> edgeList = this.maze.incidentEdges(enter);
	        while (edgeList.hasNext()) {
	            GraphEdge edge = edgeList.next();
	            GraphNode next = edge.secondEndpoint();

	            if (!next.isMarked()) {
	                if (edge.getLabel().equals("corridor") || (edge.getLabel().equals("door") && (cash - edge.getType()) >= 0)) {
	                	int nCash =  cash-edge.getType();
	                	Iterator<GraphNode> check = solve_helper(next, exit, nCash);
	                    if (check != null) {
	                    		while (check.hasNext()) {
	                    			GraphNode fcheck = check.next();
	                    			if (fcheck.equals(enter)) {
	                    				break;
	                    			}
	                    			solution.add(fcheck);
	                    		}
	                        solution.add(0, enter);
	                        return solution.iterator();
	                    }
	                }
	            }
	        }
	        enter.mark(false);
	    } catch (GraphException e) {
	        System.out.println(e);
	    }

	    return null;
	}
}
