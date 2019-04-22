package search;

import java.util.Arrays;

public class SearchInSortedAndRotatedArray02 {

    // InEfficient rotate Function - uses extra space
    public static void rotateUsingExtraSpace(Integer[] arr, Integer n, Integer d){
        Integer[] temp = Arrays.copyOf(arr, d);
        System.out.println("Length of temp array is: " + temp.length);
        for(int i=0; i<n-d; i++){
            arr[i] = arr[i+d];
        }
        for(int i=n-d; i<n; i++)
            arr[i] = temp[i+d-n];
    }

    // InEfficient rotate function - time complexity O(n*d)
    public static void rotateInEfficient(Integer[] arr, Integer n, Integer d){
        for(int i=0; i<d; i++){             // Repeat `d` times
            Integer temp = arr[0];
            for(int j=0; j<n-1; j++){
                arr[j] = arr[j+1];
            }
            arr[n-1] = temp;
        }
    }

    // Todo: Implement Juggling Algorithm
    public static void rotateEfficient(Integer[] arr, Integer n, Integer d){

    }

    // Private Helper Method
    private static Integer findRotationPoint(Integer[] arr, Integer start, Integer end){
        if(start>end)
            return -1;
        if(start.equals(end))
            return start;
        Integer mid = (start+end)/2;
        if(mid < end && arr[mid] > arr[mid+1])
            return mid;
        if(mid > start && arr[mid] < arr[mid-1])
            return mid-1;
        if(arr[start] >= arr[mid])
            return findRotationPoint(arr, start, mid-1);
        return findRotationPoint(arr, mid+1, end);
    }

    // Private Helper Method
    private static Integer binarySearch(Integer[] arr, Integer start, Integer end, Integer k){
        Integer mid = (start+end)/2;
        if(start > end) {
            return -1;
        } else{
            if(arr[mid].equals(k)) {
                return mid;
            } else if(arr[mid] > k){
                return binarySearch(arr, start, mid-1, k);
            } else {
                return binarySearch(arr, mid+1, end, k);
            }
        }
    }

    public static Integer binarySearchModified(Integer[] arr, Integer start, Integer end, Integer k){
        Integer mid = (start+end)/2;
        // find rotation point by binarySearch
        Integer rotationPoint = findRotationPoint(arr, start, end);
        System.out.println("Rotation Point = " + rotationPoint);
        // search in the appropriate part of the array
        if(rotationPoint == -1)
            return binarySearch(arr, start, end, k);
        if(arr[rotationPoint] >= k)
            return binarySearch(arr, start, rotationPoint, k);
        else
            return binarySearch(arr, rotationPoint+1, end, k);
    }

    // MOST EFFICIENT ALGORITHM - Only 1 pass of binary Search needed
    public static Integer binarySearchModifiedEfficient(Integer[] arr, Integer start, Integer end, Integer k){
        if(start>end)
            return -1;
        Integer mid = (start+end)/2;
        if(arr[mid].equals(k))
            return mid;
        if(arr[mid] > arr[start]){
            // first array is sorted
            if(arr[start] < k && arr[mid] > k){
                // recurse on first half
                return binarySearchModifiedEfficient(arr, start, mid-1, k);
            } else {
                // recurse on second half
                return binarySearchModifiedEfficient(arr, mid+1, end, k);
            }
        } else {
            // second array is sorted
            if(arr[mid] < k && arr[end] > k){
                // recurse on second half
                return binarySearchModifiedEfficient(arr, mid+1, end, k);
            } else {
                // recurse on first half
                return binarySearchModifiedEfficient(arr, start, mid-1, k);
            }
        }
    }

    public static void main(String[] args){
        Integer[] arr = new Integer[]{10,15,12,11,5,1,2};
        Integer s = 5;
        Integer n = arr.length;

        Arrays.sort(arr);

        System.out.println("Length of array is: " + n);
        System.out.println("Sorted array is: " + Arrays.toString(arr));

        // rotateUsingExtraSpace(arr, n, 3);
        rotateInEfficient(arr, n, 2);
        System.out.println("Rotated Sorted array is: " + Arrays.toString(arr));

        Integer k = 15;
        Integer index = binarySearchModified(arr, 0, n-1, k);

        if(index == -1)
            System.out.println("Element " + k + " not found in array.");
        else
            System.out.println("Element " + k + " found at index: " + index);

        Integer index2 = binarySearchModified(arr, 0, n-1, k);

        if(index2 == -1)
            System.out.println("Element " + k + " not found in array.");
        else
            System.out.println("Element " + k + " found at index: " + index2);
    }
}
