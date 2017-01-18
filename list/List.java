package list;

import list.ListNode;

public class List {
	private ListNode head;

	public List(){
		this.head = null;
	}

	// add a node at the end of the list
	public void addNode (Integer val){
		ListNode node = new ListNode();
		node.setVal(val);
		if(this.head == null){
			this.head = node;
		}else{
			ListNode current = this.head;
			while(current.getNext() != null){
				current = current.getNext();
			}
			current.setNext(node);
		}
	}

	// delete the first node with the given value from the list
	public void deleteNode (Integer val){
		ListNode current = this.head;
		if (current == null){
			return;
		}else if(current.getVal() == val){
			this.head = current.getNext();
		}else{
			while (current.getNext() != null){
				if(current.getNext().getVal() == val){
					// This is the node to be deleted
					current.setNext(current.getNext().getNext());
				}
				current = current.getNext();
			}
		}
	}

	public void printList(){
		ListNode current = this.head;
		System.out.println("Printing out the list");
		while (current != null){
			System.out.print(current.getVal() + " --> ");
			current = current.getNext();
		}
		System.out.println("Null");
	}

	public ListNode getHead(){
		return this.head;
	}

	public void setHead (ListNode head){
		this.head = head;
	}

	public static void main (String[] args){
		List lst = new List();

		lst.deleteNode(30);
		lst.printList();

		lst.addNode(10);
		lst.printList();

		lst.addNode(20);
		lst.addNode(30);
		lst.addNode(40);
		lst.addNode(50);
		lst.printList();

		lst.deleteNode(30);

		lst.printList();
	}
}