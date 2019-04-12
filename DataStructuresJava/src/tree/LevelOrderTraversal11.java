package tree;
import java.util.Iterator;
import java.util.Queue;
import java.util.LinkedList;

public class LevelOrderTraversal11 {
    private Node root;

    public void setRoot(Node root){
        this.root = root;
    }

    public Node getRoot(){
        return root;
    }

    public LevelOrderTraversal11(Node root){
        setRoot(root);
    }

    // Using a queue - time complexity: O(n), Space: O(n)
    public void levelOrderTraversal(Node root){
        System.out.println();
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(root);

        while(!queue.isEmpty()){
            // remove the first element
            Node node = queue.poll();
            // print the first element
            System.out.print(node.getKey() + " ");
            // insert the first element's children
            if(node.getLeftChild() != null){
                queue.add(node.getLeftChild());
            }
            if(node.getRightChild() != null){
                queue.add(node.getRightChild());
            }
        }
        System.out.println();
    }

    private int height(Node root){
        if(root == null)
            return 0;
        int lstHeight = height(root.getLeftChild());
        int rstHeight = height(root.getRightChild());
        return Math.max(lstHeight, rstHeight)+1;
    }

    private void printLevel(Node root, int level){
        if(root == null)
            return;
        if(level == 0) {
            System.out.print(root.getKey() + " ");
            return;
        }
        printLevel(root.getLeftChild(), level-1);
        printLevel(root.getRightChild(), level-1);
    }

    // Time Complexity: O(n^2)
    public void levelOrderTraversalInEfficient(Node root){
        for(int i=0; i<height(root); i++){
            printLevel(root, i);
        }
    }

    public static void main(String[] args){
        LevelOrderTraversal11 tree = new LevelOrderTraversal11(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(5));
        tree.getRoot().getLeftChild().setRightChild(new Node(4));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(6));
        tree.getRoot().getLeftChild().getLeftChild().setLeftChild(new Node(8));

        tree.levelOrderTraversal(tree.getRoot());
        tree.levelOrderTraversalInEfficient(tree.getRoot());
    }
}
