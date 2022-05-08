#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for i in sorted(a_dictionary):
            if a_dictionary[i] == max(list(a_dictionary.values())):
                return i
    else:
        return None
