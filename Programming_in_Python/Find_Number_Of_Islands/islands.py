Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '''
    Time Complexity: O(N * M)
    Space Complexity: O(N * M)

    Where N and M are the number of rows and columns of the 2D array, respectively.
'''
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

'''
    dx[] and dy[] are the arrays that define each of the eight directions.

    dx[0], dy[0] : West
    dx[1], dy[1] : North-West
    dx[2], dy[2] : North
    dx[3], dy[3] : North-East
    dx[4], dy[4] : East
    dx[5], dy[5] : South-East
    dx[6], dy[6] : South
    dx[7], dy[7] : South-West

'''

def findIslandsHelper(mat, n, m, x, y, vis):

	# Check if this cell is valid.
    vis[x][y] = True

    for i in range(8):

        nextX = x + dx[i]
        nextY = y + dy[i]
        if(nextX >=0 and nextX < n and nextY >= 0 and nextY < m and vis[nextX][nextY] == False and mat[nextX][nextY] == 1):
        	findIslandsHelper(mat, n, m, nextX, nextY, vis)


def findIslands(mat, n, m):

    vis = [[False for i in range(m)] for j in range(n)]
    islands = 0

    for i in range(n):
        for j in range(m):
            if(mat[i][j] == 1 and not(vis[i][j])):

                # We have found an undiscovered island.
                islands += 1
                findIslandsHelper(mat, n, m, i, j, vis)

    return islands
