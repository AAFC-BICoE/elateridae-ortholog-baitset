# coding: utf8
"""
Ortholog Based Bait Design Script for creating Staphylinidae ortholog based baits suitable submission to myBaits
Compares t_coffee AA alignment scores with nucleotide tranalignments to find conserved blocks
Author Jackson Eyres jackson.eyres@canada.ca
License: MIT
Copywright: Government of Canada
"""

import glob
import os
import shutil
from Bio import AlignIO, SeqIO
import time
import argparse


def main():
    """
    Main Function to run Staphylinidae Bait Designer
    :return:
    """
    parser = argparse.ArgumentParser(description='Processes BUSCO merged multi fastas')
    parser.add_argument('-f', type=str, required=True,
                        help='Merged Multi Fasta')
    parser.add_argument('-o', type=str, required=True,
                        help='Output directory')

    args = parser.parse_args()
    unmerge(args.f, args.o)

def unmerge(file, output):

    seq_dict = {}

    with open(file) as f:
        for seq in SeqIO.parse(f, "fasta"):
            identifier = seq.id.split(":")[0]
            if identifier in seq_dict:
                seq_dict[identifier].append(seq)
            else:
                seq_dict[identifier]= [seq]

    for key, value in seq_dict.items():
        if os.path.exists(output):
            pass
        else:
            os.makedirs(output)
        file_name = key + ".fasta"
        file_path = os.path.join(output, file_name)
        with open(file_path, "w") as g:
            SeqIO.write(value, g, "fasta")


if __name__ == "__main__":
    main()