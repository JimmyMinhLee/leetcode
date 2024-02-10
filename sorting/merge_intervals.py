def merge(intervals):
    if len(intervals) == 1:
        return intervals

    sorted(intervals, key = lambda pair: pair[0])
    ans = []
    current_interval = intervals[0]
    next_idx = 1
    while next_idx < len(intervals):
        next_interval = intervals[next_idx] 
        if current_interval[1] >= next_interval[0]: 
            if current_interval[1] >= next_interval[1]:
                current_interval[1] = current_interval[1]
            else:
                current_interval[1] = next_interval[1]
        else:
            ans.append(current_interval)
            current_interval = next_interval
        next_idx += 1
    ans.append(current_interval)
    return ans 

