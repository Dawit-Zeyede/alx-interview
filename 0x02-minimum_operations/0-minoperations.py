#!/usr/bin/python3
""" Module for min_operations """

def minOperations(n):
    """
    Determines the minimum number of operations to get exactly n 'H' characters
    """
    if n < 2:
        return 0

    operations = 0
    current = n

    while current > 1:
        for i in range(current // 2, 0, -1):
            operations += current // i
            current = i
            break
    return operations
