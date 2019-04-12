package graph;

import java.util.List;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Map;
import java.util.HashMap;

public class BFS02 {
    private int V;
    private List<Integer> adjListArray[];

    public BFS02(int V){
        this.V = V;

        adjListArray = new LinkedList[V];

        for(int i=0; i<V; i++){
            adjListArray[i] = new LinkedList<Integer>();
        }

        // Todo: Remove this. Test code for interview
        Map <String, String> m = new HashMap<String, String>();
        m.put("a", "b");
        String s = m.get("a");
    }

    public void addEdge(int src, int dest){
        adjListArray[src].add(dest);
        adjListArray[dest].add(src);
    }

    public static void printGraph(BFS02 graph){
        for(int i=0; i<graph.V; i++){
            List<Integer> adjList = graph.adjListArray[i];
            System.out.println("Adj List of Vertex " + i + " is:");
            for(Integer j: adjList){
                System.out.print(j + "->");
            }
            System.out.println("NULL");
        }
    }

    // BFS02 for connected graphs
    public void getBFS(BFS02 graph, int src){
        boolean discovered[] = new boolean[graph.V];
        boolean processed[] = new boolean[graph.V];
        Queue<Integer> q = new LinkedList<Integer>();

        System.out.println("BFS02 of tree is:");

        // initialization
        for(int i=0; i<graph.V; i++){
            discovered[i] = false;
            processed[i] = false;
        }
        discovered[src] = true;
        q.add(src);

        System.out.print(src + " ");
        while(!q.isEmpty()){
            Integer current = q.poll();
            // process vertex early
            List<Integer> neighbors = graph.adjListArray[current];
            for(Integer neighbor: neighbors){
                if(!discovered[neighbor]){
                    System.out.print(neighbor + " ");
                    discovered[neighbor] = true;
                    q.add(neighbor);
                    // process edge
                }
            }
            // process vertex late
            processed[current] = true;
        }
        System.out.println();
    }

    public static void main(String[] args){
        BFS02 graph = new BFS02(4);

        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(1, 2);
        graph.addEdge(2, 0);
        graph.addEdge(2, 3);
        graph.addEdge(3, 3);

        BFS02.printGraph(graph);
        graph.getBFS(graph, 2);
    }
}
