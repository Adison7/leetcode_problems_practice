def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                continue  # already set
            else:
                from_top = dp[i-1][j] if i > 0 else 0
                from_left = dp[i][j-1] if j > 0 else 0
                dp[i][j] = from_top + from_left
    
    return dp[m-1][n-1]