import java.util.*;
class maze{

	public enum State{
		UNVISITED,
		VISITING,
		NO_PATH_FOUND;
	}

	public static boolean oob(int[][] maze, int i , int j){
		return i<0 || i >= maze.length  || j<0 || j>= maze[0].length;
	}

		
	public static boolean pathExists(int[][] maze,int i ,int j ,State[][] memo){
		// bounday conditions 
		if (oob(maze,i,j) || maze[i][j] == 1)
			return false;

		if(i == maze.length-1 && j == maze[0].length - 1) 
			return true;

		if(memo[i][j] == State.NO_PATH_FOUND || memo[i][j] == State.VISITING)
			return false;

		memo[i][j] = State.VISITING;
			
		if(pathExists(maze,i,j-1,memo)){
				return true;
		}
		if(pathExists(maze,i,j+1,memo)){
				return true;
		}
		if(pathExists(maze,i-1,j,memo)){
				return true;
		}
		if(pathExists(maze,i+1,j,memo)){
				return true;
		}
		memo[i][j] = State.NO_PATH_FOUND;
		return false;
	}   

	public static boolean path(int[][] maze){
		if (maze == null || maze.length ==0)
		       return false;
		State[][] memo = new State[maze.length][maze[0].length];
			
		for(State[] states:memo)
			Arrays.fill(states,State.UNVISITED);
		
		return pathExists(maze,0,0,memo);
	}


	public static void main(String [] args){
		int[][] maze  = { {0,1,0,0,0},
				  {0,1,0,1,0},
				  {0,1,0,1,0},
				  {0,1,0,1,0},
				  {0,0,0,1,0}
				};
		boolean result = path(maze);
		System.out.println(result);	
	}
}
