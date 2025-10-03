def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    
    else:
        for i in range(3,num-1):
            if num % i == 0:
                return False
        return True

# chat gpt                
def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # any even number greater than 2 is not prime
        return False
    
    # Only check divisors up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Example usage
print(is_prime(73))  # True
print(is_prime(75))  # False