#Prevent Overwrite
import os
if os.path.exists('numbers.file'):
    os.remove('numbers.file')
else:
    print("The file doesn't exist at all")

if os.path.exists('numbers_updated.file'):
    os.remove('numbers_updated.file')
else:
    print("The file doesn't exist at all")

if os.path.exists('alphabet.file'):
    os.remove('alphabet.file')
else:
    print("The file doesn't exist at all")

if os.path.exists('ABC123.file'):
    os.remove('ABC123.file')
else:
    print("The file doesn't exist at all")

#Repeating Numbers
with open('numbers.file', 'w') as file:
    file.write("1 \n1 \n1 \n1 \n2 \n2 \n2 \n3 \n3 \n4 \n5 \n6 \n7 \n8 \n9 \n10")
file.close()

with open('alphabet.file', 'w') as file:
    file.write("A \nB \nC \nD \nE \nF \nG \nH \nI \nJ \nK \nL \nM \nN \nO \nP \nQ \nR \nS \nT \nU \nV \nW \nX \nY \nZ")
file.close()

#Original
with open('numbers.file', 'r') as file:
    print("In one line: ")
    cont = file.readlines()
    print(cont)
file.close()

#Split
with open('numbers.file', 'r') as file:
    print("In several lines: ")
    cont = file.readlines()
    for line in cont:
        word = line.split()
        print(word)
file.close()

#Remove Repeated Numbers
input_file = open('numbers.file', 'r')
output_file = open('numbers_updated.file', 'w')

original_lines = set()

for line in input_file:
    if line not in original_lines:
        output_file.write(line)
        original_lines.add(line)

input_file.close()
output_file.close()

with open('numbers_updated.file', 'r') as file:
    print("Remove repeated numbers: ")
    cont = file.readlines()
    for line in cont:
        word = line.split()
        print(word)
file.close()

file1 = open('numbers_updated.file', 'r')
numbers = file1.read()
file1.close()

file2 = open('alphabet.file', 'r')
letters = file2.read()
file2.close()

ABC123 = numbers + "\n" + letters
print(ABC123)

file3 = open('ABC123.file', 'w')
file3.write(ABC123)
file3.close()




