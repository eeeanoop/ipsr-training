# the program should tell if two strings are anagram of each other

def check_anagram_using_sort(string1: str, string2: str ) -> bool:
    """
    sorted = nlog(n)
    :param string1:
    :param string2:
    :return:

    required : (n)

    """
    return sorted(string1) == sorted(string2)


def check_anagram_using_dict(string1: str, string2: str) -> bool:
    """

    :param string1:
    :param string2:
    :return:
    { 'l':1, 'i':2}


    """
    if len(string1) != len(string2):
        return False

    char_dict = {}
    for input_char in string1:
        char_dict[input_char] = char_dict.get(input_char,0)+ 1

    for input_char in string2:
        if input_char not in char_dict:
            return False
        else:
            char_dict[input_char]-=1

    is_anagram = True
    for key, value in char_dict.items():
        if value != 0:
            is_anagram = False
    print(f'char_dict:{char_dict}')

    return is_anagram

# Comment the time
def check_anagram_using_oridinal(string1: str, string2: str):
    pass

if __name__ == '__main__':
    print('Start')
    print(check_anagram_using_dict('listen', 'silent'))
