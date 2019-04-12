package graph;

import java.util.List;
import java.util.LinkedList;
import java.util.Queue;

public class TwoColoringProblem03 {
    private Integer V;
    private List<Integer> adjListArray[];
    private Integer color[];
    private boolean bipartite;

    public TwoColoringProblem03(int V){
        this.V = V;
        adjListArray = new LinkedList[V];
        color = new Integer[V];
        bipartite = true;

        for(int i=0; i<V; i++){
            adjListArray[i] = new LinkedList<Integer>();
            color[i] = 0;
        }
    }

    public void addEdge(int src, int dest){
        adjListArray[src].add(dest);
        adjListArray[dest].add(src);
    }

    public static void printGraph(TwoColoringProblem03 graph){
        System.out.println("Graph01 is:");
        for(int i=0; i<graph.V; i++){
            System.out.print("AdjList for vertex " + i + " :");
            List<Integer> list = graph.adjListArray[i];
            for(Integer j: list){
                System.out.print(j + "->");
            }
            System.out.println("NULL");
        }
    }

    public static Integer complement(int color){
        if(color == 1) return 2;
        if(color == 2) return 1;
        return 0;
    }

    public void process_edge(int src, int dest){
        color[dest] = complement(color[src]);
    }

    // BFS02 only for connected components from src
    public static void bfs(TwoColoringProblem03 graph, int src, boolean discovered[], boolean processed[]){
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(src);
        while(!queue.isEmpty()){
            Integer x = queue.poll();
            // process vertex early
            for(Integer y: graph.adjListArray[x]){
                if(!discovered[y]){
                    queue.add(y);
                    discovered[y] = true;
                    graph.process_edge(x, y);
                }
                if(graph.color[x].equals(graph.color[y])) {
                    System.out.println("Graph01 is not bipartite because of " + x + " and " + y);
                    graph.bipartite = false;
                }
            }
            // process vertex late
            processed[x] = true;
        }
    }

    public void isBipartite(){
        // initialization
        boolean discovered[] = new boolean[V];
        boolean processed[] = new boolean[V];
        for(int i=0; i<V; i++){
            discovered[i] = false;
            processed[i] = false;
        }

        // for each connected component - do bfs and mark colors
        for(int i=0; i<V; i++){
            if(!discovered[i]){
                discovered[i] = true;
                color[i] = 1;                     // mark color for first node as 1
                bfs(this, i, discovered, processed);
            }
        }

        System.out.println("Colors are:");
        for(Integer i: color){
            System.out.print(i + " ");
        }
        System.out.println();

        if(bipartite){
            System.out.println("Graph01 is bipartite");
        }
    }

    public static void main(String[] args){
        int V = 5;
        TwoColoringProblem03 graph = new TwoColoringProblem03(V);

        graph.addEdge(0, 1);
        graph.addEdge(0, 4);
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 3);
        graph.addEdge(3, 4);

        TwoColoringProblem03.printGraph(graph);
        graph.isBipartite();
    }
}
