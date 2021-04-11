
class FileUtils:

    def split_multiple_sequences(self, string):
        seq_list = list()
        single_seq = list()
        is_first_seq = True
        lines = string.splitlines()

        for line in lines:
            is_last_seq = (line == lines[-1])
            if line.startswith(">") or is_last_seq:
                if not is_first_seq:
                    seq_list.append("\n".join(single_seq))
                    single_seq.clear()
                is_first_seq = False
                single_seq.append(line)
            else:
                single_seq.append(line)
        return seq_list



