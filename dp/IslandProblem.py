def isSafe(M, row, col, visited):
    return (row >= 0) and (row < len(M)) and (col >= 0) and (col < len(M[0])) and (M[row][col] == 1 and not visited[row][col])

def DFS(M, row, col, visited):
    rowNum = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNum = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited[row][col] = True

    for k in range(8):
        if isSafe(M, row + rowNum[k], col + colNum[k], visited):
            DFS(M, row + rowNum[k], col + colNum[k], visited)

def countIsland(M):
    visited = [[False for _ in range(len(M[0]))] for _ in range(len(M))]
    count = 0

    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 1 and not visited[i][j]:
                DFS(M, i, j, visited)
                count += 1

    return count

def main():
    M = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

    print(countIsland(M))

if __name__ == "__main__":
    main()
