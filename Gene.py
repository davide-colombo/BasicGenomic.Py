from FastaSequence import FastaSequence
from SequenceUtils import SequenceUtils

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

    def print_utr_regions(self, seq_utils):
        for rna in self.rna_list:
            associated_cds = self.get_cds_from_transcript(rna)
            orf_matches = seq_utils.get_open_reading_frames(rna.seq)
            print(rna.header)
            for orf in orf_matches:
                if orf.group() == associated_cds.seq:
                    print("5' UTR goes from 0 to {start} - {five}".
                          format(start=orf.start(),
                                 five=rna.seq[0:11] + "..." + rna.seq[orf.start()-11:orf.start()]))
                    print("3' UTR goes from {end} to {l} - {three}\n".
                          format(end=orf.end(), l=len(rna.seq),
                                 three=rna.seq[orf.end():orf.end()+11] + "..." + rna.seq[-11:-1]))
                    break

