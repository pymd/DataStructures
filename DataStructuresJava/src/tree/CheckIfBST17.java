package tree;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class CheckIfBST17 {
    private Node root;

    public Node getRoot() {
        return root;
    }

    public void setRoot(Node root) {
        this.root = root;
    }

    public CheckIfBST17(Node root) {
        this.root = root;
    }

    private void print(String s){
        System.out.println(s);
    }

    // T(n): O(n), No extra space
    public boolean isBST(Node root, Integer minVal, Integer maxVal){
        if(root == null)
            return true;
        if(minVal != null && minVal > root.getKey())
            return false;
        if(maxVal != null && maxVal < root.getKey())
            return false;
        boolean isLstBST = isBST(root.getLeftChild(), minVal, root.getKey());
        boolean isRstBST = isBST(root.getRightChild(), root.getKey(), maxVal);
        return isLstBST && isRstBST;
    }

    private void inOrder(Node root, List<Node> arr){
        if(root == null)
            return;
        inOrder(root.getLeftChild(), arr);
        arr.add(root);
        inOrder(root.getRightChild(), arr);
    }

    // T(n): O(n), Space: O(n) to store the inorder array
    public boolean isBSTWithSpace(Node root){
        List<Node> inorder = new ArrayList<>();
        inOrder(root, inorder);
        for(int i=0; i<inorder.size()-1; i++){
            if(inorder.get(i).getKey() > inorder.get(i+1).getKey())
                return false;
        }
        return true;
    }

    public static void main(String[] args){
        CheckIfBST17 tree = new CheckIfBST17(new Node(50));
        tree.getRoot().setLeftChild(new Node(25));
        tree.getRoot().getLeftChild().setLeftChild(new Node(20));
        tree.getRoot().getLeftChild().getLeftChild().setLeftChild(new Node(10));

        tree.getRoot().getLeftChild().setRightChild(new Node(30));
        tree.getRoot().getLeftChild().getLeftChild().setRightChild(new Node(23));
        tree.getRoot().setRightChild(new Node(75));
        tree.getRoot().getRightChild().setRightChild(new Node(100));

        boolean res = tree.isBST(tree.getRoot(), null, null);
        System.out.println("Is the tree balanced?: " + res);

        boolean res2 = tree.isBSTWithSpace(tree.getRoot());
        System.out.println("Is the tree balanced (using inOrder)?: " + res2);
    }
}
