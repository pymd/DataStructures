package tree;

public class CheckIfHeightBalanced17 {
    private Node root;

    public CheckIfHeightBalanced17(Node root){
        setRoot(root);
    }

    public void setRoot(Node root){
        this.root = root;
    }

    public Node getRoot(){
        return root;
    }

    public boolean isBalanced(Node root, Integer[] height){
        if(root == null)
            return true;

        Integer[] lstHeight = new Integer[1];
        Integer[] rstHeight = new Integer[1];
        lstHeight[0] = rstHeight[0] = 0;

        boolean lstBalanced = isBalanced(root.getLeftChild(), lstHeight);
        boolean rstBalanced = isBalanced(root.getRightChild(), rstHeight);

        if(root.getLeftChild() == null && root.getRightChild() == null)
            height[0] = 1;
        else
            height[0] = Math.max(lstHeight[0], rstHeight[0])+1;

        if(Math.abs(lstHeight[0]-rstHeight[0]) <= 1 && lstBalanced && rstBalanced)
            return true;
        return false;
    }

    public static void main(String[] args){
        CheckIfHeightBalanced17 tree = new CheckIfHeightBalanced17(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getRightChild().setRightChild(new Node(10));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
        tree.getRoot().getLeftChild().getLeftChild().setLeftChild(new Node(6));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(7));

        boolean res = tree.isBalanced(tree.getRoot(), new Integer[]{0});
        System.out.println("Is the tree balanced?:" + res);
    }
}
