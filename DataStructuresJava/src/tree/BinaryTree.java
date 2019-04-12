package tree;

public class BinaryTree {
    Node root;

    public Node getRoot(){
        return this.root;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    // Constructors
    BinaryTree(int key){
        this.setRoot(new Node(key));
    }

    BinaryTree(){
        this.setRoot(null);
    }

    // Tree Traversals

    // InOrder Traversal
    public void inOrder(Node node){
        if(node == null){
            return;
        }
        inOrder(node.getLeftChild());
        System.out.print(node.getKey() + " ");
        inOrder(node.getRightChild());
    }

    // Pre-Order Traversal
    public void preOrder(Node node){
        if(node == null){
            return;
        }
        System.out.print(node.getKey() + " ");
        preOrder(node.getLeftChild());
        preOrder(node.getRightChild());
    }

    // Post-Order Traversal
    public void postOrder(Node node){
        if(node == null){
            return;
        }
        postOrder(node.getLeftChild());
        postOrder(node.getRightChild());
        System.out.print(node.getKey() + " ");
    }

    public static void main(String[] args){
        BinaryTree tree = new BinaryTree(1);
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));

        System.out.println("PreOrder Traversal of the tree:");
        tree.preOrder(tree.getRoot());
        System.out.println();

        System.out.println("InOrder Traversal of the tree:");
        tree.inOrder(tree.getRoot());
        System.out.println();

        System.out.println("PostOrder Traversal of the tree:");
        tree.postOrder(tree.getRoot());
        System.out.println();
    }
}
