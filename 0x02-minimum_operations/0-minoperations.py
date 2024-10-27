#!/usr/bin/python3
"""Minimum Operations"""
def minOperations(n):
    """using dynamic programming to create minimum operations"""
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    
    # Factorize n, adding the prime factors to operations
    while n > 1:
        # Check if the current divisor divides n
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
        
    return operations