def insert(intervals, newInterval):
    result = []
    i, n = 0, len(intervals)
    
    # 1. intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # 2. merge all overlapping intervals into newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    
    # 3. remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result