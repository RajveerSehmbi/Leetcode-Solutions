def numIslands(grid):

	def dfs(row, col):
	
		if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
			return	
		
		val = grid[row][col]
		if val == "0" or val == ".":
			return
		
		grid[row][col] = "."
		dfs(row - 1, col)
		dfs(row + 1, col)
		dfs(row, col - 1)
		dfs(row, col + 1)


	num_of_islands = 0
	for i, row in enumerate(grid):
		for j, val in enumerate(row):
			if val == "1":
				num_of_islands += 1
				dfs(i, j)
	return num_of_islands
			
