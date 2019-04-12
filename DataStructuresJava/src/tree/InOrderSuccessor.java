package tree;

public class InOrderSuccessor {
    Node root;

    Node getRoot(){
        return root;
    }

    void setRoot(Node root){
        this.root = root;
    }

    void getInOrderSuccessor(Node root, Node node){
        if(root == null){
            return;
        }
        if(node == null){
            System.out.println("Node is null");
            return;
        }
        getInOrderSuccessor(root.getLeftChild(), node);
        if(root.getKey() == node.getKey()){
            //            return node;
        }
        getInOrderSuccessor(root.getRightChild(), node);
    }

    public static void main(String[] args){
        InOrderSuccessor tree = new InOrderSuccessor();
        tree.setRoot(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));

    }
}
