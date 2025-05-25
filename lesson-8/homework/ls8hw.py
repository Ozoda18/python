a=10
b=0
try:
    a/b
except ZeroDivisionError:
    print('can not be divided by 0');
  
try:
    a=int(input())
except ValueError:
    print('error');

try:
     with open('some.txt') as file:
            print('some.txt')
except FileNotFoundError:
        print('file was not found.');

try:
    a=int(input())
    b=int(input())
except TypeError:    
     print('is not true');

try:
     with open('some.txt') as file:
            print('some.txt')
except FileNotFoundError:
        print('file was not found.')
except PermissionError:
    print('permission denied');

try:
     lst=[1,2,3,4,5,6]
     index=lst[20]
     print(index)
except IndexError:
          print('out of range');  

try:
    num = int(input())
    print(num)
except KeyboardInterrupt:
    print("\nInput was cancelled by the user.");

try:
    a=8
    b=4
    r=a/b
    print(r)
except ArithmeticError:
     print('there is an arithmetic error');

try:
     with open('some.txt') as file:
          print('some.txt')
except UnicodeDecodeError:
     print('unable to decode');

nums = [1, 2, 3, 4, 5]
try:
    r1 = nums.lengtha
    print(r1)
except AttributeError:
    print('does not exist');

myfile=open('some.txt','r')
print(myfile.read())
myfile.close();

myfile=open('some.txt','r')
print(myfile.readlines(3))
myfile.close();

with open('some.txt','a') as f:
    f.write('how are you?');

myfile=open('some.txt','r')
print(myfile.readlines(-3))
myfile.close();

myfile.readlines();

for i in myfile.readlines():
     print(i);

sentence = input()
try:
    words = sentence.split()
    longest = max(words, key=len)
    print(longest)
except ValueError:
    print(" empty");


with open('some.txt', 'r') as file:
        line_count = sum(1 for line in file)
        print(line_count);

with open('some.txt','w') as file:
     file.write(['hello', 'wazzup']);
   
import string   
for letter in string.ascii_uppercase:
    
    with open(f"{letter}.txt", "w") as file:
        file.write(letter)
    print(f"Created {letter}.txt");

import string

def create_alphabet_file(letters_per_line, filename="alphabet.txt"):
    
    alphabet = string.ascii_uppercase

    
    with open(filename, 'w') as file:
        
        for i in range(0, len(alphabet), letters_per_line):
            
            file.write(alphabet[i:i + letters_per_line] + '\n')

    print(f"Alphabet written to {filename} with {letters_per_line} letters per line.");




             

  


     
           


     