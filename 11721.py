original_str = str(input())
result_str = ""

idx = 0

for each_char in original_str:
    if idx % 10 is 0 and idx is not 0:
        result_str += '\n'
    result_str += each_char
    idx += 1

print(result_str, end='')