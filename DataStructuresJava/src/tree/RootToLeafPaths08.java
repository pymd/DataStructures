package tree;

public class RootToLeafPaths08 {
    private Node root;

    public RootToLeafPaths08(Node root){
        setRoot(root);
    }

    public void setRoot(Node root){
        this.root = root;
    }

    public Node getRoot() {
        return root;
    }

    private void printArr(Node[] arr, Integer pathLen){
        System.out.println();
        for(int i=0; i<=pathLen; i++){
            if(arr[i] != null){
                System.out.print(arr[i].getKey() + " ");
            }else{
                System.out.print("null ");
            }
        }
        System.out.println();
    }

    // Todo: Understand its time complexity: How is it O(n^2)
    private void printAllPaths(Node root, Node[] paths, Integer pathLen){
        if(root == null)
            return;
        // push this element to array
        paths[pathLen] = root;

        // Leaf node
        if(root.getLeftChild() == null && root.getRightChild() == null){
            printArr(paths, pathLen);
            return;
        }

        printAllPaths(root.getLeftChild(), paths, pathLen+1);
        printAllPaths(root.getRightChild(), paths, pathLen+1);
    }

    public void printAllRootToLeafPaths(Node root){
        Node[] paths = new Node[1000];
        int pathLen = 0;
        printAllPaths(root, paths, pathLen);
    }

    public static void main(String[] args){
        RootToLeafPaths08 tree = new RootToLeafPaths08(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(6));

        tree.printAllRootToLeafPaths(tree.getRoot());
    }
}
