package array;

import java.util.Arrays;

public class TestClass {
    public static void main(String[] args){
        Integer[] arr = new Integer[]{10, 2, 123, 1, 40, 41, 34, 39};
        System.out.println("Original array is: " + Arrays.toString(arr));

        // Array slicing
        Integer[] slicedArray = Arrays.copyOfRange(arr, 2, 5);
        System.out.println("Sliced array is: " + Arrays.toString(slicedArray));

        // Array slicing "from start"
        slicedArray = Arrays.copyOf(arr, 4);
        System.out.println("Sliced array from start is: " + Arrays.toString(slicedArray));
    }
}
