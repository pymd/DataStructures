package array;

import java.util.Arrays;

public class MedianOfTwoSortedArrays02 {

    // Time Complexity - O(N)
    public static Integer getMedianInEfficient(Integer[] arr1, Integer[] arr2, Integer n){
        int i=0, j=0, ctr=0, med1=0, med2=0;
        while(i<n && j<n){
            if(arr1[i] <= arr2[j])
                i++;
            else
                j++;
            ctr++;
            if(ctr == n-1)
                break;
        }
        med1 = arr1[i] <= arr2[j] ? arr1[i++] : arr2[j++];
        med2 = arr1[i] <= arr2[j] ? arr1[i++] : arr2[j++];
        return (med1+med2)/2;
    }

    private static Integer median(Integer[] arr, Integer n){
//        System.out.println(Arrays.toString(arr));
        Integer med;
        if(n % 2 == 1){
            med = arr[(n-1)/2];
        } else {
            // These need to be double
            med = (arr[(n-1)/2] + arr[n/2])/2;
        }
        return med;
    }

    // Time Complexity - O(logN), Space - O(logN)
    public static Integer getMedian(Integer[] arr1, Integer[] arr2, Integer n){

        if(n == 2){
            Integer med1 = Math.min(arr1[1], arr2[1]);
            Integer med2 = Math.max(arr1[0], arr2[0]);
//            System.out.println(Arrays.toString(arr1));
//            System.out.println(Arrays.toString(arr2));
//            System.out.println("Med1 = "+med1 + " Med2 = " + med2);
            return (med1+med2)/2;
        }

        Integer med1 = median(arr1, n);
        Integer med2 = median(arr2, n);
//        System.out.println("Med1 = "+med1 + " Med2 = " + med2);

        if(med1.equals(med2)){
            return med1;
        } else if(med1 < med2){
            if(n % 2 == 0)
                return getMedian(Arrays.copyOfRange(arr1, n/2-1, n), Arrays.copyOfRange(arr2, 0, (n/2)+1), n-(n/2)+1);
            return getMedian(Arrays.copyOfRange(arr1, (n-1)/2, n), Arrays.copyOfRange(arr2, 0, (n/2)+1), (n/2)+1);
        } else {
            if(n % 2 == 0)
                return getMedian(Arrays.copyOfRange(arr1, 0, (n/2)+1), Arrays.copyOfRange(arr2, (n/2)-1, n), n-(n/2)+1);
            return getMedian(Arrays.copyOfRange(arr1, 0, (n/2)+1), Arrays.copyOfRange(arr2, (n-1)/2, n), (n/2)+1);
        }
    }

    public static void main(String[] args){
        Integer[] arr1 = new Integer[]{10,15,12,11,5,1,2,20};
        Integer[] arr2 = new Integer[]{20,25,32,16,4,13,3,21};
        Integer n = arr1.length;

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        System.out.println("Array1 is: " + Arrays.toString(arr1));
        System.out.println("Array2 is: " + Arrays.toString(arr2));

        Integer s = getMedianInEfficient(arr1, arr2, n);
        System.out.println("Median of the two arrays using inEfficient Method is: " + s);

        Integer s2 = getMedian(arr1, arr2, n);
        System.out.println("Median of the two arrays using efficient Method is: " + s2);
    }
}
