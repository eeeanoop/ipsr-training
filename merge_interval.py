# Give a list of intervals - intervals = [[1,3],[2,6],[8,10],[15,18]]
# Return a list of interval where the overlaping intervals are merged - [[1,6],[8,10],[15,18]]

'''
[[9,13],[13,16], [10,11] ] 
# Sort
[[9,13], [10,11], [13,16] ] 
[[9,11],[13,16] ] 
'''

def merge_overlapping_intervals(interval: list[list[int]]):
    # Bring intervals that needs to merged adjacent to each other a.k.a sorting by start time
    # [[9,11], [10,11], [13,16], ] 

    interval.sort(key=lambda x: x[0])
    
    # iterate through the intervals
    # check if the current_endtime >= previous_end
    # add the previous_start, current_end as the new merged interval
    previous_end = float('-inf')
    result: list[list[int]] = []
    for start, end in interval:
      if start > previous_end :
        # Do not merge
        result.append([start, end])
        
      else:
        result[-1] =[min(start,previous_start), max(end,previous_end)]
      previous_end = result[-1][1]
      previous_start = result[-1][0]
        # [[9,13]]
    print(result)
      
        
      

'''

# python doesn't care about the type
def check_float_int_conversion(x: chr):
  print(x)
    
check_float_int_conversion(1.1)
'''

merge_overlapping_intervals(interval=[[1,3],[2,6],[8,10],[15,18]])
