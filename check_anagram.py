# the program should tell if two strings are anagram of each other



def check_anagram(string1: str, string2: str ) -> bool:
    return sorted(string1) == sorted(string2)


if __name__ == '__main__':
    print('Start')
    print(check_anagram('listen', 'silnt'))
