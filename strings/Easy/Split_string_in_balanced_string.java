/***********   QUESTION ***********/
/*
 Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.
link : https://leetcode.com/problems/split-a-string-in-balanced-strings/
 */


/***********         APPROACH       ************/
/*
 We will traverse through the string and increase the count if L is found and decrease if R is found, so after a certain 
 point when both are equal (i.e L and R) count would be 0 and we will again start with the next character
 
 */

package hacktoberfeast;

import java.util.Scanner;

public class Split_string_in_balanced_string {
         
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a string : ");
		String str = sc.next();
		int substrings = StringSplit(str);
		System.out.println("The number of substrings formed are : "+substrings);
		
	}
	
	
public static int StringSplit(String s) {
	    //Initializing count to 0  to keep a track of  adjacent L and R
	    //res to store the total number of substrings
		int count=0,res=0;
		for(int i=0;i<s.length();i++)
		{
		if(s.charAt(i)=='R')
		//If a character is R increasing count by 1  
		//and if it L decreasing count by 1
		count++;
		else if(s.charAt(i)=='L')
		count--;
		//If count is equal to 0 , we have successfully found one substring
		//Hence we will increase result by 1
		if(count==0)
		res++;
		}
		//Return 
		return res ;
		}
}

/*   TIME COMPLEXITY will be O(N) where N is the length of the string    */

/*        SAMPLE OUTPUT     */
/*
Enter a string : 
LRLRLLRRLR
The number of substrings formed are : 4
 
 */
