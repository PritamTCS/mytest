string = input("Enter an alphanumeric string: ")

letters =0
digits = 0

for s in string:
    if s.isalpha():
        letters = letters + 1

    elif s.isdigit():
        digits = digits + 1

    else: pass


print('Letters: ', letters)
print('digits: ', digits)
        
