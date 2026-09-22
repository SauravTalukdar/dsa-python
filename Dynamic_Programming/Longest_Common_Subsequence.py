# We are given two sequences,we need to find the length of the longest common subsequence.
# QUESTION: Write a function to find the length of the longest common subsequence between two sequences.
# E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence 
# is "reipito" and its length is 7.

# A "sequence" is a group of items with a deterministic ordering.
# Lists, tuples and ranges are some common sequence types in Python.
# A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence. 
# For example, "edpt" is a subsequence of "serendipitous".

#test cases
# General case (string)
# General case (list)
# No common subsequence
# One is a subsequence of the other
# One sequence is empty
# Both sequences are empty
# Multiple subsequences with same length
# “abcdef” and “badcfe”
T0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}

T1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

T2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}

T3 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T4 = {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
}

T5 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}

T7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}