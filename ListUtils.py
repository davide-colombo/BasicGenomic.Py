from DNA import DNA
from Protein import Protein
from RNA import RNA

class ListUtils:

    def convert_list_to_DNA(self, list_2_convert):
        for i in range(0, len(list_2_convert)):
            list_2_convert[i] = DNA(list_2_convert[i])
        return list_2_convert

    def convert_list_to_Protein(self, list_2_convert):
        for i in range(0, len(list_2_convert)):
            list_2_convert[i] = Protein(list_2_convert[i])
        return list_2_convert

    def convert_list_to_RNA(self, list_2_convert):
        for i in range(0, len(list_2_convert)):
            list_2_convert[i] = RNA(list_2_convert[i])
        return list_2_convert