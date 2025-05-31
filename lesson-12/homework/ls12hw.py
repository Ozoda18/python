import concurrent.futures
import math

def prime_number(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    return [n for n in range(start, end) if prime_number(n)]

def main():
    start_range = 1
    end_range = 100000
    num_threads = 8
    chunk_size = (end_range - start_range) // num_threads

    ranges = [(start_range + i * chunk_size, start_range + (i + 1) * chunk_size) for i in range(num_threads)]

    ranges[-1] = (ranges[-1][0], end_range)

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        

        futures = [executor.submit(find_primes_in_range, r[0], r[1]) for r in ranges]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
        primes = [prime for sublist in results for prime in sublist]

    
    print(f"Prime numbers between {start_range} and {end_range}:")
    print(primes)

if __name__ == "__main__":
    main()
    
print(1);











