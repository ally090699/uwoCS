/**
 * Class implements the user interface
 * @author allisonso
 * 11/17/2023
 */
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Interface {
	
	public static void main(String[] args) {
		String input = args[0];
		BSTDictionary newDict = new BSTDictionary();

		try {
			/**
			 * Reads lines from files
			 */
			BufferedReader in = new BufferedReader(new FileReader(input));
			String label;
			String typedata;
			
			while((label = in.readLine())!=null && (typedata= in.readLine())!=null) {
				/**
				 * Checks and declares type integer for all types of input
				 */
				char type = typedata.charAt(0);
				int tint;
				String data;
				
				if (type=='-') {
					tint = 3;
					data = typedata.substring(1);
				}
				else if (type=='+') {
					tint = 4;
					data = typedata.substring(1);
				}
				else if (type=='*') {
					tint = 5;
					data = typedata.substring(1);
				}
				else if (type=='/') {
					tint = 2;
					data = typedata.substring(1);
				}
				else {
					if (typedata.contains(".gif")) {
						tint = 7;
						data = typedata;
					}
					else if (typedata.contains(".jpg")) {
						tint = 6;
						data = typedata;
					}
					else if (typedata.contains(".html")) {
						tint = 8;
						data = typedata;
					}
					else {
						tint = 1;
						data = typedata;
					}
				}
				label = label.toLowerCase();
				Key newKey = new Key(label, tint);
				Record newRec = new Record(newKey, data);
				newDict.put(newRec);
				
				continue;
			}
			in.close();
		} 
		catch (FileNotFoundException e) {
			System.out.println("File Not Found: " + e);
		} 
		catch (IOException e) {
			System.out.println("IO Exception: " + e);
		} catch (DictionaryException e) {
			System.out.println("Dictionary Exception: " + e);
		} 
		
		StringReader keyboard = new StringReader();
		while (true) {
			/**
			 * Asks for user commands and handles each case separately
			 */
			String user = keyboard.read("Enter next command: ");
			String[] in = user.split(" ");
			String command = in[0];
		
			if (command.contentEquals("define")) {
				String word = in[1];
				Key check = new Key(word, 1);
				Record rec = newDict.get(check);
				if (rec!=null) {
					System.out.println(rec.getDataItem());
				}
				else {
					System.out.println("The word " + word + " is not in the ordered dictionary");
				}
			}
			else if (command.contentEquals("translate")) {
				String word = in[1];
				Key check = new Key(word, 2);
				Record rec = newDict.get(check);
				if (rec!=null) {
					System.out.println(rec.getDataItem());
				}
				else {
					System.out.println("There is no definition for the word " + word);
				}
			}
			else if (command.contentEquals("sound")) {
				String word = in[1];
				Key check = new Key(word, 3);
				Record rec = newDict.get(check);
				if (rec!=null) {
					SoundPlayer player = new SoundPlayer();
				    try {
						player.play(rec.getDataItem());
					} catch (MultimediaException e) {
						System.out.println("MultimediaException: " + e);
					}
				}
				else {
					System.out.println("There is no sound file for " + word);
				}
			}
			else if (command.contentEquals("play")) {
				String word = in[1];
				Key check = new Key(word, 4);
				Record rec = newDict.get(check);
				if (rec!=null) {
					SoundPlayer player = new SoundPlayer();
				    try {
						player.play(rec.getDataItem());
					} catch (MultimediaException e) {
						System.out.println("MultimediaException: " + e);
					}
				}
				else {
					System.out.println("There is no music file for " + word);
				}
			}
			else if (command.contentEquals("say")) {
				String word = in[1];
				Key check = new Key(word, 5);
				Record rec = newDict.get(check);
				if (rec!=null) {
					SoundPlayer player = new SoundPlayer();
				    try {
						player.play(rec.getDataItem());
					} catch (MultimediaException e) {
						System.out.println("MultimediaException: " + e);
					}
				}
				else {
					System.out.println("There is no voice file for " + word);
				}
			}
			else if (command.contentEquals("show")) {
				String word = in[1];
				Key check = new Key(word, 6);
				Record rec = newDict.get(check);
				if (rec!=null) {
					PictureViewer viewer = new PictureViewer();
				    try {
				    	viewer.show(rec.getDataItem());		
					} catch (MultimediaException e) {
						System.out.println("MultimediaException: " + e);
					}
				}
				else {
					System.out.println("There is no image file for " + word);
				}
			}
			else if (command.contentEquals("animate")) {
				String word = in[1];
				Key check = new Key(word, 7);
				Record rec = newDict.get(check);
				if (rec!=null) {
					PictureViewer viewer = new PictureViewer();
				    try {
				    	viewer.show(rec.getDataItem());		
					} catch (MultimediaException e) {
						System.out.println("MultimediaException: " + e);
					}
				}
				else {
					System.out.println("There is no animated image file for " + word);
				}
			}
			else if (command.contentEquals("browse")) {
				String word = in[1];
				Key check = new Key(word, 8);
				Record rec = newDict.get(check);
				if (rec!=null) {
					ShowHTML browser = new ShowHTML();
				    browser.show(rec.getDataItem());
				}
				else {
					System.out.println("There is no webpage called " + word);
				}
			}
			else if (command.contentEquals("delete")) {
				String word = in[1];
				String k = in[2];
				int kint = Integer.parseInt(k);
				Key check = new Key(word, kint);
				Record rec = newDict.get(check);
				if (rec!=null) {
					try {
						newDict.remove(check);
					} catch (DictionaryException e) {
						System.out.println("DictionaryException: " + e);
					}
				}
				else {
					System.out.println("No record in the ordered dictionary has key (" + word + ", " + k +").");
				}
			}
			else if (command.contentEquals("add")) {
				String word = in[1];
				String t = in[2];
				String c = user.substring(user.indexOf(t) + 1);
				int tint = Integer.parseInt(t);
				Key check = new Key(word, tint);
				Record rec = new Record(check, c);
				try {
					newDict.put(rec);
				} catch (DictionaryException e) {
					System.out.println("A record with the given key(" + word + ", "+tint + ") is already in the ordered dictionary.");
				}
			}
			else if (command.contentEquals("list")) {
				String prefix = in[1];
				Record current = newDict.smallest();
				String list = "";
				while (newDict.successor(current.getKey()) != null) {
				    list+= current.getKey().getLabel() + " ";
				    current = newDict.successor(current.getKey());
				}
				String[] larr = list.split(" ");
				String result = "";
				for (int i=0; i<larr.length; i++) {
					if (larr[i].startsWith(prefix)) {
						result+=larr[i] + ", ";
						if (larr[i].compareTo(prefix)==0) {
							continue;
						}
					}
				}
				String[] rarr = result.split(", ");
				if (rarr.length==0) {
					System.out.println("No label attributes in the ordered dictionary start with prefix " + prefix);
				}
				else {
					for (int i=0; i<rarr.length; i++) {
						if (i==rarr.length-1) {
							System.out.print(rarr[i]+ "\n");
						}
						else {
							System.out.print(rarr[i]+", ");
						}
					}
				}
				
			}
			else if (command.contentEquals("first")) {
				Record small = newDict.smallest();
				System.out.println(small.getKey().getLabel() + ", " + small.getKey().getType() + ", " + small.getDataItem());
			}
			else if (command.contentEquals("last")) {
				Record big = newDict.largest();
				System.out.println(big.getKey().getLabel() + ", " + big.getKey().getType() + ", " + big.getDataItem());
			}
			else if (command.contentEquals("exit")) {
				return;
			}
			else {
				System.out.println("Invalid command");
			}
		}
	    
	}

}
