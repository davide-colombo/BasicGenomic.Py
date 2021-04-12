import re


class FileUtils:

    def split_multiple_sequences(self, string):
        seq_list = list()
        single_seq = list()
        is_first_seq = True
        lines = string.splitlines()

        for line in lines:
            is_last_seq = (line == lines[-1])
            if line.startswith(">") or is_last_seq:
                if line.startswith(">") and not self.is_valid_header(line):
                    raise Exception("Not a valid header: {}".format(line))

                if not is_first_seq:
                    if is_last_seq:
                        single_seq.append(line)
                    seq_list.append("\n".join(single_seq))
                    single_seq.clear()
                is_first_seq = False
                single_seq.append(line)
            else:
                single_seq.append(line)
        return seq_list

    def is_valid_header(self, header):
        pattern = re.compile(r'>(Homosapiens)-(nanog|pou5f1)(-(cds|transcript)[0-9])?(-(protein|exon)[0-9])?')
        matches = pattern.finditer(header)
        return len(list(matches)) != 0

