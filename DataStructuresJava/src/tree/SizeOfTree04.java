package tree;

public class SizeOfTree04 {
    private Node root;

    public SizeOfTree04(Node root){
        setRoot(root);
    }

    public Node getRoot(){
        return root;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    // Bottom up approach
    public Integer getSize(Node node){
        if(node == null)
            return 0;
        int lstSize = getSize(node.getLeftChild());
        int rstSize = getSize(node.getRightChild());
        return (1+lstSize+rstSize);
    }

    public static void main(String[] args){
        SizeOfTree04 tree = new SizeOfTree04(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(6));
        tree.getRoot().getLeftChild().getLeftChild().setLeftChild(new Node(8));

        System.out.println("Size of tree = " + tree.getSize(tree.getRoot()));
    }
}
