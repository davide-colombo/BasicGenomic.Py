from DNA import DNA
from SequenceUtils import SequenceUtils
import os

# Changing the current working directory
myDirectory = "/Users/davidecolombo/Desktop/universita/quintoanno/Bioinformatica/esercitazioni/sod1MusMusculus"
os.chdir(myDirectory)

print("\n==================== OPENING AND READING A FILE ====================\n")
with open("sod1_cds.txt", "r") as f:
    lines = "".join(f.readlines())
f.close()

# Creating a SequenceUtils object
seq_utils = SequenceUtils()

print("\n==================== PRINTING DNA SEQUENCE ====================\n")
dna_seq = DNA(lines)
dna_seq.to_string()

print("\n==================== CONVERTING DNA 2 RNA ====================\n")
rna_seq = seq_utils.dna_2_rna(dna_seq.seq)
print(rna_seq)

print("\n==================== CONVERTING DNA 2 PROTEIN ====================\n")
protein_seq = seq_utils.dna_2_protein(dna_seq.seq)
print(protein_seq)

print("\n==================== CHECK IF SEQUENCES ARE VALID ====================\n")
is_valid_dna = seq_utils.is_valid_dna(dna_seq.seq)
is_valid_rna = seq_utils.is_valid_rna(rna_seq)
is_valid_prot = seq_utils.is_valid_protein(protein_seq)

print("Dna is valid? {}".format(is_valid_dna))
print("Rna is valid? {}".format(is_valid_rna))
print("Protein is valid? {}".format(is_valid_prot))

print("\n==================== REVERSE COMPLEMENT ====================\n")
reverse_compl = seq_utils.reverse_complement(dna_seq.seq)
print(reverse_compl)