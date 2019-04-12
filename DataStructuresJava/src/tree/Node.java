package tree;

public class Node {
    int key;
    Node leftChild, rightChild;

    public Node getLeftChild() {
        return leftChild;
    }

    public void setLeftChild(Node leftChild) {
        this.leftChild = leftChild;
    }

    public Node getRightChild() {
        return rightChild;
    }

    public void setRightChild(Node rightChild) {
        this.rightChild = rightChild;
    }

    public int getKey() {
        return key;
    }

    public void setKey(int key) {
        this.key = key;
    }

    // Constructor
    public Node(int key){
        this.key = key;
        leftChild = rightChild = null;
    }
}
