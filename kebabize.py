def kebabize(string):
    """If a letter is capital, insert a -"""
    kebab = ""
    for letter in string:
        if letter.isdigit():
            continue
        elif letter.isupper():
            kebab+=("-" + letter.lower())
        else:
            kebab+=letter
    return kebab if kebab[0] != "-" else kebab[1:]


print(kebabize("CamelsHave3ThreeHumps"))


def kebabize(string):
    # your code here
    kebab = ""
    for i in string:
        if i.isalpha():
            if i.isupper():
                kebab += '-' + i.lower()
            else:
                kebab += i
    if len(kebab) > 0:
        return kebab if kebab[0] != '-' else kebab[1:]
    else:
        return ''

def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')