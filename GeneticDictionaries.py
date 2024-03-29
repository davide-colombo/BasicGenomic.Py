# This script is a brief introduction to genetic code in Python

genetic_code = {"GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
                "AAT": "N", "AAC": "N",
                "GAT": "D", "GAC": "D",
                "TGT": "C", "TGC": "C",
                "CAA": "Q", "CAG": "Q",
                "GAA": "E", "GAG": "E",
                "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
                "CAT": "H", "CAC": "H",
                "ATT": "I", "ATC": "I", "ATA": "I",
                "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
                "AAA": "K", "AAG": "K",
                "ATG": "M",
                "TTT": "F", "TTC": "F",
                "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
                "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                "TGG": "W",
                "TAT": "Y", "TAC": "Y",
                "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V"
                }

nucleotide_complements = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

restriction_sites = {
    "EcoRI": r'GAATTC',
    "XbaI": r'TCTAGA',
    "ClaI": r'ATCGAT',
    "EaeI": r'(C|T)GGCC(A|G)'
}

methylated_site = {
    "XbaI": r'(GATCTAGA|TCTAGATC)',
    "EaeI": r'(C|T)GGCC(A|G)GG'
}
