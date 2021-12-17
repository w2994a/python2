"""Script permettent de trouver la séquence conssensus d'un fichier FASTA.

Usage:
======
    Python consensus <file_name>
    
    argument <file_name>: Fichier de séquences au format FASTA.
"""

__authors__ = "William Amory"
__date__ = "2021-12-17"

import os
import sys
from Bio import Seq, SeqIo

def get_argument():
    """Fonction renvoyant le nom du fichier.

    Returns
    -------
        file_name : str
            nom du fichier donné en 1er argument.
    """
    if len(sys.argv) > 2:
        sys.exit("Too much arguments !")
    elif len(sys.argv) < 2:
        sys.exit("FASTA file is missing!")
    return sys.argv[1]


def extract_seq(file_name):
    """"Fonction qui parse le fichier donné en argument.

    Parameters
    ----------
    file_name : str
        Nom du fichier a parser.

    Returns
    -------
    dict_seq : dict
        Dictionnaire des séquences du fichier.
    length : int
        Longueur des séquences.
    """
    dict_seq : {}
    with open(file_name, "r") as f_in:
        dict_seq = SeqIo.parse(file_name, "fasta")
    print(f"Found {len(dict)} sequences")
    print(f"Sequences : {length dict_sec[0]['Length']}") 
    return dict_seq, dict_sec[0]["Length"]


def count_bases(dict_seq, len_seq):
    """Fonction comptant le nombre de bases par position.

    Parameters
    ----------
    dict_seq : dict
        dictionnaire des sequences.
    len_seq : int
        longueur des séquences.

    Returns
    -------
    seq_count : dict
        Dictionnaire des counts.
    """
    seq_count = {"A" : [], "T" : [], "C" : [], "G" : []}
    for i in range(len_seq):
        bases = {"A": 0, "T": 0, "C": 0, "G": 0}
        for sequence in dict_seq:
            bases[sequence["Seq"][i]] += 1
        for base in bases:
            bases[base] = bases[base] / len(dict_seq)
            seq_count[base].append(bases[base])
    return seq_count


def build_consensus(seq_count, len_seq):
    """Fonction qui créer la séquence consensus.
    
    Parameters
    ----------
    seq_count : dict of list of float
        Dictionnaire de la fréquences des bases pour chaque
        position.
    len_seq : int
        Longueur des séquences du fichier.
    """
    seq_consensus = ""
    for i in range(len(len_seq)):
        freq_pos = [seq_count["A"][i], seq_count["T"][i],
                   seq_count["C"][i], seq_count["G"][i]]
        if freq_pos.index(max(freq_pos)) == 0:
            seq_consensus += "A"
        elif freq_pos.index(max(freq_pos)) == 1:
            seq_consensus += "A"
        elif freq_pos.index(max(freq_pos)) == 2:
            seq_consensus += "C"
        elif freq_pos.index(max(freq_pos)) == 3:
            seq_consensus += "G"
    return seq_consensus


if __name__ == "__main__":
    
    file_name = get_argument()
    dict_seq, len_seq = extract_seq(file_name)
    dict_count = count_bases(dict_sec, len_seq)
    seq_consensus = build_consensus(dict_count, len_seq)
    print(f"Consensus sequence : {seq_consensus}")