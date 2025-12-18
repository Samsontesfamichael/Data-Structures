"""
Numeric Algorithms Implementation
Includes: Primality test, base conversions, GCD, factorial, etc.
"""

import math

# 9.1 Primality Test
def is_prime(n):
    """
    Check if a number is prime - O(√n) time
    A prime number is only divisible by 1 and itself
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to √n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def sieve_of_eratosthenes(limit):
    """
    Find all primes up to limit - O(n log log n) time
    More efficient for finding multiple primes
    """
    if limit < 2:
        return []
    
    # Create boolean array, initially all True
    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime_arr[i]:
            # Mark all multiples as not prime
            for j in range(i * i, limit + 1, i):
                is_prime_arr[j] = False
    
    # Collect all prime numbers
    return [i for i in range(limit + 1) if is_prime_arr[i]]


# 9.2 Base Conversions
def decimal_to_base(number, base):
    """
    Convert decimal number to any base (2-36) - O(log n) time
    """
    if number == 0:
        return "0"
    
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    negative = number < 0
    number = abs(number)
    
    while number > 0:
        remainder = number % base
        result.append(digits[remainder])
        number //= base
    
    if negative:
        result.append('-')
    
    return ''.join(reversed(result))


def base_to_decimal(number_str, base):
    """
    Convert number from any base to decimal - O(n) time
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_str = number_str.upper()
    
    result = 0
    power = 0
    
    for digit in reversed(number_str):
        if digit == '-':
            result = -result
        else:
            value = digits.index(digit)
            if value >= base:
                raise ValueError(f"Invalid digit '{digit}' for base {base}")
            result += value * (base ** power)
            power += 1
    
    return result


# 9.3 Greatest Common Denominator (GCD)
def gcd(a, b):
    """
    Euclidean algorithm for GCD - O(log min(a,b)) time
    """
    a, b = abs(a), abs(b)
    
    while b != 0:
        a, b = b, a % b
    
    return a


def gcd_recursive(a, b):
    """
    Recursive version of GCD
    """
    a, b = abs(a), abs(b)
    
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def lcm(a, b):
    """
    Least Common Multiple using GCD - O(log min(a,b)) time
    LCM(a,b) = (a * b) / GCD(a,b)
    """
    return abs(a * b) // gcd(a, b)


# 9.4 Maximum value for base N with D digits
def max_value_for_base(base, num_digits):
    """
    Compute maximum value for a number of specific base with N digits
    For base B with D digits: (B^D) - 1
    Example: Base 10, 3 digits = 999 = (10^3) - 1
    """
    if base < 2:
        raise ValueError("Base must be at least 2")
    if num_digits < 1:
        raise ValueError("Number of digits must be at least 1")
    
    return (base ** num_digits) - 1


# 9.5 Factorial
def factorial(n):
    """
    Iterative factorial - O(n) time, O(1) space
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def factorial_recursive(n):
    """
    Recursive factorial - O(n) time, O(n) space
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)


def factorial_memoized(n, memo=None):
    """
    Memoized factorial for better performance with repeated calls
    """
    if memo is None:
        memo = {}
    
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 1
    
    memo[n] = n * factorial_memoized(n - 1, memo)
    return memo[n]


# Additional numeric algorithms
def fibonacci(n):
    """
    Compute nth Fibonacci number - O(n) time, O(1) space
    """
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


def power(base, exponent):
    """
    Fast exponentiation using binary method - O(log n) time
    """
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    
    result = 1
    current_power = base
    
    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_power
        current_power *= current_power
        exponent //= 2
    
    return result


# Example usage and testing
if __name__ == "__main__":
    print("=== Numeric Algorithms Demo ===\n")
    
    # Primality Test
    print("1. Primality Test:")
    test_numbers = [2, 3, 4, 17, 20, 29, 100, 97]
    for num in test_numbers:
        print(f"  {num} is {'prime' if is_prime(num) else 'not prime'}")
    
    print(f"\n  Primes up to 50: {sieve_of_eratosthenes(50)}")
    
    # Base Conversions
    print("\n2. Base Conversions:")
    print(f"  255 in binary: {decimal_to_base(255, 2)}")
    print(f"  255 in hexadecimal: {decimal_to_base(255, 16)}")
    print(f"  255 in octal: {decimal_to_base(255, 8)}")
    print(f"  Binary 11111111 to decimal: {base_to_decimal('11111111', 2)}")
    print(f"  Hex FF to decimal: {base_to_decimal('FF', 16)}")
    
    # GCD and LCM
    print("\n3. GCD and LCM:")
    print(f"  GCD(48, 18) = {gcd(48, 18)}")
    print(f"  GCD(100, 75) = {gcd(100, 75)}")
    print(f"  LCM(12, 18) = {lcm(12, 18)}")
    
    # Maximum value for base
    print("\n4. Maximum Value for Base:")
    print(f"  Max value for base 10, 3 digits: {max_value_for_base(10, 3)}")
    print(f"  Max value for base 2, 8 digits: {max_value_for_base(2, 8)}")
    print(f"  Max value for base 16, 2 digits: {max_value_for_base(16, 2)}")
    
    # Factorial
    print("\n5. Factorial:")
    for i in range(0, 11):
        print(f"  {i}! = {factorial(i)}")
    
    # Additional algorithms
    print("\n6. Fibonacci Sequence:")
    print(f"  First 15 Fibonacci numbers: {[fibonacci(i) for i in range(15)]}")
    
    print("\n7. Fast Exponentiation:")
    print(f"  2^10 = {power(2, 10)}")
    print(f"  5^3 = {power(5, 3)}")
    print(f"  2^-3 = {power(2, -3)}")
