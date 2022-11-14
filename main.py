from data.database_dna_rna import *
from data.database_triplets_aminoacids import *


def convert_dna_to_rna(dna_input):
    """
    Original function that I created before the database
    """
    # rna = dna_input.replace("T", "U")

    """
    Below I tried to use the information from the database because 
    in the database I've already set the relations between DNA bases and RNA bases
    """

    rna = ""
    for base_input in dna_input:
        for dna_base in dna_sequence:
            if dna_base.base == base_input:
                rna += dna_base.rna_relation.base
    return rna


rna1 = convert_dna_to_rna(input())
print(rna1)


def convert_rna_to_protein(rna_input):
    protein = ""
    for nucleotide in range(0, len(rna_input), 3):
        triplet_input = rna_input[nucleotide:nucleotide + 3]
        if len(triplet_input) == 3:
            for codon in codons_list:
                if codon.triplet == triplet_input:
                    protein += codon.amino_acid_relation.acid
    return protein


protein1 = convert_rna_to_protein(input())
print(protein1)
