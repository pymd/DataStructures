package tree;

public class MaxInBinaryTree02 {
    private Node root;

    public MaxInBinaryTree02(Node root){
        setRoot(root);
    }

    public Node getRoot(){
        return root;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    // Bottom-up approach
    public int maxValueInTree(Node node){
        if(node == null){
            return Integer.MIN_VALUE;
        }
        int lstMax = maxValueInTree(node.getLeftChild());
        int rstMax = maxValueInTree(node.getRightChild());
        return Math.max(Math.max(lstMax, rstMax), node.getKey());       // processing step
    }

    // Top-Down approach
    public int maxValueInTreeTopDown(Node node, int maxVal){
        if(node == null){
            return maxVal;
        }
        int mVal = Math.max(maxVal, node.getKey());
        int lstMax = maxValueInTreeTopDown(node.getLeftChild(), mVal);
        int rstMax = maxValueInTreeTopDown(node.getRightChild(), mVal);
        return Math.max(lstMax, rstMax);
    }

    public static void main(String[] args){
        MaxInBinaryTree02 tree = new MaxInBinaryTree02(new Node(1));
        tree.getRoot().setLeftChild(new Node(20));
        tree.getRoot().setRightChild(new Node(13));
        tree.getRoot().getLeftChild().setLeftChild(new Node(24));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(25));

        int m1 = tree.maxValueInTree(tree.getRoot());
        System.out.println("Max Value through bottom-up approach is:" + m1);

        int m2 = tree.maxValueInTreeTopDown(tree.getRoot(), Integer.MIN_VALUE);
        System.out.println("Max Value through top-down approach is:" + m2);
    }
}
