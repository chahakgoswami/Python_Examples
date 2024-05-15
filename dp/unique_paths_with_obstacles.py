def unique_paths_with_obstacles(obstacle_grid):
    n = len(obstacle_grid)
    m = len(obstacle_grid[0])
    dp = [[0] * m for _ in range(n)]

    obs = 1
    for i in range(m):
        if obstacle_grid[0][i] == 1:
            obs = 0
        dp[0][i] = obs

    obs = 1
    for i in range(n):
        if obstacle_grid[i][0] == 1:
            obs = 0
        dp[i][0] = obs

    for i in range(1, n):
        for j in range(1, m):
            if obstacle_grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m - 1]
