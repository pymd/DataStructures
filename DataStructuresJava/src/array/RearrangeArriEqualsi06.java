package array;

import java.util.Arrays;

public class RearrangeArriEqualsi06 {

    // T(n) = O(n*logn)
    public static void rearrange(Integer[] arr){
        Arrays.sort(arr);
        for(int i=0; i<arr.length; i++){
            if(arr[i] != -1){
                Integer temp1 = arr[i];
                Integer temp2 = arr[arr[i]];
                arr[temp1] = temp1;
                arr[i] = temp2;
            }
        }
        print(Arrays.toString(arr));
    }

    // O(n)
    public static void rearrange2(Integer[] arr){
        for(int i=0; i<arr.length; ){
            if(arr[i] >= 0 && arr[i] != i){
                int ele = arr[arr[i]];
                arr[arr[i]] = arr[i];
                arr[i] = ele;
            }else{
                i++;
            }
        }
        print(Arrays.toString(arr));
    }

    public static void print(String s){
        System.out.println(s);
    }

    public static void main(String[] args){
        Integer[] arr = new Integer[]{-1, -1, 6, 1, 9, 3, 2, -1, 4, -1};
        print("Original Array: " + Arrays.toString(arr));
        rearrange(arr);
        rearrange2(arr);
    }
}
