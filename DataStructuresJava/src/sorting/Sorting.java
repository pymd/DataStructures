package sorting;

import java.lang.reflect.Array;
import java.util.Arrays;
import heap.MaxHeap;

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

    // O(nlogn)
    public static void mergeSort(Integer[] arr, Integer start, Integer end){
        if(start >= end)
            return;
        Integer mid = (start+end)/2;
        mergeSort(arr, start, mid);                 // T(n/2)
        mergeSort(arr, mid+1, end);            // T(n/2)
        merge(arr, start, mid, end);                // O(n)
    }

    // O(nlogn)
    public static void heapSort(Integer[] arr, Integer n){
        MaxHeap heap = new MaxHeap(n);
        heap.setArr(arr);
        Integer[] heapArr = heap.getArr();

        // O(n)
        heap.buildMaxHeap();

        // O(nlogn)
        for(int i=0; i<arr.length; i++){
            Integer temp = heapArr[n-1];
            heapArr[n-1] = heapArr[0];
            heapArr[0] = temp;

            heap.setHeapSize(--n);
            heap.heapify(0);            // O(logn)
        }
    }

    // O(n+k) : sorts number between range 0 to k-1
    public static void countingSort(Integer[] arr, Integer k){
        int n = arr.length;

        int[] output = new int[n];

        // define count array                   O(k)
        int count[] = new int[k];
        for(int i=0; i<k; i++)
            count[i] = 0;

        // set counts                           O(n)
        for(int i=0; i<n; i++)
            count[arr[i]]++;

        // modify count array to contain sum of previous counts         O(k)
        for(int i=1; i<k; i++){
            count[i] = count[i]+count[i-1];
        }

        // set output                           O(n)
        for(int i=0; i<n; i++){
            output[count[arr[i]]-1] = arr[i];
            count[arr[i]]--;
        }

        // O(n)
        for(int i=0; i<n; i++)
            arr[i] = output[i];
    }

    public static void main(String[] args){
        Integer[] arr = new Integer[]{30,12,51,21,5,1,5,55,60};
        System.out.println("Unsorted Array is: " + Arrays.toString(arr));

        insertionSort(arr, arr.length);
        System.out.println("Array after insertionSort is: " + Arrays.toString(arr));

        arr = new Integer[]{30,12,51,21,5,1,5,55,60};
        System.out.println("Unsorted Array is: " + Arrays.toString(arr));
        mergeSort(arr, 0, arr.length-1);
        System.out.println("Array after mergeSort is: " + Arrays.toString(arr));

        arr = new Integer[]{30,12,51,21,5,1,5,55,60};
        System.out.println("Unsorted Array is: " + Arrays.toString(arr));
        heapSort(arr, arr.length);
        System.out.println("Array after heapSort is: " + Arrays.toString(arr));

        arr = new Integer[]{30,12,51,21,5,1,5,55,60};
        System.out.println("Unsorted Array is: " + Arrays.toString(arr));
        countingSort(arr, 61);
        System.out.println("Array after countingSort is: " + Arrays.toString(arr));
    }
}
