#Задача №2
#https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f

def alias_gen(f_name, l_name):
    if f_name[0].isalpha() and l_name[0].isalpha():
        return f'{FIRST_NAME[f_name[0].upper()]} {SURNAME[l_name[0].upper()]}'
    else:
        return 'Your name must start with a letter from A - Z.'

#     Выполнено
