import java.util.*;

class shortestpath{
	
	static int ROW = mat.length;
	static int COL = mat[0].length;	

	public class Pair{
		private int x;
		private int y;
		
		public Pair(int x, int y){
			this.x = x;
			this.y = y;	
		}

	}
	public class Node{
		Pair pt;
		int distance ;

		public Node(Pair p, int distance){
			this.pt = p;
			this.distance = distance ;
		}
		

	}	

	public static int BFS(int[][] mat, Pair source , Pair destination){
		
		if( mat[source.x][source.y] == 0 || mat[destination.x][destination.y] == 0){
			return -1;
		}

		// directions 
		int[] rowdir = {0,0,-1,1};
		int[] coldir = {1,-1,0,0};
		
		Queue<Node> q = new LinkedList<>();
		
		boolean[][] visited = new boolean [ROW][COL];	
		Node s = new Node(source , 0);
		q.add(s);	
		visited[source.x][source.y] = true;
		while(!q.isEmpty()){
			Node curr = q.peek();
			Point pt  = curr.pt;
		// check if we reached the destination ?
		if ((pt.x == destination.x) && (pt.y == destination.y)){
			return curr.distance;
		}
		
		q.remove();
		for (int i = 0 ; i < 4 ; i++){
			int row = pt.x + rowdir[i];
			int col = pt.y + coldir[j];

			if (isValid(row,col) && mat[row][col] == 1 && !visited[row][col]){
				visited[row][col] = true;
				Node adjcell = new Node(new Pair(row,col),curr.distance+1);
				q.add(adjcell);
			}

		}


		}
		return -1 ;
	}	
	
	public static boolean isValid(int row, int col){
		return ((row >= 0 && row < ROW) && (col >=0 && col < COL));
	}

	public static void main(String [] args){
		int[][] mat = { {0,1,0,1},
				{1,0,1,1},
				{0,1,1,1},
				{1,1,1,0}};
		Pair source = new Pair(0,3);	
		int result = BFS(mat, source , destination);
		System.out.println(result);
	}

}
