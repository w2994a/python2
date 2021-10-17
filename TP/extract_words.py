""" Script d'extraction de mots de n lettres dans une séquence.

Usage:
======

    python extract_word.py argument1 argument2
    
    argument1: Fichier FASTA
    argument2: Longueur des mots
    
    ou pour une utilisation en module: import extract_word
"""

import os
import sys


def lit_fasta(name_file):
    """ Extraction d'un séquence ADN d'un fichier FASTA.
    
    Fonction permettant d'extraire une séquence d'ADN d'un fichier au format
    FASTA qui contient une seule séquence d'ADN.
    
    Parameters
    ----------
    name_file : str
        Nom du fichier FASTA.
    
    Returns
    -------
    seq : str
        Séquence ADN du fichier FASTA.
    """
    
    if not os.path.exists(name_file):
        sys.exit(f"{name_file} don't exist")
    with open(name_file, "r") as filin:
        seq = ""
        for line in filin:
            if line.startswith(">"):
                continue
            seq += line.strip()
    return seq


def compt_mot_n_lettres(seq, nb_lettres):
    """ Compte les mots de n lettres.
    
    Fonction qui permet d'extraire et de compter les mots de n lettres d'un
    séquence d'ADN ou d'un séquence protéique.
    
    Parameters
    ----------
    seq : str
        Séquence d'ADN ou d'aa.
    nb_lettres : int
        Taille des mots à extraire.
    
    Returns
    -------
    occur_mot_lettres : dict
        Dictionnaire des mots extraits et de leurs nombres d'occurences.
    """
    
    occur_mot_lettres = {}
    for i in range(len(seq)-(nb_lettres-1)):
        mot = seq[i:i+nb_lettres]
        occur_mot_lettres[mot] = occur_mot_lettres.get(mot, 0) + 1
    return occur_mot_lettres


def affichage_mots_in_seq(mot_dict, nb_lettres):
    """ Affichage des mots et occurences d'un dictionnaire
    
    Fonction qui affiche les mots de n lettres et leurs occurences dans
    un dictionnaire.
    
    Parameters
    ----------
    mot_dict : dict
        Dictionnaire de mots et leurs occurences.
    nb_lettres : int
        Taille des mots présents dans le cictionnaire.
    """
    
    print(f"Mots de {nb_lettres} lettres")
    for mot, nb_mot in mot_dict.items():
        print(f"{mot} : {nb_mot:>5d}")
    return


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Missing arguments")
    if len(sys.argv) > 3:
        sys.exit("To much arguments")
    name_file = sys.argv[1]
    if not os.path.exists(name_file):
        sys.exit(f"{name_file} don't exist")
    try :
        taille_mots = int(sys.argv[2])
    except:
        sys.exit("Second argument must be an integer")
    
    seq_adn = lit_fasta(name_file)
    mot_dict = compt_mot_n_lettres(seq_adn, taille_mots)
    affichage_mots_in_seq(mot_dict, taille_mots)