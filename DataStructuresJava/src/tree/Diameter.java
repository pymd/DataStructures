package tree;

public class Diameter {
    Node root;

    class Height{
        int h;
    }

    public void setRoot(Node root){
        this.root = root;
    }

    public Node getRoot(){
        return root;
    }

    // InOrder Traversal
    public void inOrder(Node node){
        if(node == null){
            return;
        }
        inOrder(node.getLeftChild());
        System.out.print(node.getKey() + " ");
        inOrder(node.getRightChild());
    }

    // Helper method
    private int height(Node root){
        if(root == null)
            return 0;
        return 1 + Math.max(height(root.getLeftChild()), height(root.getRightChild()));
    }

    // Time Complexity: O(n**2)
    public int getDiameter(Node root){
        if(root == null){
            return 0;
        }
        return Math.max(
                Math.max(getDiameter(root.getLeftChild()), getDiameter(root.getRightChild())),
                (1 + height(root.getLeftChild()) + height(root.getRightChild()))
        );
    }

    // Time Complexity: O(n) (height calculated in same routine)
    public int getDiameterOptimized(Node root){
        Height h = new Height();
        return getDiameterOptimized(root, h);
    }

    // Time Complexity: O(n) (height calculated in same routine)
    public int getDiameterOptimized(Node root, Height h){
        Height leftHeight = new Height();
        Height rightHeight = new Height();
        if(root == null){
            h.h = 0;
            return 0;
        }
        int leftDiameter = getDiameterOptimized(root.getLeftChild(), leftHeight);
        int rightDiameter = getDiameterOptimized(root.getRightChild(), rightHeight);

        // height for this tree = max of (height of LST and RST)
        h.h = Math.max(leftHeight.h, rightHeight.h) + 1;

        return Math.max(Math.max(leftDiameter, rightDiameter),
                1 + leftHeight.h + rightHeight.h);
    }

    public static void main(String[] args){
        Diameter tree = new Diameter();
        tree.setRoot(new Node(1));
        tree.getRoot().setLeftChild(new Node(2));
        tree.getRoot().setRightChild(new Node(3));
        tree.getRoot().getLeftChild().setLeftChild(new Node(4));
        tree.getRoot().getLeftChild().setRightChild(new Node(5));
//        tree.getRoot().getRightChild().setLeftChild(new Node(6));
//        tree.getRoot().getRightChild().setRightChild(new Node(7));

        System.out.println("InOrder Traveral of tree:");
        tree.inOrder(tree.getRoot());
        System.out.println("");

        System.out.println("Diameter of tree is:");
        System.out.println(tree.getDiameter(tree.getRoot()));

        System.out.println("Diameter of tree with optimized Algo is:");
        System.out.println(tree.getDiameterOptimized(tree.getRoot()));
    }
}
