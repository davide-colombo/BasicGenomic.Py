from FastaSequence import FastaSequence


class Gene:

    def __init__(self, dna_seq, rna_list, cds_list, exon_list, protein_list):
        self.dna_seq = dna_seq
        self.rna_list = rna_list
        self.cds_list = cds_list
        self.exon_list = exon_list
        self.protein_list = protein_list

    def longest_rna_correspond_2_longest_protein(self):
        print(self.search_longest_rna_header())
        print(self.search_longest_protein_header())

    def search_longest_rna_header(self):
        longest_rna_header = ""
        max_len = len(self.rna_list[0].seq)
        for rna in self.rna_list:
            rna_len = len(rna.seq)
            if rna_len >= max_len:
                max_len = rna_len
                longest_rna_header = rna.header
        return longest_rna_header

    def search_longest_protein_header(self):
        longest_prot_header = ""
        max_len = len(self.protein_list[0].seq)
        for prot in self.protein_list:
            prot_len = len(prot.seq)
            if prot_len >= max_len:
                max_len = prot_len
                longest_prot_header = prot.header
        return longest_prot_header

    def get_protein_from_cds(self, cds_obj):
        cds_header = cds_obj.header
        cds_number = cds_header[-1]
        for prot in self.protein_list:
            if cds_number == prot.header[-1]:
                return prot
        raise Exception("No protein associated to cds number {n}".format(n=cds_number))

    def get_cds_from_transcript(self, rna_obj):
        rna_header = rna_obj.header
        rna_number = rna_header[-1]
        for cds in self.cds_list:
            if cds.header[-1] == rna_number:
                return cds
        raise Exception("No cds associated to rna number {n}".format(n=rna_number))
