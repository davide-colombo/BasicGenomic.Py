
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

nanog_seq = DNA(lines)

# ========================= NANOG CDS =========================
with open(nanog_dir + "nanog_cds.txt") as f:
    lines = "".join(f.readlines())
f.close()

cds_list = file_utils.split_multiple_sequences(lines)
cds_list = list_utils.convert_list_to_DNA(cds_list)

# ========================= NANOG PROTEIN =========================
with open(nanog_dir + "nanog_prot.txt") as f:
    lines = "".join(f.readlines())
f.close()

prot_list = file_utils.split_multiple_sequences(lines)
prot_list = list_utils.convert_list_to_Protein(prot_list)

# ========================= NANOG EXON =========================
with open(nanog_dir + "nanog_exon.txt") as f:
    lines = "".join(f.readlines())
f.close()

exon_list = file_utils.split_multiple_sequences(lines)
exon_list = list_utils.convert_list_to_DNA(exon_list)

# ========================= NANOG mRNA =========================
with open(nanog_dir + "nanog_transcript.txt") as f:
    lines = "".join(f.readlines())
f.close()

rna_list = file_utils.split_multiple_sequences(lines)
rna_list = list_utils.convert_list_to_RNA(rna_list)

# ========================= NANOG GENE OBJECT =========================
nanog_gene = Gene(nanog_seq, rna_list, cds_list, exon_list, prot_list)
# nanog_gene.dna_seq.to_string()                                       # GENE OK
# nanog_gene.dna_seq.print_type()
# nanog_gene.rna_list[0].to_string()                                   # mRNA OK
# nanog_gene.rna_list[0].print_type()
# nanog_gene.cds_list[0].to_string()                                   # CDS OK
# nanog_gene.cds_list[0].print_type()
# nanog_gene.exon_list[0].to_string()                                  # EXON OK
# nanog_gene.exon_list[0].print_type()
# nanog_gene.protein_list[0].to_string()                               # PROTEIN OK
# nanog_gene.protein_list[0].print_type()
print("nanog gene OK")

# ========================================================================================

#                                  POU5F1 HOMO SAPIENS

# ========================================================================================

print("\n======================== OPEN AND READING POU5F1 GENE FILE ========================\n")

with open(pou5f1_dir + "pou5f1_gene.txt", "r") as f:
    lines = "".join(f.readlines())
f.close()

pou5f1_seq = DNA(lines)

# ========================= POU5F1 CDS =========================
with open(pou5f1_dir + "pou5f1_cds.txt", "r") as f:
    lines = "".join(f.readlines())
f.close()

cds_list = file_utils.split_multiple_sequences(lines)
cds_list = list_utils.convert_list_to_DNA(cds_list)

# ========================= POU5F1 EXON =========================
with open(pou5f1_dir + "pou5f1_exon.txt", "r") as f:
    lines = "".join(f.readlines())
f.close()

exon_list = file_utils.split_multiple_sequences(lines)
exon_list = list_utils.convert_list_to_DNA(exon_list)

# ========================= POU5F1 PROTEIN =========================
with open(pou5f1_dir + "pou5f1_prot.txt", "r") as f:
    lines = "".join(f.readlines())
f.close()

prot_list = file_utils.split_multiple_sequences(lines)
prot_list = list_utils.convert_list_to_Protein(prot_list)

# ========================= POU5F1 mRNA =========================
with open(pou5f1_dir + "pou5f1_transcript.txt", "r") as f:
    lines = "".join(f.readlines())
f.close()

rna_list = file_utils.split_multiple_sequences(lines)
rna_list = list_utils.convert_list_to_RNA(rna_list)

# ========================= POU5F1 GENE OBJECT =========================
pou5f1_gene = Gene(pou5f1_seq, rna_list, cds_list, exon_list, prot_list)
# pou5f1_gene.dna_seq.to_string()                                       # GENE OK
# pou5f1_gene.dna_seq.print_type()
# pou5f1_gene.rna_list[0].to_string()                                   # mRNA OK
# pou5f1_gene.rna_list[0].print_type()
# pou5f1_gene.cds_list[0].to_string()                                   # CDS OK
# pou5f1_gene.cds_list[0].print_type()
# pou5f1_gene.exon_list[0].to_string()                                  # EXON OK
# pou5f1_gene.exon_list[0].print_type()
# pou5f1_gene.protein_list[0].to_string()                               # PROTEIN OK
# pou5f1_gene.protein_list[0].print_type()
print("pou5f1 gene OK")

