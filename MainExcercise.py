
import os

from DNA import DNA
from Gene import Gene

from SequenceUtils import SequenceUtils
from FileUtils import FileUtils
from ListUtils import ListUtils

# ========================================================================================

#                                     CODE BEGINS HERE...

# ========================================================================================
os.chdir("/Users/davidecolombo/Desktop/universita/quintoanno/Bioinformatica/esercitazioni")
nanog_dir = "nanogHomoSapiens/"
pou5f1_dir = "pou5f1HomoSapiens/"

seq_utils = SequenceUtils()
file_utils = FileUtils()
list_utils = ListUtils()

print("\n======================== QUESTION 1 ========================\n")
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
rna_list = list_utils.convert_list_to_DNA(rna_list)

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
print("nanog gene OK\n")

# ========================================================================================

#                                  POU5F1 HOMO SAPIENS

# ========================================================================================

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
rna_list = list_utils.convert_list_to_DNA(rna_list)

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

print("\n======================== QUESTION 2 ========================\n")

# DOMANDA 2 - Per ciascun gene si calcoli lunghezza e contenuto in %GC
print("nanog Homo sapiens gene length = {}".format(nanog_gene.dna_seq.get_sequence_length()))
print("nanog Homo sapiens gene %GC = {:.3f} %".format(nanog_gene.dna_seq.get_gc_percentage()))
print("\n")
print("pou5f1 Homo sapiens gene length = {}".format(pou5f1_gene.dna_seq.get_sequence_length()))
print("pou5f1 Homo sapiens gene %GC = {:.3f} %".format(pou5f1_gene.dna_seq.get_gc_percentage()))

print("\n======================== QUESTION 3 ========================\n")

# DOMANDA 3 - Mediante espressione regolare, si verifichi la validità della CDS
for cds in nanog_gene.cds_list:
    print("{header} is valid? {is_valid}".format(header=cds.header, is_valid=seq_utils.is_valid_cds(cds.seq)))
print("\n")
for cds in pou5f1_gene.cds_list:
    print("{header} is valid? {is_valid}".format(header=cds.header, is_valid=seq_utils.is_valid_cds(cds.seq)))

print("\n======================== QUESTION 4 ========================\n")

# DOMANDA 4 - Per ciascun gene, si calcoli se i trascritti più lunghi corrispondono alle proteine più lunghe

nanog_gene.longest_rna_correspond_2_longest_protein()
print("\n")
pou5f1_gene.longest_rna_correspond_2_longest_protein()

print("\n======================== QUESTION 5 ========================\n")

# DOMANDA 5 - Si calcoli il reverse-complement dei geni

nanog_reverse_compl = seq_utils.reverse_complement(nanog_gene.dna_seq.seq)
print("nanog Homo sapiens gene reverse complement is: {}".
      format(nanog_reverse_compl[:10] + "..." + nanog_reverse_compl[-10:]))
print("\n")
pou5f1_reverse_compl = seq_utils.reverse_complement(pou5f1_gene.dna_seq.seq)
print("pou5f1 Homo sapiens gene reverse complement is: {}".
      format(pou5f1_reverse_compl[:10] + "..." + pou5f1_reverse_compl[-10:]))

print("\n======================== QUESTION 6 ========================\n")

# DOMANDA 6 - Si trovi quante sequenze ATG sono presenti in ciascun trascritto
print("nanog Homo sapiens ATG count\n")
for rna in nanog_gene.rna_list:
    print("{header}: {count}".format(header=rna.header, count=rna.get_atg_count()))
print("\n")
print("pou5f1 Homo sapiens ATG count\n")
for rna in pou5f1_gene.rna_list:
    print("{header}: {count}".format(header=rna.header, count=rna.get_atg_count()))

print("\n======================== QUESTION 7 ========================\n")

# DOMANDA 7 - Si trovino eventuali sequenze ripetute di A, T, C o G con più di 3 ripetizioni all’interno dei geni
print("nanog Homo sapiens gene repeated sequences are:\n")
nanog_gene.dna_seq.print_repeated_sequence_matches()
print("\n")
print("pou5f1 Homo sapiens gene repeated sequences are:\n")
pou5f1_gene.dna_seq.print_repeated_sequence_matches()
