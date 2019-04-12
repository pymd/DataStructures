package graph;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Vertex{
    private boolean discovered;
    private boolean processed;
    private int val;
    private int parent;

    public Vertex(int v){
        discovered = false;
        processed = false;
        this.val = v;
    }

    public boolean isProcessed() {
        return processed;
    }

    public void setProcessed(boolean processed) {
        this.processed = processed;
    }

    public boolean isDiscovered() {
        return discovered;
    }

    public void setDiscovered(boolean discovered) {
        this.discovered = discovered;
    }

    public int getVal() {
        return val;
    }

    public void setVal(int val) {
        this.val = val;
    }

    public Integer getParent() {
        return parent;
    }

    public void setParent(Integer parent) {
        this.parent = parent;
    }
}

public class DFS04 {
    private Vertex vertices[];
    private int V;
    private List<Integer> adjListArray[];

    public DFS04(int V){
        this.V = V;

        adjListArray = new LinkedList[V];
        vertices = new Vertex[V];

        for(int i=0; i<V; i++){
            adjListArray[i] = new LinkedList<Integer>();
            vertices[i] = new Vertex(i);
        }
    }

    public void addEdge(int src, int dest){
        adjListArray[src].add(dest);
        adjListArray[dest].add(src);
    }

    public static void printGraph(DFS04 graph){
        for(int i=0; i<graph.V; i++){
            System.out.println("Adj List for vertex " + i + " is:");
            for(Integer j: graph.adjListArray[i]){
                System.out.print(j + "->");
            }
            System.out.println("NULL");
        }
        System.out.println();
    }

    // dfs only for connected components
    public void dfs(int src){
        Integer x = src;

        System.out.print(x + "->");
        vertices[x].setDiscovered(true);
        // process vertex early
        for(Integer y: adjListArray[x]){
            if(!vertices[y].isDiscovered()){
                vertices[y].setDiscovered(true);
                // process edge
                dfs(y);
            }
        }
        // process vertex late
        vertices[x].setProcessed(true);
    }

    public static void main(String[] args){
        int V = 5;
        DFS04 graph = new DFS04(V);

        graph.addEdge(0, 1);
        graph.addEdge(0, 4);
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 3);
        graph.addEdge(3, 4);

        printGraph(graph);

        graph.dfs(0);
    }
}
