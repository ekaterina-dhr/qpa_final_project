from sqlalchemy import (
    Column, ForeignKey, Integer, String,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///triplets_aminoacids_relations.db")

Session = sessionmaker(bind=engine)

Base = declarative_base()

genetic_code = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
                "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
                "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
                "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
                "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
                "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
                "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
                "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
                }


class Codons(Base):
    __tablename__ = "codons"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    triplet = Column(String)
    amino_acid_relation = relationship("AminoAcids", back_populates="codon_relation")
    amino_acid_id = Column(Integer, ForeignKey("amino_acids.id"))

    def __str__(self):
        return f"{self.id}: {self.triplet} relates to <<{self.amino_acid_relation}>>"


class AminoAcids(Base):
    __tablename__ = "amino_acids"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    acid = Column(String)
    codon_relation = relationship("Codons", back_populates="amino_acid_relation")

    def __str__(self):
        return self.acid


Base.metadata.create_all(engine)

amino_acids_list = []

for value in genetic_code.values():
    value = AminoAcids(acid=str(value))
    amino_acids_list.append(value)

codons_list_indexes = []
codons_list = []

for key in genetic_code:
    codons_list_indexes.append(key)
    index = codons_list_indexes.index(key)
    key = Codons(triplet=str(key), amino_acid_relation=amino_acids_list[index])
    codons_list.append(key)


with Session() as session:
    session.add_all(codons_list)
    session.commit()
    for codon in session.query(Codons).all():
        print(codon)

"""
I delete the information from the database at the end of the file
because the information is added again every time I run the script.
Not sure how to repair it in a good way.
"""

session.query(Codons).delete()
session.commit()
