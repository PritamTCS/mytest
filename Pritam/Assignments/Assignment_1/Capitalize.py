import string
import collections

file = open('/home/ubuntu/Desktop/test2.txt', 'r')
x = file.read().splitlines()
print(x)

list3 = []

for i in range(len(x)):
    
    list2 = x[i].split()
    list3.extend(list2)
    

print('Lists: ',list3)
d = collections.Counter(list3)
print(dict(d))
print(' ')


for line in x:
    print('Original content: ',line)
    print('Capitalized each Word: ',string.capwords(line))
    list1 = line.split()
    print(list1)
    for i in list1:
        print('Length of each word ', len(i))
                   
                    
    print('Count of words in each line: ', len(list1))
    c = collections.Counter(list1)
    print(dict(c))
    print(' ')


file.close()
    
    

        

    
