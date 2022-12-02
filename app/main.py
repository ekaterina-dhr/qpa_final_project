import matplotlib.pyplot as plt

from data.database_dna_rna import dna_sequence
from data.database_triplets_aminoacids import codons_list


def convert_dna_to_rna(dna_input):
    """
    Original function that was created before the database
    and which converts DNA sequence to RNA sequence.
    """
    # rna = dna_input.replace("T", "U")

    """
    Below in order to convert DNA sequence to RNA sequence the information from the database is used 
    because in the database the relations between DNA bases and RNA bases are already set
    """

    rna = ""
    for base_input in dna_input:
        for dna_base in dna_sequence:
            if dna_base.base == base_input:
                rna += dna_base.rna_relation.base
    return rna


"""
Code to run the function convert_dna_to_rna

rna1 = convert_dna_to_rna(input("Input DNA sequence: "))
print(rna1)
"""


def convert_rna_to_protein(rna_input):
    """
    Function that converts RNA to protein.
    All the relations between triplets and amino acids are set in the database.
    """
    protein = ""
    for nucleotide in range(0, len(rna_input), 3):
        triplet_input = rna_input[nucleotide:nucleotide + 3]
        if len(triplet_input) == 3:
            for codon in codons_list:
                if codon.triplet == triplet_input:
                    protein += codon.amino_acid_relation.acid
    return protein


"""
Code to run the function convert_rna_to_protein

protein1 = convert_rna_to_protein(input("Input RNA sequence: "))
print(protein1)
"""


def gc_content_ratio(sequence, step):
    """
    This function plots G-C ratio in a DNA molecule.
    The horizontal axis of the graph is the genome position.
    The vertical axis is the GC ratio in each part of the window.
    """
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

    # code to save the plot as png file
    # plt.savefig('plot.png')

    # code to show the plot
    # plt.show()

    return gc_content_list


if __name__ == "__main__":
    """
    Code below refers to the file genomic.fna which contains SARS-CoV-2 genome
    and is used as data to call gc_content_ratio function.
    """
    fileReader = open("data/genomic.fna", 'r')
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
