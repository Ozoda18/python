num=[6,92,-12,8,61,9,-12]
print(sorted(num));

print(sorted(num,reverse=True));

given = {0: 10, 1: 20}
given.update({2: 30})  
print(given) ;

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1);

n =5
square= {}
for i in range(1, n + 1):
    square[i] = i * i
print(square);

n =15
square= {}
for i in range(1, n + 1):
    square[i] = i * i
print(square);

my_set={'John','Doe','Alice'}
for i in my_set:
    print(i);
my_set.add('Smith')
print(my_set);
my_set.remove('Smith')
print(my_set);
my_set.discard('Smith')
print(my_set)
