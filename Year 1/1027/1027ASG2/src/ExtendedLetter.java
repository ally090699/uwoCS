/**
 * A subclass of the Letter class that extends its functionality.
 * The contents of the object are represented by a string instead of 
 * a single character. This subclass also introduces more features
 * like a family and a related attribute to the instance variable. 
 * @author Allison So
 * @version 1.0
 */
public class ExtendedLetter extends Letter{
	private String content;
	private int family;
	private boolean related;
	final private int SINGLETON = -1;
	
	public ExtendedLetter(String s) {
		/**
		 * Constructor initializing instance variables of the
		 * superclass using an arbitrary character. Further, also
		 * initializing the content, related and family instance
		 * variables.
		 * @param s, string to be assigned to the content variable
		 */
		super('c');
		this.content = s;
		this.related = false;
		this.family = SINGLETON;
		
	}
	
	public ExtendedLetter(String s, int fam) {
		/**
		 * Constructor initializing instance variables of the
		 * superclass using an arbitrary character. Further, also
		 * initializing the content, related and family instance
		 * variables.
		 * @param s, string to be assigned to the content variable
		 * @param fam, integer value to be assigned to the family
		 * variable. 
		 * Instance variables are considered related if the family
		 * values match.
		 */
		super('c');
		this.content = s;
		this.related = false;
		this.family = fam;
	}
	
	public boolean equals(Object other) {
		/**
		 * Checks if the other Object is an ExtendedLetter Object.
		 * @return false, if not.
		 * Further, checks if the other object's family and content
		 * instance variables match with this object instances values.
		 * If family values match, instance variables are related.
		 * @return true, if other is an ExtendedLetter object and 
		 * content of this object and other object match.
		 * @param other, variable representing object of Object class.
		 */
		if (other instanceof ExtendedLetter) {
			if (((ExtendedLetter) other).family==this.family) {
				this.related = true;
			}
			if (((ExtendedLetter) other).content.equals(this.content)) {
				return true;
			}
		}
		return false;
	}
	
	@Override
	public String toString() {
		/**
		 * @return string representation of this object instance.
		 * @return content surrounded with "." if unused and related
		 * @return content surrounded with decorators otherwise
		 */
		if (this.isUnused() && this.related==true) {
			return "." + this.content + ".";
		}
		else {
			return "" + super.decorator() + this.content + super.decorator();
		}
	}
	
	public static Letter[] fromStrings(String[] content,int[] codes) {
		/**
		 * Creates an array of Letter objects initialized in various
		 * ways depending on whether the parameter codes is null or not.
		 * @return array of Letter objects created.
		 * @param content, array of Strings to be used as the content 
		 * value of the Letter object created
		 * @param codes, array of code values to be used for the Letter
		 * object created
		 */
		Letter[] letters = new Letter[content.length];
		for (int i=0; i<content.length; ++i) {
			if (codes == null) {
				letters[i] = new ExtendedLetter(content[i]);
			}
			else {
				letters[i] = new ExtendedLetter(content[i],codes[i]);
			}
		}
		return letters;
	}
}
