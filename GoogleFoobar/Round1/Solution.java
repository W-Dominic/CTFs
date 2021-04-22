import java.util.*;
public class Solution {
    public static String solution(String s) {
    	// Your code here
    	ArrayList<String> positions = new ArrayList<String>();
    	for(char c : s.toCharArray()){
    	    char temp = Character.toLowerCase(c);
    	    int pos = ((int)temp) - 96;
    	    String bin = Integer.toBinaryString(pos);
    	    positions.add(bin);
	    System.out.println(bin);
    	}
	return null;    	
    }
    public static void main(String[] args){
    	//test here	   
	String foo = solution("code");
    }
}
