package graph;
import java.util.LinkedList;
import java.util.List;

public class Graph01 {
    private int V;          // number of vertices
    private List<Integer> adjListArray[];

    public int getV(){
        return V;
    }

    public List<Integer>[] getAdjListArray(){
        return adjListArray;
    }

    // constructor
    public Graph01(int V){
        this.V = V;

        // Array of Vertices
        adjListArray = new LinkedList[V];

        // create new list for each vertex
        for(int i=0; i<V; i++){
            adjListArray[i] = new LinkedList<Integer>();
        }
    }

    // Add An Edge In an Undirected Graph01
    public void addEdge(int src, int dest){
        adjListArray[src].add(dest);
        adjListArray[dest].add(src);
    }


    // Remove an edge from an undirected graph
    public void removeEdge(int src, int dest){
        adjListArray[src].remove(dest);
        adjListArray[dest].remove(src);
    }

    public static void printGraph(Graph01 graph01){
        for(int i = 0; i< graph01.getV(); i++){
            System.out.println("Adjaceny List for vertex " + i + " is: ");
            List<Integer> list = graph01.getAdjListArray()[i];
            for(Integer j: list){
                System.out.print(j + "->");
            }
            System.out.println("NULL");
        }
        System.out.println();
    }

    public static void main(String[] args){
        int V = 5;
        Graph01 graph01 = new Graph01(V);
        graph01.addEdge(0, 1);
        graph01.addEdge(0, 4);
        graph01.addEdge(1, 2);
        graph01.addEdge(1, 3);
        graph01.addEdge(1, 4);
        graph01.addEdge(2, 3);
        graph01.addEdge(3, 4);

        Graph01.printGraph(graph01);
    }
}
