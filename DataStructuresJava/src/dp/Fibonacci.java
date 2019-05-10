package dp;

import java.util.*;

public class Fibonacci {
    private static List<Integer> fibs = new ArrayList<>();

    // Recursive solution - exponential
    private static Integer fibRecur(Integer n){
        if(n == 0)
            return 0;
        if(n == 1)
            return 1;
        return fibRecur(n-1)+fibRecur(n-2);
    }

    // Recursion with memoization (top-down DP) - O(n)
    private static Integer fib(Integer n){
        if(n == 0 || n == 1)
            return fibs.get(n);
        if(fibs.size() >= n+1)
            return fibs.get(n);
        fibs.add(n, fib(n-1) + fib(n-2));
        return fibs.get(n);
    }

    // Iterative with memoization (bottom-up DP) - O(n)
    private static Integer fibIter(Integer n){
        int[] f = new int[n+2];
        f[0] = 0;
        f[1] = 1;
        for(int i=2; i<=n; i++){
            f[i] = f[i-1] + f[i-2];
        }
        return f[n];
    }

    // Iterative with optimized space - O(n)
    private static Integer fibIterOp(Integer n){
        int first = 0;
        int second = 1;
        int current = 0;
        for(int i=2; i<=n; i++){
            current = first+second;
            first = second;
            second = current;
        }
        return current;
    }

    // Using Binet's Formula - O(1)
    private static Long fibFormula(Integer n){
        Double phi = (1+Math.sqrt(5))/2;
        return Math.round(Math.pow(phi, n)/Math.sqrt(5));
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Integer n = in.nextInt();
        System.out.println(n + "th fibonacci number with exponential recursion is:" + fibRecur(n));

        fibs.add(0);
        fibs.add(1);
        System.out.println(n + "th fibonacci number with Memoization is:" + fib(n));

        System.out.println(n + "th fibonacci number with Iterative Solution is:" + fibIter(n));

        System.out.println(n + "th fibonacci number with Iterative Mem Optimized Solution is:" + fibIterOp(n));

        System.out.println(n + "th fibonacci number with Formula is:" + fibFormula(n));
    }
}
