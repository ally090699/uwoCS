/**
 * A class representing a stack built via doubly linked list. 
 * @author Allison So
 * @version 1.0
*/
public class DLStack<T> implements DLStackADT<T> {
	private DoubleLinkedNode<T> top;
	private int numItems;
	
	public DLStack() {
		/**
		 * Constructor creates an empty stack where top is null
		 * and there are no items in the stack.
		 */
		this.top = null;
		this.numItems = 0;
	}
	
	public void push(T dataItem) {
		/**
		 * Adds the given dataItem to the top of the stack.
		 * @param dataItem, the item to be added to the top of the stack
		 */
		
		if (this.isEmpty()) {
			DoubleLinkedNode<T> newNode = new DoubleLinkedNode<T>(dataItem);
			DoubleLinkedNode<T> temp = this.top;
			this.top = newNode;
			this.top.setPrevious(temp);
			this.numItems+=1;
		}
		else {
			DoubleLinkedNode<T> newNode = new DoubleLinkedNode<T>(dataItem);
			while (this.top.getNext()!=null) {
				this.top = this.top.getNext();
			}
			this.top.setNext(newNode);
			newNode.setPrevious(this.top);
			this.top = newNode;
			this.numItems+=1;
		}
	}
	
	public T pop() throws EmptyStackException {
		/**
		 * Removes and returns the data item at the top of the stack. 
		 * An EmptyStackException is thrown if the stack is empty.
		 * @return popped stack item 
		*/
		if (this.isEmpty()) {
			throw new EmptyStackException("Stack is empty");
		}
		else {
			while (this.top.getNext()!=null) {
				this.top = this.top.getNext();
			}
			DoubleLinkedNode<T> poppedItem = this.top;
			if (this.top.getPrevious()==null) {
				this.top = poppedItem;
				this.numItems-=1;
				return poppedItem.getElement();
			}
			DoubleLinkedNode<T> front = this.top.getPrevious();
			front.setNext(poppedItem.getNext());
			this.top = front;
			this.numItems-=1;
			return poppedItem.getElement();
			
		}
	}
	
	public T pop(int k) throws InvalidItemException {
		/**
		 * Removes and returns the k-th data item from the top of the 
		 * stack. 
		 * An InvalidItemException is thrown if the value of k is larger 
		 * than the number of data items stored in the stack or if k 
		 * is less than or equal to zero. 
		 * @param k, index of stack item to return
		 * @return popped stack item
		 */		
		if (k<=0 || k>this.top.toString().split("").length) {
			throw new InvalidItemException("Invalid Item");
		}
		else {
			for (int i=1; i<=this.size(); ++i) {
				if (i==k) {
					DoubleLinkedNode<T> poppedItem = this.top;
					if (this.top.getNext()==null) {
						if (this.top.getPrevious()==null) {
							this.top = poppedItem.getNext();
						}
						else {
							DoubleLinkedNode<T> prev = this.top.getPrevious();
							prev.setNext(poppedItem.getNext());
							this.top = prev;
						}
						this.numItems-=1;
						return poppedItem.getElement();
					}
					else {
						DoubleLinkedNode<T> prev = this.top.getPrevious();
						DoubleLinkedNode<T> next = this.top.getNext();
						next.setPrevious(prev);
						prev.setNext(next);
						this.top = next;
						this.numItems-=1;
						return poppedItem.getElement();
					}
					
				}
				this.top = this.top.getPrevious();
				
				
			}
		}
		return null;
	}
	
	public T peek() throws EmptyStackException {
		/**
		 * Returns the data item at the top of the stack without 
		 * removing it. An EmptyStackException is thrown if the 
		 * stack is empty.
		 * @return item at top of stack
		 */
		if (isEmpty()) {
			throw new EmptyStackException("Empty Stack");
		}
		else {
			return this.getTop().getElement();
		}
	}
	
	public boolean isEmpty() {
		/**
		 * Checks if the stack is empty.
		 * @return true if the stack is empty and false otherwise
		 */
		if (this.numItems==0) {
			return true;
		}
		else {
			return false;
		}
	}
	
	public int size() {
		/**
		 * @return the number of data items in the stack.
		 */
		return this.numItems;
	}
	public DoubleLinkedNode<T> getTop() {
		/**
		 * @return node representing the top of the stack
		 */
		return this.top;
	}
	public String toString() {
		/**
		 * @return string representation of stack starting from the top 
		 * of the stack
		 */
		String arr = "";
		String result = "";
		while (this.top.getElement()!=null) {
			arr += this.top.getElement().toString() + " ";
			this.top = this.top.getNext();
		}
		String[] arrResults = arr.split(" ");
		for (int i=arrResults.length-1; i>=0;--i) {
			result+=arrResults[i] + " ";
		}
		return result;
	}
	
	
	
}
