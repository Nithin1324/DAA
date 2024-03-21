def is_prime(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False   
    return is_prime(n, divisor + 1)

def generate_primes(n, current=2, primes=[]):
    if current > n:
        return primes
    if is_prime(current):
        primes.append(current)
    return generate_primes(n, current + 1, primes)
n=int(input())
prime_numbers = generate_primes(n)
print(f"The prime numbers up to are: {prime_numbers}") 
