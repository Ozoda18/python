n=int(input())
for i in range(n):
    print(i**2);

number=10
while number<20:
    print(number)
    number+=1;

n=5
for i in range(1,n+1):
     for j in range(1,i+1):
         print(j, end='')
     print();

num=10
sum=0
for i in range(num+1):
    sum+=i
print(sum);

num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    print(i*2);

numbers=[12,75,150,145,525,50]
for number in numbers:
    if number==75:
         print(number)
    if number==150:
        print(number)
    if number==145:
        print(number) ;    
  
numbers=[75869]
for number in numbers:
    print(len(str(number)));

n=5
for i in range(n,0,-1):
     for j in range(i,0,-1):
         print(j, end='')
     print();

list1=[10,20,30,40,50]
for i in list1:
    print(list1[::-1])
    break;
 
for i in range(-10,0):
    print(i);

for i in range(0,5):
    print(i)
print('Done!');

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  
fibonacci_sequence(10);

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 5
print(f"The factorial of {num} is {factorial(num)}") ;

list1=[1,2,3]
list2=[4,5,6]
merged_list = []
for num in list1 + list2:
    if num not in merged_list:
        merged_list.append(num)

print(merged_list);



