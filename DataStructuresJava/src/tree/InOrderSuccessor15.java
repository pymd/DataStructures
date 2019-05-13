package tree;

public class InOrderSuccessor15 {
    private Node root;

    public Node getRoot(){
        return root;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    private Node successor = null;

    private boolean setInOrderSuccessor(Node root, Node node){
        if(root == null || node == null)
            return false;

        if(root.getLeftChild() == node){
            successor = root;
            return true;
        }
        if(root.getRightChild() == node)
            return true;

        // search node in LST
        successor = root;
        if(setInOrderSuccessor(root.getLeftChild(), node))
            return true;

        // search node in RST
        successor = null;
        return setInOrderSuccessor(root.getRightChild(), node);
    }

    private Node getLeftMostNode(Node root){
        if(root == null)
            return null;
        while(root.getLeftChild() != null){
            root = root.getLeftChild();
        }
        return root;
    }

    public Node getInOrderSuccessor(Node root, Node node){
        if(root == null || node == null)
            return null;
        if(node.getRightChild() != null){
            return getLeftMostNode(node.getRightChild());
        } else {
            setInOrderSuccessor(root, node);
            return successor;
        }
    }

    private Node prev = null;
    public Node successorUsingReverseInOrder(Node root, Node searchNode){
        if(root == null || searchNode == null)
            return null;

        Node result = successorUsingReverseInOrder(root.getRightChild(), searchNode);
        if(result != null)
            return result;

        if(root == searchNode){
            return prev;
        }else{
            prev = root;
        }

        return successorUsingReverseInOrder(root.getLeftChild(), searchNode);
    }

    public static void main(String[] args){
        InOrderSuccessor15 tree = new InOrderSuccessor15();
        tree.setRoot(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(6));

        Node n = tree.getRoot().getLeftChild().getLeftChild();
        System.out.println("InOrder Successor for node: " + n.getKey() + " is: ");
        Node successor = tree.getInOrderSuccessor(tree.getRoot(), n);
        if(successor != null)
            System.out.println(successor.getKey());

        System.out.println("InOrder Successor for node: " + n.getKey() + " using reverseInOrder is: ");
        Node successor2 = tree.successorUsingReverseInOrder(tree.getRoot(), n);
        if(successor2 != null)
            System.out.println(successor2.getKey());
    }
}
