#!/usr/bin/python3
""" utf8_validator.py"""
import sys

def validUTF8(data):
    """
    Validate if a given dataset represents a valid UTF-8 encoding.

    Parameters:
        data (list of int): List of integers where each integer is a byte (8 bits).

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.

    Raises:
        TypeError: If data is not a list or elements are not integers.

    Example:
        >>> validUTF8([197, 130, 1])
        True
        >>> validUTF8([235, 140, 4])
        False
    """
    num_bytes = 0
    
    # Masks to check leading bits in the byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Only consider the 8 least significant bits of each integer
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Determine the number of leading 1's
            mask = 1 << 7
            while (byte & mask):
                num_bytes += 1
                mask = mask >> 1
            
            # For a 1-byte character, num_bytes will be 0 after this
            if num_bytes == 0:
                continue
            
            # UTF-8 encoding must be 1 to 4 bytes
            if num_bytes == 1 or num_bytes > 4:
                return False
            
            # Subtract 1 to account for the current byte
            num_bytes -= 1
        else:
            # Check if it's a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False
            # Decrement the number of continuation bytes needed
            num_bytes -= 1

    return num_bytes == 0
