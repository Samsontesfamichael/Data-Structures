/*
 * Numeric Algorithms Implementation in C
 * Includes: Primality test, base conversions, GCD, factorial, etc.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>

// 9.1 Primality Test
bool is_prime(int n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    
    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) return false;
    }
    
    return true;
}

void sieve_of_eratosthenes(int limit, int* primes, int* count) {
    if (limit < 2) {
        *count = 0;
        return;
    }
    
    bool* is_prime_arr = (bool*)malloc((limit + 1) * sizeof(bool));
    for (int i = 0; i <= limit; i++) {
        is_prime_arr[i] = true;
    }
    is_prime_arr[0] = is_prime_arr[1] = false;
    
    for (int i = 2; i <= sqrt(limit); i++) {
        if (is_prime_arr[i]) {
            for (int j = i * i; j <= limit; j += i) {
                is_prime_arr[j] = false;
            }
        }
    }
    
    *count = 0;
    for (int i = 2; i <= limit; i++) {
        if (is_prime_arr[i]) {
            primes[(*count)++] = i;
        }
    }
    
    free(is_prime_arr);
}

// 9.2 Base Conversions
void decimal_to_base(int number, int base, char* result) {
    if (number == 0) {
        strcpy(result, "0");
        return;
    }
    
    char digits[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char temp[100];
    int index = 0;
    bool negative = number < 0;
    number = abs(number);
    
    while (number > 0) {
        temp[index++] = digits[number % base];
        number /= base;
    }
    
    int result_index = 0;
    if (negative) result[result_index++] = '-';
    
    for (int i = index - 1; i >= 0; i--) {
        result[result_index++] = temp[i];
    }
    result[result_index] = '\0';
}

int base_to_decimal(const char* number_str, int base) {
    char digits[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int result = 0;
    int power = 0;
    int len = strlen(number_str);
    bool negative = (number_str[0] == '-');
    int start = negative ? 1 : 0;
    
    for (int i = len - 1; i >= start; i--) {
        char c = number_str[i];
        if (c >= 'a' && c <= 'z') c -= 32; // Convert to uppercase
        
        char* pos = strchr(digits, c);
        int value = pos - digits;
        result += value * pow(base, power++);
    }
    
    return negative ? -result : result;
}

// 9.3 Greatest Common Denominator (GCD)
int gcd(int a, int b) {
    a = abs(a);
    b = abs(b);
    
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    
    return a;
}

int gcd_recursive(int a, int b) {
    a = abs(a);
    b = abs(b);
    
    if (b == 0) return a;
    return gcd_recursive(b, a % b);
}

int lcm(int a, int b) {
    return abs(a * b) / gcd(a, b);
}

// 9.4 Maximum value for base N with D digits
long long max_value_for_base(int base, int num_digits) {
    return (long long)pow(base, num_digits) - 1;
}

// 9.5 Factorial
long long factorial(int n) {
    if (n < 0) return -1; // Error
    
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    
    return result;
}

long long factorial_recursive(int n) {
    if (n < 0) return -1;
    if (n == 0 || n == 1) return 1;
    
    return n * factorial_recursive(n - 1);
}

// Additional: Fibonacci
long long fibonacci(int n) {
    if (n < 0) return -1;
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    long long a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        long long temp = a + b;
        a = b;
        b = temp;
    }
    
    return b;
}

// Additional: Fast Exponentiation
long long power(long long base, int exponent) {
    if (exponent == 0) return 1;
    
    bool negative = exponent < 0;
    exponent = abs(exponent);
    
    long long result = 1;
    long long current_power = base;
    
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result *= current_power;
        }
        current_power *= current_power;
        exponent /= 2;
    }
    
    return negative ? 1.0 / result : result;
}

// Main function for testing
int main() {
    printf("=== Numeric Algorithms Demo (C) ===\n\n");
    
    // Primality Test
    printf("1. Primality Test:\n");
    int test_numbers[] = {2, 3, 4, 17, 20, 29, 100, 97};
    for (int i = 0; i < 8; i++) {
        printf("  %d is %s\n", test_numbers[i], 
               is_prime(test_numbers[i]) ? "prime" : "not prime");
    }
    
    int primes[100];
    int count;
    sieve_of_eratosthenes(50, primes, &count);
    printf("\n  Primes up to 50: ");
    for (int i = 0; i < count; i++) {
        printf("%d ", primes[i]);
    }
    printf("\n");
    
    // Base Conversions
    printf("\n2. Base Conversions:\n");
    char result[100];
    decimal_to_base(255, 2, result);
    printf("  255 in binary: %s\n", result);
    decimal_to_base(255, 16, result);
    printf("  255 in hexadecimal: %s\n", result);
    decimal_to_base(255, 8, result);
    printf("  255 in octal: %s\n", result);
    
    printf("  Binary 11111111 to decimal: %d\n", base_to_decimal("11111111", 2));
    printf("  Hex FF to decimal: %d\n", base_to_decimal("FF", 16));
    
    // GCD and LCM
    printf("\n3. GCD and LCM:\n");
    printf("  GCD(48, 18) = %d\n", gcd(48, 18));
    printf("  GCD(100, 75) = %d\n", gcd(100, 75));
    printf("  LCM(12, 18) = %d\n", lcm(12, 18));
    
    // Maximum value for base
    printf("\n4. Maximum Value for Base:\n");
    printf("  Max value for base 10, 3 digits: %lld\n", max_value_for_base(10, 3));
    printf("  Max value for base 2, 8 digits: %lld\n", max_value_for_base(2, 8));
    printf("  Max value for base 16, 2 digits: %lld\n", max_value_for_base(16, 2));
    
    // Factorial
    printf("\n5. Factorial:\n");
    for (int i = 0; i <= 10; i++) {
        printf("  %d! = %lld\n", i, factorial(i));
    }
    
    // Fibonacci
    printf("\n6. Fibonacci Sequence:\n");
    printf("  First 15 Fibonacci numbers: ");
    for (int i = 0; i < 15; i++) {
        printf("%lld ", fibonacci(i));
    }
    printf("\n");
    
    // Fast Exponentiation
    printf("\n7. Fast Exponentiation:\n");
    printf("  2^10 = %lld\n", power(2, 10));
    printf("  5^3 = %lld\n", power(5, 3));
    
    return 0;
}
