'''
Given a sorted list of intervals by start
And a new_interval

Insert the new interval to intevals maintaing the sort order
If there are overlapping intervals, merge  them

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]


[1,3] [6,9] => current_end < new_start = add_current

current_start > new_end = add_new



[6,9], [[1,3] => current_start > new_end = add_new
[1,3] [2,5] => current_end > new_start = merge ( min(current_start, new_start), max(current_end, new_end))

[1,4] [2,3] => current_end > new_end = add_current

'''



'''

1. Non overlapping

[a - b]
        [c - d]

c > b

2. [c - d]
           [a - b]

a > d

Overlapping
-----------

not(b > c) or not (a > d)

(b <= c) or (a <= d)


[a -- b]
      [c -- d]


[a ------- b]      
  [c --- d]

    [a -- b]
[c ---------- d]

[c ---  d]
    [a ---- b]


Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        new_start,new_end=newInterval
        for start,end in intervals:
            #Current Interval completely before 
            if end < new_start:
                result.append([start,end])
            #Current Interval Completely After
            elif start > new_end:
                result.append([new_start,new_end])
                new_start,new_end = start,end
            ## Merge case
            else:
                new_start = min(start,new_start)
                new_end = max(end,new_end)
        result.append([new_start,new_end])
        return result


'''

def insert(intervals, newInterval):
    res = []
    i, n = 0, len(intervals)

    # 1. All intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # 2. Merge all overlapping intervals into newInterval
    while i < n and  not(intervals[i][0] > newInterval[1]):
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)

    # 3. The rest
    res.extend(intervals[i:])
    return res




def insert_intevals(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

  merged_list: list[list[int]] = []
  i = 0
  n = len(intervals)

  # Non-overlapping
  while i < n and intervals[i][1] < newInterval[0]:
    merged_list.append(intervals[i])
    i += 1

  if i == n-1:
    merged_list.append(newInterval)
  # Overlapping
  while i < n and ( (intervals[i][1] <=  newInterval[0])  or  (intervals[i][0] <=  newInterval[1]) )
    
    

  

    

  
print(insert_intevals([[1,3],[6,9]],[2,5]))
      
      

      

    


  


