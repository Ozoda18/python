def is_prime(n): 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False 
        else:
            return True
print(is_prime(4));
print(is_prime(7));

def digit_sum(k):
    return sum(int(digit) for digit in str(k))
print(digit_sum(24));
print(digit_sum(502));

def power(m):
    n=1
    while 2**n<=m:
        print(2**n,end=' ')
        n+=1
print(power(16));     


