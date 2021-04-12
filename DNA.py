from FastaSequence import FastaSequence
import re


class DNA(FastaSequence):

    def print_type(self):
        print("DNA")

    def get_gc_percentage(self):
        pattern = re.compile(r'(G|C){1}')
        matches = pattern.finditer(self.seq)
        return (len(list(matches)) / len(self.seq)) * 100

    def get_atg_count(self):
        pattern = re.compile(r'(ATG)+')
        matches = pattern.finditer(self.seq)
        return len(list(matches))

    def print_repeated_sequence_matches(self):
        pattern = re.compile(r'((A){4,}|(G){4,}|(T){4,}|(C){4,})')
        matches = pattern.finditer(self.seq)
        for m in matches:
            print(m)
