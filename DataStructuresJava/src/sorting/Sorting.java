package sorting;

import java.util.Arrays;

public class Sorting {
    // Time Complexity: O(n**2)
    public static void insertionSort(Integer[] arr, Integer n){
        for(int i=1; i<n; i++){
            for(int j=i-1; j>=0; j--){
                if(arr[j+1] < arr[j]){
                    Integer temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }

    /*
        Private merge routine: merge two sorted arrays into a new array,
        copy the merged array back to the original array
    */
    private static void merge(Integer[] arr, Integer start, Integer mid, Integer end){
        Integer[] temp = new Integer[end-start+1];
        int i=start, j=mid+1, k=0;

        while(i<=mid && j<=end){
            if(arr[i] < arr[j])
                temp[k++] = arr[i++];
            else
                temp[k++] = arr[j++];
        }
        while(i<=mid)
            temp[k++] = arr[i++];
        while(j<=end)
            temp[k++] = arr[j++];

        // Copy the temp array back to the original array
        i=start; k=0;
        while(i<=end)
            arr[i++] = temp[k++];
    }

    public static void mergeSort(Integer[] arr, Integer start, Integer end){
        if(start >= end)
            return;
        Integer mid = (start+end)/2;
        mergeSort(arr, start, mid);                 // T(n/2)
        mergeSort(arr, mid+1, end);            // T(n/2)
        merge(arr, start, mid, end);                // O(n)
    }

    public static void main(String[] args){
        Integer[] arr = new Integer[]{30,12,51,21,5,1,5,55,60};
        System.out.println("Unsorted Array is: " + Arrays.toString(arr));

        insertionSort(arr, arr.length);
        System.out.println("Array after insertionSort is: " + Arrays.toString(arr));

        arr = new Integer[]{30,12,51,21,5,1,5,55,60};
        arr = Arrays.copyOf(arr, 3);
        System.out.println("Unsorted Array is: " + Arrays.toString(arr));
        mergeSort(arr, 0, arr.length-1);
        System.out.println("Array after mergeSort is: " + Arrays.toString(arr));
    }
}
