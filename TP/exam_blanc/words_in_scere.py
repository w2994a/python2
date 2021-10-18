"""Extract words of two letters of DNA sequence in FASTA file.

Usage:
======
    python words_in_scere.py NC_001133.fna

    fasta_name: Name FASTA file
"""
__author__ = "William Amory"
__date__ = "2021-09_18"

import os
import sys


def read_fasta(fasta_name):
    """Extract sequence in FASTA file NC_001133.fna.

    Fonction permettant d'extraire la séquence d'ADN d'un fichier FASTA
    contenant une seul séquence d'ADN.

    Parameters
    ----------
    fasta_name : str
        Name FASTA file.

    Returns
    -------
    seq : str
        DNA sequence in FASTA file.
    """
    if not os.path.exists(fasta_name):
        sys.exit(f"{fasta_name} don't exist")
    with open(fasta_name, "r") as filin:
        seq = ""
        for line in filin:
            if line.startswith(">"):
                continue
            seq += line.strip()
    return seq


def count_words(seq):
    """Count words of two letters in DNA séquence.

    Parameters
    ----------
    seq : str
        DNA sequence

    Returns
    -------
    occur_words : dict
        Dictionnary of extract words and occurences.
    """
    occur_words = {}
    for i in range(len(seq)-1):
        word = seq[i:i+2]
        occur_words[word] = occur_words.get(word, 0) + 1
    return occur_words


if __name__ == "__main__":
    sequence = read_fasta("NC_001133.fna")
    word_dict = count_words(sequence)
    for word_2_letters, nb_word in word_dict.items():
        print(f"{word_2_letters} : {nb_word:>3d}")
   