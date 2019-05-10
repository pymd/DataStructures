package heap;

import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

import java.util.Arrays;

public class MaxHeap {
    private Integer heapSize;
    private Integer capacity;
    private Integer[] arr;

    // Constructor
    public MaxHeap(Integer capacity){
        this.capacity = capacity;
        arr = new Integer[this.capacity];
    }

    // Getters and Setters
    public Integer getHeapSize(){
        return heapSize;
    }

    public void setHeapSize(Integer heapSize){
        this.heapSize = heapSize;
    }

    public Integer getCapacity(){
        return capacity;
    }

    public void setCapacity(Integer capacity){
        this.capacity = capacity;
    }

    public void setArr(Integer[] arr){
        System.arraycopy(arr, 0, this.arr, 0, arr.length);
        this.heapSize = arr.length;
    }

    public Integer[] getArr(){
        return arr;
    }

    // Helper Methods
    private Integer parent(Integer i){
        return (i-1)/2;
    }

    private Integer leftChild(Integer i){
        return 2*i+1;
    }

    private Integer rightChild(Integer i){
        return 2*i+2;
    }

    // Heap Operations

    // T(n): O(n)
    /*
        Convert any given array to heap
     */
    public void buildMaxHeap(){
        for(int i=heapSize/2; i>=0; i--){
            heapify(i);
        }
    }

    // T(n): O(log n)
    /*
        Assume only 1 correction needed at index i; Recurse downwards
     */
    public void heapify(Integer i){
        if(i >= heapSize/2)
            return;

        Integer left = leftChild(i);
        Integer right = rightChild(i);
        Integer largest = i;

        if(left<heapSize && arr[i]<arr[left])
            largest = left;
        if(right<heapSize && arr[largest]<arr[right])
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
    /*
        Reduce Heap Size by 1
        Replace first array element by last
     */
    public Integer extractMax(){
        if(heapSize.equals(0))
            return null;
        if(heapSize.equals(1)){
            setHeapSize(heapSize-1);
            return arr[0];
        }
        Integer maxVal = arr[0];
        arr[0] = arr[heapSize-1];
        setHeapSize(heapSize-1);
        heapify(0);                     // O(log n)
        return maxVal;
    }

    // O(log n)
    /*
        Insert at last position,
        Move up and fix heap property
     */
    public void insertKey(Integer k){
        if(heapSize.equals(capacity)){
            System.out.println("Heap Overflow!!!");
            return;
        }
        setHeapSize(heapSize+1);
        arr[heapSize-1] = k;
        Integer i = heapSize-1;
        while(i > 0 && arr[parent(i)] < arr[i]){
            // swap parent and i
            Integer temp = arr[parent(i)];
            arr[parent(i)] = arr[i];
            arr[i] = temp;
            // update i
            i = parent(i);
        }
    }

    // O(log n)
    // Assumption: newVal is smaller than arr[index] => Move Down
    public void decreaseKey(Integer index, Integer newVal){
        if(heapSize < index+1){
            System.out.println("Error! Index " + index + " does not exist in heap");
            return;
        }
        arr[index] = newVal;
        heapify(index);
    }

    // O(log n)
    // Assumption: newVal is greater than arr[index] => Move Up
    public void increaseKey(Integer index, Integer newVal){
        if(heapSize < index+1){
            System.out.println("Error! Index " + index + " does not exist in heap");
            return;
        }
        arr[index] = newVal;
        Integer i = index;
        while(i > 0 && arr[parent(i)] < arr[i]){
            // swap i and parent(i)
            Integer temp = arr[i];
            arr[i] = arr[parent(i)];
            arr[parent(i)] = arr[i];

            // update i
            i = parent(i);
        }
    }

    // O(log n)
    // Delete the value at index i
    public void deleteKey(Integer index){
        if(heapSize < index+1){
            System.out.println("Error! Index " + index + " does not exist in heap");
            return;
        }
        System.out.println("Deleting key at index: " + index);
        increaseKey(index, Integer.MAX_VALUE);          // O(log n)
        extractMax();                                   // O(log n)
    }

    public void printHeap(){
        if(heapSize.equals(0)) {
            System.out.println("Heap is Empty!!!");
            return;
        }
        System.out.print("The heap is: ");
        for(int i=0; i<heapSize; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void print(String s){
        System.out.println(s);
    }

    public static void main(String[] args){
        Integer n = 12;
        MaxHeap heap = new MaxHeap(n);
        heap.setArr(new Integer[]{30,12,51,21,5,1,5,55,60});

        heap.printHeap();
        heap.buildMaxHeap();
        heap.printHeap();

        System.out.println("Max value is: " + heap.extractMax());
        System.out.println("Max value is: " + heap.extractMax());
        heap.printHeap();

        heap.insertKey(60);
//        print("Size of heap is: " + heap.getHeapSize());
        heap.insertKey(55);
//        print("Size of heap is: " + heap.getHeapSize());
//        print("Capacity of heap is: " + heap.getCapacity());
        heap.printHeap();

        heap.deleteKey(2);
//        print("Size of heap is: " + heap.getHeapSize());
//        print("Capacity of heap is: " + heap.getCapacity());
        heap.printHeap();

        heap.deleteKey(20);
//        print("Size of heap is: " + heap.getHeapSize());

        heap.insertKey(40);
        heap.insertKey(20);
        heap.insertKey(70);
        heap.insertKey(80);
        heap.printHeap();
        heap.insertKey(11);
        heap.printHeap();
    }
}
