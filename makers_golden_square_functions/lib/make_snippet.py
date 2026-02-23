def make_snippet(str):
    
    str_list = str.split(" ")
    str_list_shortened = str.split(" ")[0:5]
    new_str = ''
    for i in str_list_shortened:
        new_str += i
        new_str += ' '
    new_str = new_str[0:-1]
    if str_list_shortened != str_list:
        new_str += '...'
    print(new_str)
    return new_str