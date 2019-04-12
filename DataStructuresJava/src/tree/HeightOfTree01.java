package tree;

public class HeightOfTree01 {
    private Node root;

    // constructor
    public HeightOfTree01(Node root){
        setRoot(root);
    }

    public Node getRoot(){
        return root;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    // Bottom-up Approach
    public int height(Node node){
        if(node == null)
            return 0;
        int lstHeight = height(node.getLeftChild());
        int rstHeight = height(node.getRightChild());
        return Math.max(lstHeight, rstHeight)+1;            // processing step
    }

    // Top-Down Approach
    public int heightTopDown(Node node, int distanceFromRoot){
        if(node == null)
            return distanceFromRoot;
        int newDistance = distanceFromRoot+1;                           // processing step
        int lstHeight = heightTopDown(node.getLeftChild(), newDistance);
        int rstHeight = heightTopDown(node.getRightChild(), newDistance);
        return Math.max(lstHeight, rstHeight);
    }

    public static void main(String[] args){
        HeightOfTree01 tree = new HeightOfTree01(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(6));

        int h1 = tree.height(tree.getRoot());
        System.out.println("Height through bottom-up approach is:" + h1);

        int h2 = tree.heightTopDown(tree.getRoot(), 0);
        System.out.println("Height through top-down approach is:" + h2);
    }
}
