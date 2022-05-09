#!/usr/bin/python3
def roman_to_int(roman_string):
    list_roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    s = 0
    if roman_string:
        for i in range(len(roman_string)):
            if roman_string[i] == 'I':
                if (roman_string[i + 1] == 'V' or roman_string[i + 1] == 'X'):
                    s = s - 1
                else:
                    s = s + 1
            elif roman_string[i] == 'V':
                s = s + 5
            elif roman_string[i] == 'X':
                s = s +10
            elif roman_string[i] == 'L':
                s = s + 50
            elif roman_string[i] == 'C':
                s = s + 100
            elif roman_string[i] == 'D':
                s = s + 500
            elif roman_string[i] == 'M':
                s = s + 1000
            else:
                s = s + 0
        return (s)
    else:
        return (0)
