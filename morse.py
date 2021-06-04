#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Bethany Folino with help from Jacob Short'

from morse_dict import MORSE_2_ASCII
from morse_dict import bits_2_morse


def decode_bits(bits):
    bits = bits.strip("0")
    bit_list = []
    result_list = []
    bit_string = ""
    result_string = ""
    min_len = 999999
    for bit in bits:
        if not bit_string and bit == "1":
            bit_string += bit
        elif bit == bit_string[-1]:
            bit_string += bit
        else:
            bit_list.append(bit_string)
            bit_string = bit
    bit_list.append(bit_string)

    # smallest string length
    for bit in bit_list:
        if len(bit) < min_len:
            min_len = len(bit)
    # divide each word by multiplier
    for ele in bit_list:
        division = len(ele) / float(min_len)
        c = [ele[int(round(division * i)):
             int(round(division * (i + 1)))] for i in range(min_len)]
        result_list.append(c[0])

    for result in result_list:
        if result in bits_2_morse:
            morse = bits_2_morse.get(result)
            result_string += morse
    return result_string


def decode_morse(morse):
    result = ""
    for word in morse.split("   "):
        for char in word.split():
            if char in MORSE_2_ASCII:
                decode = MORSE_2_ASCII.get(char)
                result += decode
        result += " "
    return result.strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
