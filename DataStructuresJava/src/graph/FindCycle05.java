package graph;

import graph.Vertex;
import java.util.List;
import java.util.LinkedList;

public class FindCycle05 {
    private Integer V;
    private List<Integer> adjListArray[];
    private Vertex vertices[];

    public FindCycle05(int V){
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

    public static void printGraph(FindCycle05 graph){
        for(int i=0; i<graph.V; i++){
            System.out.println("AdjList for vertex " + i + " is: ");
            for(Integer j: graph.adjListArray[i]){
                System.out.print(j + "->");
            }
            System.out.println("NULL");
        }
        System.out.println();
    }

    private boolean process_edge(int x, int y){
        if(vertices[x].getParent() != y){
            System.out.println("Found cycle from " + x + " to " + y);
            return true;
        }
        return false;
    }

    public boolean findCycles(int src){
        boolean subGraphhasCycle = false;
        boolean hasCycle = false;
        Integer x = src;
        vertices[x].setDiscovered(true);
        for(Integer y: adjListArray[x]){
            if(!vertices[y].isDiscovered()){
                vertices[y].setDiscovered(true);
                vertices[y].setParent(x);
                subGraphhasCycle = subGraphhasCycle || findCycles(y);
            }
            if(!vertices[y].isProcessed()){
                hasCycle = hasCycle || process_edge(x,y);
            }
        }
        vertices[x].setProcessed(true);
        return (hasCycle || subGraphhasCycle);
    }

    public static void main(String[] args){
        int V = 5;
        FindCycle05 graph = new FindCycle05(V);

        graph.addEdge(0, 1);
        graph.addEdge(0, 4);
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 3);
        graph.addEdge(3, 4);

        printGraph(graph);

        System.out.println("Does the graph has cycles?: " + graph.findCycles(0));
    }
}
