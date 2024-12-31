/**
 * A class containing methods necessary to compute a path from the park 
 * entrance to all the treasure chambers on the map.
 * @author Allison So
 * @version 1.0
 */
import java.io.IOException;

public class PathFinder {
	private Map pyramidMap;
	
	public PathFinder(String fileName) {
		/**
		 * Constructor creates an object of the Map Class and catches
		 * any exceptions.
		 * @param fileName, name of the file to be used to create the Map
		 */
		try {
			this.pyramidMap = new Map(fileName);
		}
		catch (IOException e){
			System.out.println("IOException" + e.getMessage());
		}
		catch (Exception e){
			System.out.println("Exception" + e.getMessage());
		}
	}
	
	public DLStack<Chamber> path() {
		/**
		 * Finds a path from the entrance to all treasure chambers,
		 * pushing all chambers into a stack to be returned.
		 * @return stack of items of the Chamber Class representing the path
		 */
		DLStack<Chamber> pathStack = new DLStack<Chamber>();
		Chamber start = this.pyramidMap.getEntrance();
		int numTreasures = this.pyramidMap.getNumTreasures();
		int foundTreasures = 0;
		pathStack.push(start);
		start.markPushed();
		while (!pathStack.isEmpty()) {
			Chamber currentChamber = pathStack.peek();
			if (currentChamber.isTreasure()==true && foundTreasures==numTreasures) {
				break;
			}
			else {
				Chamber c = bestChamber(currentChamber);
				if (c!=null) {
					if (c.isTreasure()==true) {
						foundTreasures+=1;
					}
					pathStack.push(c);
					c.markPushed();
				}
				else {
					Chamber result = pathStack.pop();
					result.markPopped();
				}
			}
		}
		return pathStack;
	}
	
	public Map getMap() {
		/**
		 * @return the pyramidMap.
		 */
		return this.pyramidMap;
	}
	
	public boolean isDim(Chamber currentChamber) {
		/**
		 * Checks if the chamber is dim by checking if it was not null,
		 * not sealed, not lighted and one of its neighbours is lighted.
		 * @return true, if all the conditions are met, otherwise false
		 */
		if (currentChamber!=null && currentChamber.isSealed()==false && currentChamber.isLighted()==false) {
			for (int i=0; i<6; ++i) {
				if (currentChamber.getNeighbour(i)!=null) {
					if (currentChamber.getNeighbour(i).isLighted()==true) {
						return true;
					}
				}
			}
			return false;
		}
		else {
			return false;
		}
	}
	
	public Chamber bestChamber(Chamber currentChamber) {
		/**
		 * Finds and returns the best chamber to move to from the current
		 * chamber, with features of greatest to lowest priority being:
		 * an adjacent unmarked treasure chamber, an unmarked lighted chamber,
		 * and an unmarked dim chamber. If no conditions are met, a null
		 * Chamber is returned.
		 * @return best chamber to move to from the current
		 * @param currentChamber, object referencing the current chamber
		 */
		if (currentChamber!=null) {
			for (int i=0; i<6; ++i) {
				Chamber thisChamber = currentChamber.getNeighbour(i);
				if (thisChamber!=null) {
					if (thisChamber.isTreasure()==true && thisChamber.isMarked()==false) {
						return thisChamber;
					}
				}
			}
			for (int i=0; i<6; ++i) {
				Chamber thisChamber = currentChamber.getNeighbour(i);
				if (thisChamber!=null) {
					if (thisChamber.isLighted()==true && thisChamber.isMarked()==false) {
						return thisChamber;
					}
				}
			}
			for (int i=0; i<6; ++i) {
				Chamber thisChamber = currentChamber.getNeighbour(i);
				if (thisChamber!=null) {
					if (isDim(thisChamber)==true && thisChamber.isMarked()==false) {
						return thisChamber;
					}
				}
			}
		}
		return null;
	}
	
	/**
	 * First, I read through the code and tried to get a basic understanding 
	 * of all classes that would be implemented or used in my code. Then, I 
	 * began by working on filling in as much of the code as I could break 
	 * down, ensuring any code that I could not fully flush out, that I 
	 * commented it out and ensured a proper return statement and print line 
	 * so I could see where the errors were. This began with the DLStack class 
	 * as it would serve as the foundation for the assignment. So, after filling 
	 * in as much of the methods as I could logically gather, I began debugging 
	 * using the TestStackMap class provided. After all tests except test 6 passed 
	 * (because test 6 uses Pathfinder), I focused on fixing and debugging the 
	 * PathFinder class. Fixing the class in order of the methods called in test 6 
	 * before I finally tested, fixed and debugged my code against the Pyramid 
	 * class provided.
	 */
}
