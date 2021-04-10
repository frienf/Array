class LifeGrid :
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self,numRows,numCols):
        self._grid = Array2D(numRows,numCols)
        self.configure(list())

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def configure(self,coordList):
        for i in range(numRows):
            for j in range(numCols):
                self.clearCell(i,j)
        for coord in coordList :
            self.setCells(coord[0],coord[1])

    def isLiveCell(self,row,col):
        return self._grid[row,col] == GameGrid.LIVE_CELL

    def clearCell(self,row,col):
        self._grid[row,col] = GameGrid.DEAD_CELL

    def setCell(self,row,col):
        self._grid[row,col] = GameGrid.LIVE_CELL

    def numLiveNeighbors(self,row,col):
        return len(self._grid[row,col].LIVE_CEL

INIT_CONFIG=[(1,1)]

Grid_WIDTH = 5
GRID_HEIGHT = 5

NUM_GENS = 8

def main():
	grid = LifeGrid(GRID_WIDTH,GRID_HEIGHT)
	grid.configure(INIT_CONFIG)
	draw(grid)
	for i in range(NUM_GENS):
		evolve(grid)
		draw(grid)

def evolve(grid):
	liveCells=list()
	for i in range(grid.numRows()):
		for j in range(grid.numCols()):
			neighbors = grid.numLiveNeighbors(i,j)
			if (neighbors == 2 and grid.isLiveCell(i,j)) or (neighbors == 3):
				liveCells.append((i,j))
	grid.configure(liveCells)

def draw(grid):
	print(grid)			