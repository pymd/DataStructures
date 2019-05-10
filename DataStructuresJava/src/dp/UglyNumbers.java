package dp;

import java.util.*;

public class UglyNumbers {
    public static int findNthUglyNumber(int n) {
        int i=0,j=0,k=0;
        List<Integer> l = new ArrayList<Integer>();
        l.add(1);
        int count = 1;
        while(true){
            int minimum = Math.min(Math.min(l.get(i)*2, l.get(j)*3), l.get(k)*5);
            if(minimum == l.get(i)*2)
                i++;
            if(minimum == l.get(j)*3)
                j++;
            if(minimum == l.get(k)*5)
                k++;
//            if(l.contains(minimum))
//                continue;
            l.add(minimum);
            count++;
            if(count >= n)
                break;
        }
        System.out.println(Arrays.toString(l.toArray()));
        return l.get(l.size()-1);
    }

    public static void main(String[] args) {
        int n = 150;
        int ans = findNthUglyNumber(n);
        System.out.println(n + "th Ugly number is: " + ans);
    }
}
