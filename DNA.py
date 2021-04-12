from FastaSequence import FastaSequence
import re

class DNA(FastaSequence):

    def print_type(self):
        print("DNA")

    def get_gc_percentage(self):
        pattern = re.compile(r'(G|C){1}')
        matches = pattern.finditer(self.seq)
        return (len(list(matches)) / len(self.seq)) * 100
