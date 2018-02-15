def reverse(string):
    return string[::-1]

def check_palindrome(string):
    rev = reverse(string)

    if (string == rev):
        return 1
    else:
        return 0


if __name__ == '__main__':
        string = 'aubuA'
        string = string.casefold()
        res = check_palindrome(string)

        if res == 1:
            print('Yes')
        else:
            print('No')
