# Write a program to encode strings and decode
# 

# input = =["I", "2am", "a", "programmer"]
def encode(input_string: list[str]) -> str:
  result:list[str] = []
  for word in input_string:
    word_length = str(len(word))
    delimiter_char = '#'
    result.append(word_length)
    result.append(delimiter_char)
    result.append(word)
    result_string = "".join(result)
  return result_string

def decode(input_string: str) -> list[str]:
  # 7#awesome6#python8#language
  # i = 0
  # j = 0
  # Determine word length
  # j = 1
  # word_length = input_string[0:1] = 7
  # i = 9, j = 9
  # j = 8
  
  i = 0
  result: list[str] = []
  while i < len(input_string):
    j = i
    while not input_string[j] == '#':
      j += 1
    word_length = input_string[i:j]
    word = input_string[j+1: (j+1) + int(word_length)]
    i +=  int(len(word_length)) + 1 + int(word_length)
    result.append(word)
  return result
    
      
   


encoded_string = encode(['awesome','python','language'])
print(encoded_string)
print(decode(encoded_string))
  

