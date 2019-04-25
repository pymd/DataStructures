package array;

import java.util.Arrays;

public class TestClass {

    public static void print(String s){
        System.out.println(s);
    }

    public static void main(String[] args){
        Integer[] arr = new Integer[]{10, 2, 123, 1, 40, 41, 34, 39};
        Integer[] largerArr = new Integer[arr.length+10];
        print("Original array is: " + Arrays.toString(arr));

        // Array slicing
        Integer[] slicedArray = Arrays.copyOfRange(arr, 2, 5);
        print("Sliced array is: " + Arrays.toString(slicedArray));

        // Array slicing "from start"
        slicedArray = Arrays.copyOf(arr, 4);
        print("Sliced array from start is: " + Arrays.toString(slicedArray));

        // Copy smaller array into larger one
        System.arraycopy(arr, 0, largerArr, 0, arr.length);
        print("Larger array is: " + Arrays.toString(largerArr));
        print("Larger array length is: " + largerArr.length);
    }
}
