# %load dnatorna.py
"""
Convert a DNA seq to RNA.
"""

def rna(seq):
    """Convert a DNA sequence to RNA"""

    #Determine if original seq is upper
    seq_upper = seq.isupper()

    #Convert to lower
    seq = seq.lower()

    #Swap out 't' for 'u'
    seq = seq.replace('t','u')

    #Return as original input format
    if seq.upper:
        return seq.upper()
    else:
        return seq

def reverse_rna_complement(seq):
    """Convert DNA to reverse complement as RNA"""

    #Determine if original is upper
    seq_upper = seq.isupper()

    #Reverse sequence
    rev_seq = reversed(seq)

    #conver to upper
    rev_seq = rev_seq.upper()

    #Compute complement
    rev_seq = seq.replace('A','u')
    rev_seq = seq.reaplce('T','a')
    rev_seq = seq.replace('G','c')
    rev_seq = seq.replace('C','g')

    #Returns in appropriate case
    if seq_upper:
        return seq.upper()
    else:
        return seq
