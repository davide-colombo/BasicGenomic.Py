from FastaSequence import FastaSequence


class Gene:

    def __init__(self, dna_seq, rna_list, cds_list, exon_list, protein_list):
        self.dna_seq = dna_seq
        self.rna_list = rna_list
        self.cds_list = cds_list
        self.exon_list = exon_list
        self.protein_list = protein_list
