package search;

import java.util.Arrays;

public class FindPeak03 {

    // A Binary Search inspired O(logN) solution
    public static Integer findPeak(Integer[] arr, Integer start, Integer end){
        Integer mid = (start+end)/2 ;
        if(start > end)
            return -1;
        if(start.equals(end))
            return start;
        if(end-start == 1){
            if(arr[end] >= arr[start])
                return arr[end];
            else
                return arr[start];
        }
        if(arr[mid] >= arr[mid-1] && arr[mid] >= arr[mid+1])
            return mid;
        if(arr[mid] < arr[mid+1])
            return findPeak(arr, mid+1, end);
        else
            return findPeak(arr, start, mid-1);
    }

    public static void main(String[] args){
        Integer[] arr = new Integer[]{5,10,14};
        Integer n = arr.length;
        System.out.println("Length of array is: " + n);
        System.out.println("The array is: " + Arrays.toString(arr));

        Integer peak = findPeak(arr, 0, n-1);
        System.out.println("Peak in array is at index: " + peak);
    }
}
