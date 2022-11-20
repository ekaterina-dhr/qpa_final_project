from sqlalchemy import (
    Column, ForeignKey, Integer, String,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# from config import dna_rna_relations_address

engine = create_engine("sqlite:///dna_rna_relations.db")

Session = sessionmaker(bind=engine)

Base = declarative_base()


class Dna(Base):
    __tablename__ = "dna_bases"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    base = Column(String)
    rna_relation = relationship("Rna", back_populates="dna_relation")
    rna_id = Column(Integer, ForeignKey("rna_bases.id"))

    def __str__(self):
        return f"{self.id}: {self.base} relates to <<{self.rna_relation}>> in RNA"


class Rna(Base):
    __tablename__ = "rna_bases"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    base = Column(String)
    dna_relation = relationship("Dna", back_populates="rna_relation")

    def __str__(self):
        return self.base


Base.metadata.create_all(engine)

rna_base_1 = Rna(base="A")
rna_base_2 = Rna(base="C")
rna_base_3 = Rna(base="G")
rna_base_4 = Rna(base="U")

dna_base_1 = Dna(base="A", rna_relation=rna_base_1)
dna_base_2 = Dna(base="C", rna_relation=rna_base_2)
dna_base_3 = Dna(base="G", rna_relation=rna_base_3)
dna_base_4 = Dna(base="T", rna_relation=rna_base_4)

dna_sequence = [dna_base_1, dna_base_2, dna_base_3, dna_base_4]


if __name__ == "__main__":
    with Session() as session:
        session.add_all(dna_sequence)
        session.commit()
        for dna in session.query(Dna).all():
            print(dna)

    session.query(Dna).delete()
    session.commit()

"""
I delete the information from the database at the end of the file
because the information is added again every time I run the script.
Not sure how to repair it in a good way.
"""


