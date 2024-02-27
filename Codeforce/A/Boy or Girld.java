//# https://codeforces.com/problemset/problem/236/A
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
public class BoyOrGirl {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String[] inputKeys;
		inputKeys = input.nextLine().split("");
		Set<String> uniqueValues = new HashSet<>(); 
	    for (String value : inputKeys) { 
	        uniqueValues.add(value); 
	    } 
	    System.out.println(uniqueValues.size()%2==0 ? "CHAT WITH HER!" : "IGNORE HIM!");
	}
}