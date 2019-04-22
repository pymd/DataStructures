package search;

import java.util.Arrays;

public class BinarySearch01 {
    /*
    A recursive implementation of a Binary Search Algorithm
    on an Array.
     */
    public static Integer recursiveBinarySearch(Integer[] arr, Integer start, Integer end, Integer s){
        Integer mid = (start+end)/2;
        if (arr[mid].equals(s))
            return mid;
        if(start >= end)
            return -1;
        if(arr[mid] < s)                // search in right subarray
            return recursiveBinarySearch(arr, mid+1, end, s);
        else                            // search in left subarray
            return recursiveBinarySearch(arr, start, mid-1, s);
    }


    /*
    An interative implementation of Binary Search Algorithm
    on an Array
     */
    public static Integer iterativeBinarySearch(Integer[] arr, Integer start, Integer end, Integer s){
        Integer startIndex = start;
        Integer endIndex = end;
        Integer mid = (startIndex+endIndex)/2;
        while(startIndex <= endIndex){
            if(arr[mid].equals(s))
                return mid;
            if(arr[mid] < s)             // search in right subarray
                startIndex = mid+1;
            else
                endIndex = mid-1;        // search in left subarray
        }
        return -1;
    }

    public static void main(String[] args){
        Integer[] arr = new Integer[]{10,15,12,11,5,1,2};
        Integer s = 5;
        Integer n = arr.length;

        Arrays.sort(arr);

        System.out.println("Length of array is: " + n);
        System.out.println("Sorted array is: ");
        for(int i=0; i<n; i++)
            System.out.print(arr[i] + " ");
        System.out.println();

        Integer index = recursiveBinarySearch(arr, 0, n-1, s);
        if(index == -1)
            System.out.println("Element " + s + " not found in array.");
        else
            System.out.println("Element " + s + " found at index " + index);

        System.out.println("Performing Iterative BinarySearch ...");
        Integer index2 = recursiveBinarySearch(arr, 0, n-1, s);
        if(index2 == -1)
            System.out.println("Element " + s + " not found in array.");
        else
            System.out.println("Element " + s + " found at index " + index2);
    }
}
