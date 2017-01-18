package list;

public class ListNode {
	private Integer val;
	private ListNode next;

	public String toString(){
		return val.toString();
	}

	public ListNode(){
		this.val = 0;
		this.next = null;
	}

	public Integer getVal(){
		return this.val;
	}

	public void setVal(Integer val){
		this.val = val;
	}

	public ListNode getNext(){
		return this.next;
	}

	public void setNext(ListNode next){
		this.next = next;
	}
}