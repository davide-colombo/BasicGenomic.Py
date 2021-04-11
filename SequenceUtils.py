from GeneticDictionaries import genetic_code
from GeneticDictionaries import nucleotide_complements

class SequenceUtils:

    def dna_2_rna(self, dna_seq):
        rna_seq = list()
        for nucleotide in dna_seq:
            if nucleotide == "T":
                rna_seq.append("U")
            else:
                rna_seq.append(nucleotide)
        return "".join(rna_seq)

    def dna_2_protein(self, dna_seq):
        protein = list()
        codons = [dna_seq[i:i + 3] for i in range(0, len(dna_seq), 3)]
        for codon in codons:
            protein.append(genetic_code.get(codon, "_"))                    # This is to avoid to return None type!!!
        return "".join(protein)

    def reverse_complement(self, dna_seq):
        rev_seq = list()
        for i in range(1, len(dna_seq)+1):
            rev_seq.append(nucleotide_complements.get(dna_seq[-i], "_"))
        return "".join(rev_seq)
