import java.util.*;
public class Node{
	private double val;
	private ArrayList<Node> neighbors = new ArrayList<Node>();
	
	public Node(double nodeValue){
		val=nodeValue;
	}
	
	public void addNeighbor(Node newNeighbor){
		neighbors.add(newNeighbor);
	}
	
	public void removeNeighbor(Node neighborToDelete){
		neighbors.remove(neighborToDelete);
	}
	public ArrayList<Node> getNeighbors(){
		return neighbors;
	}
	
	public double getVal(){
		return val;
	}
	public void setVal(double newVal){
		val=newVal;
	}
	public static void main(String[] args){
		Node a= new Node(2.5);
		Node b= new Node(1.5);
		Node c= new Node(5.5);
		a.addNeighbor(b);
		ArrayList<Node> neighborsOfA=a.getNeighbors();
		System.out.println(neighborsOfA.get(0).getVal());
		a.addNeighbor(c);
		for(Node i:a.getNeighbors()){
			System.out.println(i.getVal());
		}
	}
}
