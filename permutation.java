import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

public class permutation {
	
	 static Set<String> set;
	 static Set<String> set2;
	 static StringBuilder string;
	
	  static void printPermutn(String str,int i) {
	    
		  set2  = new LinkedHashSet<String>();
		      
			 for (int j = i; j < str.length(); j++) {
				
				string.delete(0, str.length());
				string.append(str);
	            string.setCharAt(i, str.charAt(j));
	            string.setCharAt(j, str.charAt(i));
	            
	             set.add(string.toString());
	             set2.add(string.toString());
			 }
	         
			 if(i < str.length())
			 {
			      i=i+1;
			     for(String s:set2) {
			    	 printPermutn(s,i); 
			     }
			    
			     
			 }
			 
			
	    }

	public static void main(String[] args) {
		String s = "abcd";
		set  = new LinkedHashSet<String>();
		//set2  = new LinkedHashSet<String>();
		string = new StringBuilder();
        printPermutn(s,0);
        System.out.println(set.toString());
	}

}
