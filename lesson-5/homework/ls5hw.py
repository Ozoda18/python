leap_year=100
if (leap_year%4==0 and  leap_year%100!=0) or (leap_year%400==0):
        print(True)
else:
    print(False);

n=8
if n%2!=0:
      print('weird')
elif n%2==0:
    if  2<n<5:
      print('not weird')
    elif 6<n<20:
         print('weird')
    elif  n<20:
         print('not weird');

def find_even_numbers(a, b):

    if a % 2 != 0:
        a += 1
        return list(range(a, b + 1, 2))

a = 3
b = 15
even_numbers = find_even_numbers(a, b)
print(even_numbers);