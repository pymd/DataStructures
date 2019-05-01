package array;

public class MaxSumIniAi05 {

    public static void print(String s){
        System.out.println(s);
    }

    public static void main(String[] args){
        Integer[] arr = new Integer[]{3, 2, 1};
        Integer s = 0;
        Integer sumOfDigits = 0;
        Integer maxSum = 0;
        // O(n)
        for(int i=0; i<arr.length; i++){
            s += i*arr[i];
            sumOfDigits += arr[i];
        }
        print("s = " + s);
        print("sumOfdigits = " + sumOfDigits);
        maxSum = s;

        // O(n)
        for(int i=0; i<arr.length; i++){
            s = s - sumOfDigits + (arr[i]*(arr.length));
            print("New S = " + s);
            if(maxSum < s)
                maxSum = s;
        }

        print("Max Sum is: " + maxSum);
    }
}
