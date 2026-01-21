
# nums = [1,1,1,2,2,3,3,3,3]. k=2.   Find the TopK Frequent elements
# Really hard to sort the values of a Dict


from collections import defaultdict
def find_most_fequent(l :[int], k :int):
    result = []
    temp_dict = defaultdict(int)
    for i in l:
        temp_dict[i ]+ =1
        print(i)
    tem_list = [[] for _ in range(len(l))]


    for i, j in temp_dict.items():
        tem_list[j].append(i)
        print(f'Key: {i}, Value: {j}')

    for i in reversed(tem_list):
        if len(i) != 0:
            result = result + i
            print(f' List Values: {i}')

    print(result[:k])


if __name__ == "__main__":
    nums = [1 ,1 ,1 ,2 ,2 ,3 ,3 ,3 ,3] k=2
    find_most_fequent(nums, k)