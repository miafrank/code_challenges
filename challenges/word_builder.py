import functools
import operator

# Given an array of characters ['a', 'b', 'c', 'd']
# return all string combinations (ex: ['ab', 'ac', 'ba'...])


def word_builder(chars):
    return list(map(lambda x: functools.reduce(operator.add, x), chars))
