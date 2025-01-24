#!/usr/bin/env python3
import string


def hex_to_byte(hex_byte: str) -> str:
    """
    Converts a hex value to an 8-bit binary string.
    :param hex_byte: A hex value represented as a string.
    :return: A string representing the converted byte with exactly 8 bits in length.
    """
    return f"{int(hex_byte, 16):08b}"

def hex_string_to_bytes(hex_string: str) -> str:
    """
    Converts a string of hex values to a binary string.
    :param hex_string: A string of hexadecimal values to be converted to bytes.
    :return: A binary string representation of the hex input.
    """
    if len(hex_string) % 2 != 0:
        raise ValueError("Hex string must have an even length.")
    return ''.join(hex_to_byte(hex_string[i:i+2]) for i in range(0, len(hex_string), 2))

def bytes_to_base64(bytes_string: str) -> str:
    """
    Encodes a binary string to a base64 string.
    :param bytes_string: A binary string to encode.
    :return: A base64-encoded string.
    """
    base64_lookup = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/")
    if len(bytes_string) % 6 != 0:
        bytes_string = bytes_string.ljust((len(bytes_string) + 5) // 6 * 6, '0')
    return ''.join(base64_lookup[int(bytes_string[i:i+6], 2)] for i in range(0, len(bytes_string), 6))

def main():
    test_hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    binary_string = hex_string_to_bytes(test_hex_string)
    base64_output = bytes_to_base64(binary_string)
    assert base64_output == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    print(base64_output)

if __name__ == "__main__":
    main()
