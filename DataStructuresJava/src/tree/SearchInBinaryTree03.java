package tree;

public class SearchInBinaryTree03 {
    private Node root;

    public SearchInBinaryTree03(Node root){
        setRoot(root);
    }

    public Node getRoot(){
        return root;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    public boolean searchInTree(Node node, Integer key){
        if(node == null)
            return false;
        if(node.getKey() == key)
            return true;
        return (searchInTree(node.getLeftChild(), key)) ||
                (searchInTree(node.getRightChild(), key));
    }

    public static void main(String[] args){
        SearchInBinaryTree03 tree = new SearchInBinaryTree03(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(6));

        boolean val = tree.searchInTree(tree.getRoot(), 6);
        System.out.println("Does it have the value?: " + val);
    }
}
