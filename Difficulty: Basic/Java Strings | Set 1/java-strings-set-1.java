// User function template for Java

class Solution {
    static String conRevstr(String S1, String S2) {
        // code here
        String s=S1+S2;
        String reversed=new StringBuilder(s).reverse().toString();
       return reversed;
    }
}