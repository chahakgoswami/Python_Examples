def spiral_rotation(input_matrix):
    n = len(input_matrix)
    m = len(input_matrix[0])
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    direction = 0

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                print(input_matrix[top][i], end=" ")
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                print(input_matrix[i][right], end=" ")
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                print(input_matrix[bottom][i], end=" ")
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                print(input_matrix[i][left], end=" ")
            left += 1
        direction = (direction + 1) % 4

# Example usage
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

spiral_rotation(a)
