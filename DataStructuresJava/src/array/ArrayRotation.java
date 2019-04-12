package array;

public class ArrayRotation {
    private int[] arr;

    public ArrayRotation(int[] arr){
        this.arr = arr;
    }

    public void printArray(){
        System.out.println("Array is:");
        for(int i=0; i<arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    // Todo: Imp - Euclid's Algorithm to Find GCD of 2 numbers
    private int hcf(int a, int b){
        if(b == 0)
            return a;
        else
            return hcf(b, a%b);
    }

    // Todo: Not working
    public void jugglingAlgorithm(int[] a, int d, int n){
        int gcd = hcf(n,d);
        for(int i=0; i<gcd; i++){
            System.out.println("Runing for i="+i);
            int beginIndex = i;
            int temp = a[beginIndex];
            int currentIndex = beginIndex;
            while(true){
                int nextIndex = (currentIndex+d) % n;
                if(nextIndex == beginIndex){
                    a[nextIndex] = temp;
                    break;
                }
                a[currentIndex] = a[nextIndex];
                currentIndex = nextIndex;
            }
        }
    }

    public static void main(String[] args){
        int d = 3;
        int[] arr = new int[]{1,2,3,4,5,6,7,8};

        ArrayRotation arrObj = new ArrayRotation(arr);
        arrObj.printArray();
        arrObj.jugglingAlgorithm(arr, d, arr.length);
        arrObj.printArray();
    }
}
