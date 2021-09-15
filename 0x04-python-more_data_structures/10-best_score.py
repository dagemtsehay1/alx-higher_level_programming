#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = 0
        best = ""
        for k, score in a_dictionary.items():
            if score > max_score:
                max_score = score
                best = k
        return best
