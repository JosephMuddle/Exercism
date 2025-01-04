def to_rna(dna_strand):
    dna_to_rna_dict = {"G":"C", "C":"G","T":"A","A":"U"}
    return ''.join([dna_to_rna_dict[x] for x in dna_strand])
