# The Sequence class

class FastaSequence:

    def __init__(self, seq):
        self.seq = "".join(seq.split("\n")[1:])
        self.header = seq.split("\n")[0]

    def get_sequence_length(self):
        return len(self.seq)

    def to_string(self):
        print("HEADER: {h}\n"
              "{seq}".format(h=self.header, seq=self.seq))

    def print_type(self):
        print("FastaSequence")