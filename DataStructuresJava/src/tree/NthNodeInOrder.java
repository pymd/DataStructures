package tree;

public class NthNodeInOrder {
    Node root;
    static int count;

    void setRoot(Node root){
        this.root = root;
    }

    Node getRoot(){
        return root;
    }

    Node getNthNodeInOrder(Node root, int n){
        if(root == null){
            return null;
        }
        Node nodeInLst = getNthNodeInOrder(root.getLeftChild(), n);
        if(nodeInLst != null){
            return nodeInLst;
        }
        count++;
        if(count == n){
            return root;
        }
        Node nodeInRst = getNthNodeInOrder(root.getRightChild(), n);
        return nodeInRst;
    }

    public static void main(String[] args){
        NthNodeInOrder tree = new NthNodeInOrder();
        tree.setRoot(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));

        int n = 6;

        System.out.println("Nth node is: " + (tree.getNthNodeInOrder(tree.getRoot(), n)).getKey());
    }
}
