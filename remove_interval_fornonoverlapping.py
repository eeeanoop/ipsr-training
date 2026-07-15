


def count_overlapping_intevals(intervals: list[list[int]]) -> int:
    overlapping_interval_count: int = 0
    non_overlapping_intv: list[list[int]] = []
    intervals.sort(key=lambda x : x[0])

    for curr_start, curr_end in intervals:
        if not non_overlapping_intv:
            non_overlapping_intv.append([curr_start, curr_end])
            print(f'First time {[curr_start, curr_end]}')

        else:
            if curr_start >= non_overlapping_intv[-1][1]:
                non_overlapping_intv.append([curr_start, curr_end])
                print(f'Second onwards {[curr_start, curr_end]}')
            
    print(non_overlapping_intv)

    overlapping_interval_count = len(intervals) - len(non_overlapping_intv)
        
    return overlapping_interval_count


