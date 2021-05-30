import java.util.*;

class islands{

	static int ROW;
	static int COL;

	public static int  findIsland(int[][] grid){
		
		boolean[][] visited = new boolean[ROW][COL];
		int count = 0;
		for(int i = 0; i < ROW; i++){
			for(int j = 0; j < COL; j++){
				if(grid[i][j] == 1 && !visited[i][j]){
					DFS(grid,i,j,visited);		
					count++;	
				}
			}

		}

		return count ;
	}
	
	public static void DFS(int[][] grid ,int row, int col, boolean[][] visited){
		
		int[] rowN = {-1,-1,-1,0,0,1,1,1};
		int[] colN = {-1,0,1,-1,1,-1,0,1};	
	
		visited[row][col] = true;
		for(int k = 0 ; k < 8 ; k++){
			if(isSafe(grid,row+rowN[k],col+colN[k],visited)){
				DFS(grid,row+rowN[k],col+colN[k],visited);
			}

		}
	}
	
	public static  boolean isSafe(int[][] grid, int row, int col , boolean[][] visited){
		return (row >=0 && row < ROW && col >= 0 && col < COL && grid[row][col] == 1 && !visited[row][col]);
	}


	public static void main(String [] args){
		int[][] grid = new int[][]{ {1,1,0,0,0},
					    {0,1,0,0,1},
					    {1,0,0,1,1},
					    {0,0,0,0,0},
					    {1,0,1,0,1}};
		ROW  = grid.length;
		COL  = grid[0].length;	
	
		int islands = findIsland(grid);
		System.out.println(islands);

	}

}
