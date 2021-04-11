
import os
import re

from DNA import DNA
from SequenceUtils import SequenceUtils
from FileUtils import FileUtils
from ListUtils import ListUtils

from Gene import Gene

# ========================================================================================

#                                     CODE BEGINS HERE...

# ========================================================================================
os.chdir("/Users/davidecolombo/Desktop/universita/quintoanno/Bioinformatica/esercitazioni")
nanog_dir = "nanogHomoSapiens/"
pou5f1_dir = "pou5f1HomoSapiens/"

seq_utils = SequenceUtils()
file_utils = FileUtils()
list_utils = ListUtils()

print("\n======================== OPEN AND READING NANOG GENE FILE ========================\n")
with open(nanog_dir + "nanog_gene.txt") as f:
    lines = "".join(f.readlines())
f.close()

# nanog Homo sapiens gene sequence
nanog_seq = DNA(lines)
# nanog_seq.to_string()
# print("Is valid gene sequence? {}".format(seq_utils.is_valid_dna(nanog_seq.seq)))

# Open and read nanog homo sapiends cds file
with open(nanog_dir + "nanog_cds.txt") as f:
    lines = "".join(f.readlines())
f.close()

# Split multiple sequence
cds_list = file_utils.split_multiple_sequences(lines)

# Convert to objects
cds_list = list_utils.convert_list_to_DNA(cds_list)
# cds_list[0].to_string()
# cds_list[0].print_type()

# Read nanog homo sapiens protein file
with open(nanog_dir + "nanog_prot.txt") as f:
    lines = "".join(f.readlines())
f.close()

prot_list = file_utils.split_multiple_sequences(lines)
prot_list = list_utils.convert_list_to_Protein(prot_list)
# prot_list[0].to_string()
# prot_list[0].print_type()

# Read nanog homo sapiens exon file
with open(nanog_dir + "nanog_exon.txt") as f:
    lines = "".join(f.readlines())
f.close()

exon_list = file_utils.split_multiple_sequences(lines)
exon_list = list_utils.convert_list_to_DNA(exon_list)
# exon_list[0].to_string()
# exon_list[0].print_type()

# Read nanog homo sapiens transcript file
with open(nanog_dir + "nanog_transcript.txt") as f:
    lines = "".join(f.readlines())
f.close()

rna_list = file_utils.split_multiple_sequences(lines)
rna_list = list_utils.convert_list_to_RNA(rna_list)
# rna_list[0].to_string()
# rna_list[0].print_type()

# Creating the gene object
nanog_gene = Gene(nanog_seq, rna_list, cds_list, exon_list, prot_list)
# print(nanog_gene.dna_seq.header)
# print(nanog_gene.rna_list[0].header)
# print(nanog_gene.exon_list[0].header)

