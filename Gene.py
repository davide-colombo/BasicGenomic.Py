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
                                 five=rna.seq[0:11] + "..." + rna.seq[orf.start() - 11:orf.start()]))
                    print("3' UTR goes from {end} to {l} - {three}\n".
                          format(end=orf.end(), l=len(rna.seq),
                                 three=rna.seq[orf.end():orf.end() + 11] + "..." + rna.seq[-11:-1]))
                    break

    def print_intragenic_regions(self):
        for rna in self.rna_list:
            print("\n" + rna.header + "\n")
            exon_regions = self.get_exon_regions(rna)
            is_first_exon = True
            intron_count = 0
            for region_index in range(0, len(exon_regions)):
                region_at_index = exon_regions[region_index]        # this is a tuple object: (exon_start, exon_end)
                is_last_exon = (region_at_index == exon_regions[-1])
                if is_first_exon:
                    is_first_exon = False
                    if region_at_index[0] != 0:
                        print("intragenic region #{n} goes from 1 to {e}".
                              format(n=intron_count+1, e=region_at_index[0]))
                        region_at_next_index = exon_regions[region_index+1]
                        print("intragenic region #{n} goes from {s} to {e}".
                              format(n=intron_count+2, s=region_at_index[1]+1, e=region_at_next_index[0]))
                        intron_count += 2
                    else:
                        region_at_next_index = exon_regions[region_index+1]
                        print("intragenic region #{n} goes from {s} to {e}".
                              format(n=intron_count+1, s=region_at_index[1]+1, e=region_at_next_index[0]))
                        intron_count += 1
                else:
                    if is_last_exon:
                        if region_at_index[1] != len(self.dna_seq.seq):
                            print("intragenic region #{n} goes from {s} to {e}".
                                  format(n=intron_count+1, s=region_at_index[1]+1, e=len(self.dna_seq.seq)))
                    else:
                        region_at_next_index = exon_regions[region_index+1]
                        print("intragenic region #{n} goes from {s} to {e}".
                              format(n=intron_count+1, s=region_at_index[1]+1, e=region_at_next_index[0]))
                        intron_count += 1

    def get_exon_regions(self, rna_obj):
        exon_regions = list()
        associated_exons = self.get_exon_associated_2_rna(rna_obj)
        for exon in associated_exons:
            start = self.dna_seq.seq.find(exon.seq)
            end = start + len(exon.seq)
            exon_regions.append((start, end))
        return exon_regions

    def get_exon_associated_2_rna(self, rna_obj):
        matched_exon = list()
        rna_header = rna_obj.header
        for exon in self.exon_list:
            if rna_header in exon.header:
                matched_exon.append(exon)
        return matched_exon
