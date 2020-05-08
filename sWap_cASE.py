def swap_case(s):
    result = ""
    for letters in s:
        if letters.islower():
            letters = letters.upper()
            result = result + "".join(letters)
        else:
            letters = letters.lower()
            result = result + "".join(letters)

    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)