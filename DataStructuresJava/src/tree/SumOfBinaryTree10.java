package tree;

public class SumOfBinaryTree10 {
    private Node root;

    public SumOfBinaryTree10(Node root){
        setRoot(root);
    }

    public Node getRoot(){
        return root;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    public int sumOfTree(Node root){
        if(root == null)
            return 0;
        int lstSum = sumOfTree(root.getLeftChild());
        int rstSum = sumOfTree(root.getRightChild());
        return lstSum+rstSum+root.getKey();
    }

    public static void main(String[] args){
        SumOfBinaryTree10 tree = new SumOfBinaryTree10(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
//        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(6));

        int s = tree.sumOfTree(tree.getRoot());
        System.out.println("The sum of binary tree = " + s);
    }
}
