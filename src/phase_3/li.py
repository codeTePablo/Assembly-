my_list = ['[DX', 'SI]']
joined_string = ' '.join(my_list)
result = joined_string[joined_string.index('[')+1:joined_string.index(']')]
print(result)
