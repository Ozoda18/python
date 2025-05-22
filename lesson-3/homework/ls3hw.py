fruits=['apple','strawberry','banana','orange','cherry']
print(fruits[2]);

num1=[21,87,26,9,73]
num2=[31,65,98,2,7]
num1.extend(num2)
print(num1);

numbers=[11,96,63,2,10]
first=numbers[0]
middle=numbers[2]
last=numbers[-1]
print([first,middle,last]);

movies=['Go ahead','Driver','Baby driver','Butterfly','Sunset']
print(tuple(movies));

cities=['New York','Paris','Tokio','California','Seoul']
print('Paris' in cities);

numbs=[1,2,3,4,5]
doubled = [x * 2 for x in numbs]
print(doubled);

lst=[1,2,3,4,5,6,7,8,9]
lst[0]=41
lst[-1]=75
print(lst);

numbers=(1,2,3,4,5,6,7,8,9,10)
print(numbers[2:7]);

colors=['red','blue','orange','white','black','blue']
print(colors.count('blue'));

animals=('rabbit','cat','lion','monkey')
print(animals.index('lion'));

tuple1=(1,2,3,4,5)
tuple2=(6,7,8,9,10)
tuple1+=tuple2
print(tuple1);

lst=[5,6,'hello',9]
tuplee=(6,2,'zxc')
print(len(lst))
print(len(tuplee));

numbers=(1,2,3,4,5)
print(tuple(numbers));

numbers=(1,2,3,4,5)
print(max(numbers))
print(min(numbers));

word=('hello')
print(word[::-1]);





