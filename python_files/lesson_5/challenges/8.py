from itertools import count


def replace(text='', target=None, replace=None):

    while True:
        if target not in text: 
            return text
        else:
            text.replace(target, replace)


new_txt = replace('hello world', 'hello', 'hi')
print(new_txt)