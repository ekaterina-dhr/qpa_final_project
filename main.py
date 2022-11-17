from data.database_dna_rna import *
from data.database_triplets_aminoacids import *
import matplotlib.pyplot as plt


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


rna1 = convert_dna_to_rna(input("Input DNA sequence: "))
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


protein1 = convert_rna_to_protein(input("Input RNA sequence: "))
print(protein1)


def gc_content_ratio(sequence, step):
    genome_position = []
    gc_content_list = []
    step = int(step)
    for base in range(0, len(sequence) - step + 1, step):
        part = sequence[base:base + step]
        genome_position.append(base + step)
        gc_content = (part.count("G") + part.count("C")) / len(part) * 100
        gc_content_list.append(gc_content)
    plt.plot(genome_position, gc_content_list)
    plt.xlabel('Genome position')
    plt.ylabel('GC-content ratio')
    plt.title('GC-content metric')
    return plt.show()


fileReader = open("genomic.fna", 'r')
covid_sequence = ""
for number, line in enumerate(fileReader):
    if number > 0:
        covid_sequence += line
fileReader.close()

gc = gc_content_ratio(covid_sequence, 100)

"""
Script to run gc_content_ratio with different DNA sequence and size of the window

gc = gc_content_ratio(input("Input the DNA sequence: "), input("Input the size of the window "))
print(gc)
"""
