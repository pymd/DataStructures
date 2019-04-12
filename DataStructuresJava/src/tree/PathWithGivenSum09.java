package tree;

public class PathWithGivenSum09 {
    private Node root;


    public PathWithGivenSum09(Node root){
        setRoot(root);
    }

    public Node getRoot(){
        return root;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    public boolean hasPathWithSum(Node root, Integer n){
        if(root == null)
            return false;
        n = n - root.getKey();
        if(root.getLeftChild() == null && root.getRightChild() == null){
            if(n == 0){
                return true;
            }
            return false;
        }
        return (hasPathWithSum(root.getLeftChild(), n) || hasPathWithSum(root.getRightChild(), n));
    }

    public static void main(String[] args){
        PathWithGivenSum09 tree = new PathWithGivenSum09(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(6));

        int s = 8;
        boolean result = tree.hasPathWithSum(tree.getRoot(), s);
        System.out.println("Does it have a path with sum = " + s + " : " + result);
    }
}
