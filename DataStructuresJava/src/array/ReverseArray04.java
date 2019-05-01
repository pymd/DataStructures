package array;

import java.util.Arrays;

public class ReverseArray04 {
    public static void reverse(Integer[] arr, int start, int end){
        if(start >= end)
            return;
        Integer temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        reverse(arr, start+1, end-1);
    }

    public static void reverseIterative(Integer[] arr, int start, int end){
        while(start < end){
            Integer temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }

    public static void print(String s){
        System.out.println(s);
    }

    public static void main(String[] args){
        Integer[] arr = new Integer[]{1,2,3,4,5,6,7,8};
        print(Arrays.toString(arr));
        reverse(arr, 0, arr.length-1);
        print(Arrays.toString(arr));
        reverseIterative(arr, 0, arr.length-1);
        print(Arrays.toString(arr));
    }
}
