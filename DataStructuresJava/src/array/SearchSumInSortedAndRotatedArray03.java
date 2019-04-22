package array;

import java.util.Arrays;

public class SearchSumInSortedAndRotatedArray03 {
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

    private static Integer findRotationPoint(Integer[] arr, Integer start, Integer end){
        Integer mid = (start+end)/2;
        if(start.equals(end) || arr[start] < arr[end])
            return -1;
        if(arr[mid] > arr[mid+1])
            return mid;
        if(arr[start] > arr[mid])
            return findRotationPoint(arr, start, mid-1);
        else
            return findRotationPoint(arr, mid, end);
    }

    public static void printPairsWithSum(Integer[] arr, Integer n, Integer s){
        int start=0, end=n-1;

        int rotPoint = findRotationPoint(arr, 0, n-1);
        if(rotPoint == -1){
            start = 0;
            end = n-1;
        } else {
            start = rotPoint+1;
            end = rotPoint;
        }

        while(start != end){
            if(arr[start] + arr[end] == s){
                System.out.println(arr[start] + ", " + arr[end]);
                start++;
            } else if(arr[start] + arr[end] < s){
                start++;
            } else{
                end--;
            }
            if(end < 0)
                end = n-1;
            if(start > n-1)
                start = 0;
        }
    }

    public static void main(String[] args){
        Integer[] arr = new Integer[]{10,15,12,11,5,1,2};
        Integer r = 5;
        Integer n = arr.length;

        Arrays.sort(arr);

        System.out.println("Length of array is: " + n);
        System.out.println("Sorted array is: " + Arrays.toString(arr));

        rotateInEfficient(arr, n, r);
        System.out.println("Rotated Sorted array is: " + Arrays.toString(arr));

        int s = 16;
        printPairsWithSum(arr, n, s);
    }
}
