string = 'This is a test string'
string = string.casefold()

words = string.split()
print('Original Unsorted String : {}'.format(words))

words.sort()
print('Sorted String : {}'.format(words))

file = open('/home/ubuntu/Desktop/Test.txt', 'w')
for i in words:
    file.write(i)

file.close()
