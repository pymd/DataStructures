package tree;

// Todo: Convert the tree to its mirror tree
public class MirrorOfTree07 {
    private Node root;

    public Node getRoot(){
        return root;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    public MirrorOfTree07(Node root){
        setRoot(root);
    }

    // Recursive Method
    public void convertTreeToMirror(Node root){
        if(root == null)
            return;
        // recurse
        convertTreeToMirror(root.getLeftChild());
        convertTreeToMirror(root.getRightChild());

        // Mirror this node
        Node temp = root.getRightChild();
        root.setRightChild(root.getLeftChild());
        root.setLeftChild(temp);
    }

    // Todo: Iterative Method - Uses a Queue
    public void convertTreeToMirrorIterative(Node root){
        if(root == null)
            return;
    }

    public void inOrder(Node node){
        if(node == null)
            return;
        inOrder(node.getLeftChild());
        System.out.print(node.getKey() + " ");
        inOrder(node.getRightChild());
    }

    public static void main(String[] args){
        MirrorOfTree07 tree = new MirrorOfTree07(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(6));

        System.out.println("Original tree is:");
        tree.inOrder(tree.getRoot());
        tree.convertTreeToMirror(tree.getRoot());
        System.out.println();
        System.out.println("Mirror tree is:");
        tree.inOrder(tree.getRoot());
        System.out.println();
    }
}
