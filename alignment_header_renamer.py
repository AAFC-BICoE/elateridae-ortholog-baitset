"""
Standardizes aa alignment fasta and nt fasta headers to be compatible for tranalign
Author Jackson Eyres jackson.eyres@canada.ca
License: MIT
Copywright: Government of Canada
"""
from Bio import AlignIO, SeqIO
import os
import glob

alignment_dir = "/home/eyresj/Desktop/Summarized/alignments"
original_fasta_dir = "/home/eyresj/Desktop/Summarized/nt_summarized"


def rename_alignment_header(alignment_dir, original_fasta_dir):
    alignment_files = glob.glob(os.path.join(alignment_dir, "*.fasta_aln"))
    fastas = glob.glob(os.path.join(original_fasta_dir, "*.fa"))


    for file in fastas:
        seqs = []
        new_file = file.replace("nt_summarized","nt_renamed")
        for seq in SeqIO.parse(file,"fasta"):
            #print(seq.id)
            seq.id = "_".join(seq.id.split("|")[0:2])
            seq.description = ""
            seqs.append(seq)

        with open(new_file, "w") as g:
            SeqIO.write(seqs, g, "fasta")
            #print(seq.id)
        #break


    seq_names = []
    reference_seqs = ["Aethina", "Agrilus", "Anoplophora", "Dendroctonus", "Leptinotarsa", "Nicrophorus", "Onthophagus", "Oryctes", "Tribolium"]
    for file in alignment_files:
        print(file)
        alns = []
        new_file = file.replace("alignments", "alignments_fasta_renamed").replace(".fasta_aln", ".aln")
        with open(file) as g:
            alignments = AlignIO.read(g, "fasta")
            for aln in alignments:
                aln.id = "_".join(aln.id.split("|")[0:2])
                aln.description = ""
                #
                is_reference = False
                for item in reference_seqs:
                    if item in aln.id:
                        is_reference = True
                if not is_reference:
                    alns.append(aln)

        with open(new_file, "w") as g:
            SeqIO.write(alns, g, "fasta")
        #break

rename_alignment_header(alignment_dir, original_fasta_dir)