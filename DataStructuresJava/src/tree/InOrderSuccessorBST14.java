package tree;

public class InOrderSuccessorBST14 {
    Node root;

    public Node getRoot(){
        return root;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    // constructor
    public InOrderSuccessorBST14(Node root){
        this.setRoot(root);
    }

    public void inOrderTraversal(Node root){
        if(root == null)
            return;
        inOrderTraversal(root.getLeftChild());
        System.out.print(root.getKey() + " ");
        inOrderTraversal(root.getRightChild());
    }

    // min node is the leftMost Node
    public Node minNodeInBST(Node root){
        if(root == null)
            return null;
        Node current = root;
        while(current.getLeftChild() != null)
            current = current.getLeftChild();
        return current;
    }

    public void insertIntoBST(Node root, int key){
        if(root == null)
            return;
        if(root.getKey() > key){
            if (root.getLeftChild() == null) {
                Node node = new Node(key);
                root.setLeftChild(node);
                return;
            }
            insertIntoBST(root.getLeftChild(), key);
        } else {
            if (root.getRightChild() == null){
                Node node = new Node(key);
                root.setRightChild(node);
                return;
            }
            insertIntoBST(root.getRightChild(), key);
        }
    }

    public Node getInOrderSuccessor(Node root, Node node){
        if(root == null || node == null)
            return null;
        if(node.getRightChild() != null){
            return minNodeInBST(node.getRightChild());
        }
        Node current = root;
        Node successor = current;
        while(current != null && current != node){
            if(current.getKey() > node.getKey()){
                successor = current;
                current = current.getLeftChild();
            } else {
                current = current.getRightChild();
            }
        }
        return successor;
    }

    public static void main(String[] args){
        InOrderSuccessorBST14 tree = new InOrderSuccessorBST14(new Node(5));
        tree.insertIntoBST(tree.getRoot(), 10);
        tree.insertIntoBST(tree.getRoot(), 1);
        tree.insertIntoBST(tree.getRoot(), 6);
        tree.insertIntoBST(tree.getRoot(), 9);
        tree.insertIntoBST(tree.getRoot(), 3);
        tree.insertIntoBST(tree.getRoot(), 2);
        tree.insertIntoBST(tree.getRoot(), 8);

        System.out.println();
        tree.inOrderTraversal(tree.getRoot());
        System.out.println();

        Node node = tree.minNodeInBST(tree.getRoot());
        System.out.println("Min Tree Node is:" + node.getKey());

        Node n = tree.getRoot().getLeftChild().getRightChild().getLeftChild();
        System.out.println("Find successor for node:" + n.getKey());
        Node successor = tree.getInOrderSuccessor(tree.getRoot(), n);
        System.out.println("InOrder Successor of the node: " + successor.getKey());
    }
}
