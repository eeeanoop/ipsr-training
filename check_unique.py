

def check_dupes(input_num_list):
    return len(input_num_list) == len(set(input_num_list))

def check_dupe_with_set(input_num_list):

    empty_list = []
    empty_tuple = ()
    empty_dict = {}
    temp_set = set()
    dupe_flag = False
    for num in input_num_list:
        if num in temp_set:
            dupe_flag = True
        else:
            temp_set.add(num)
    return dupe_flag

"""

"""


if __name__ == "__main__":
    input_list = [1, 2, 3]
    print(f' Result: {check_dupe_with_set(input_list)}')
