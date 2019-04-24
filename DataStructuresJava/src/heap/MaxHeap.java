package heap;

import java.util.Arrays;

public class MaxHeap {
    private Integer n;
    private Integer[] arr;

    public MaxHeap(Integer n){
        this.n = n;
        arr = new Integer[this.n];
    }

    public void setArr(Integer[] arr){
        this.arr = arr;
        this.n = arr.length;
    }

    public Integer[] getArr(){
        return arr;
    }

    public Integer getN(){
        return n;
    }

    public void setN(Integer n){
        this.n = n;
    }

    // T(n): O(n)
    public void buildMaxHeap(){
        for(int i=n/2; i>=0; i--){
            heapify(i);
        }
    }

    // T(n): O(log n)
    public void heapify(Integer i){
        if(i >= n/2)
            return;

        Integer left = 2*i+1;
        Integer right = 2*i+2;
        Integer largest = i;

        if(left<n && arr[i]<arr[left])
            largest = left;
        if(right<n && arr[largest]<arr[right])
            largest = right;

        if(largest.equals(i))
            return;

        // swap i with largest child
        Integer temp = arr[largest];
        arr[largest] = arr[i];
        arr[i] = temp;

        // recurse on child
        heapify(largest);
    }

    // O(1)
    public Integer getMax(){
        return arr[0];
    }

    // O(log n)
    public Integer extractMax(){
        Integer m = arr[0];
        arr[0] = arr[n-1];
        setN(n-1);
        heapify(0);                 // O(log n)
        return m;
    }

    public void printHeap(){
        System.out.print("The heap is: ");
        for(int i=0; i<n; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String[] args){
        Integer n = 10;
        MaxHeap heap = new MaxHeap(n);
        heap.setArr(new Integer[]{30,12,51,21,5,1,5,55,60});

        heap.printHeap();
        heap.buildMaxHeap();
        heap.printHeap();

        System.out.println("Max value is: " + heap.extractMax());
        System.out.println("Max value is: " + heap.extractMax());
        heap.printHeap();
    }
}
