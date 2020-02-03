import json
from Bio import SeqIO
import glob
# with open("/home/eyresj/Desktop/orthodb10_coleoptera.txt") as f:
#     data = json.load(f)
#     with open("/home/eyresj/Desktop/7041_OG2.txt", "w") as g:
#         for item in data['data']:
#             g.write(item.replace("'","")+"\n")
#             print(item.replace("'",""))

fasta_headers = []
with open("/home/eyresj/Desktop/OrthoDB_Coleoptera_cut_80.tsv") as f:
    lines = f.readlines()
    lines.pop(0)
    for line in lines:
        split = line.rstrip().split("\t")
        fasta_headers.append(split[1])

fasta_files = glob.glob("/home/eyresj/Desktop/Coleoptera_OrthoDB_Fastas/*.fs")
print(len(set(fasta_headers)))
import collections
print([item for item, count in collections.Counter(fasta_headers).items() if count > 1])

print(len(fasta_headers))
print(fasta_headers[:5])
orthologs = []
for fasta_file in fasta_files:
    with open(fasta_file) as f:
        for seq in SeqIO.parse(f, "fasta"):
            if seq.name in fasta_headers:
                #seq.description = fasta_headers[seq.name]
                orthologs.append(seq)
    print(fasta_file)
print(len(orthologs))
print(len(fasta_headers))
# print(list(set(fasta_headers) - set(orthologs)))
# for item in fasta_headers:
#     if item not in orthologs:
#         print(item)
# with open("/home/eyresj/Desktop/Coleoptera_OrthoDBv10_Orthologs.fasta", "w") as g:
#     for seq in orthologs:
#         SeqIO.write(seq, g, "fasta")
# for key, value in sorted(fasta_headers.items()):
#     file_name = key.split(":")[0] +

