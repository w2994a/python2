import os
import subprocess


file_name = "spirale.dat"
wc_cmd = subprocess.check_output(['wc', file_name])
wc_cmd = wc_cmd.decode()
wc_cmd = wc_cmd.split()
nb_lignes = int(wc_cmd[0])
nb_mots = int(wc_cmd[1])
nb_caractères = int(wc_cmd[2])
print(f"{file_name} contient {nb_lignes} lignes, {nb_mots} mots, "
      f"{nb_caractères} caractères") 