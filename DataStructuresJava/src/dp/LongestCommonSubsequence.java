package dp;

import java.util.*;

public class LongestCommonSubsequence {
    private static Map<String, Integer> memo = new HashMap<String, Integer>();

    // Recursive solution - exponential
    private static Integer lcs(String x, String y){
        int m = x.length();
        int n = y.length();
        if(m == 0 || n == 0)
            return 0;
        if(x.charAt(m-1) == y.charAt(n-1)){
            return 1 + lcs(x.substring(0, m-1), y.substring(0, n-1));
        } else {
            return Math.max(lcs(x.substring(0, m), y.substring(0, n-1)),
                    lcs(x.substring(0, m-1), y.substring(0, n)));
        }
    }

    // Recursive solution with memoization - O(mn) with O(mn) space
    private static Integer lcsDP(String x, String y){
        Integer m = x.length();
        Integer n = y.length();
        if(m == 0 || n == 0)
            return 0;
        String key = m + "|" + n;

        if(!memo.containsKey(key)){
            if(x.charAt(m-1) == y.charAt(n-1)) {
                memo.put(key, 1 + lcs(x.substring(0, m-1), y.substring(0, n-1)));
            } else {
                memo.put(key, Math.max(lcs(x.substring(0, m), y.substring(0, n-1)), lcs(x.substring(0, m-1), y.substring(0, n))));
            }
        }
        return memo.get(key);
    }

    // Iterative solution - O(mn) with O(mn) space - space can be reduced to O(n)
    private static Integer lcsDPIter(String x, String y){
        Integer m = x.length();
        Integer n = y.length();
        Integer[][] matrix = new Integer[m+1][n+1];
        for(int i=0; i<=m; i++){
            matrix[i][0] = 0;
        }
        for(int i=0; i<=n; i++){
            matrix[0][i] = 0;
        }
        for(int i=1; i<=m; i++){
            for(int j=1; j<=n; j++){
                if(x.charAt(i-1) == y.charAt(j-1)){
                    matrix[i][j] = 1 + matrix[i-1][j-1];
                } else {
                    matrix[i][j] = Math.max(matrix[i][j-1], matrix[i-1][j]);
                }
            }
        }
        return matrix[m][n];
    }

    public static void main(String[] args){
        String x = "ABCBDAB";
        String y = "BDCABA";

        System.out.println("LCS length with recursive approach: " + lcs(x, y));
        System.out.println();

        System.out.println("LCS length with DP recursive approach: " + lcsDP(x, y));
        System.out.println();

        System.out.println("LCS length with DP iterative (bottom-up) approach: " + lcsDPIter(x, y));
        System.out.println();
    }
}
