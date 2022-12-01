import unittest

from app.main import convert_dna_to_rna, convert_rna_to_protein, gc_content_ratio
from app.data.database_dna_rna import *
from app.data.database_triplets_aminoacids import *


class TestDnaToRna(unittest.TestCase):
    def test_basic(self):
        """"""
        data_input = "ATTTGGCTACTAACAATCTA"
        expected = "AUUUGGCUACUAACAAUCUA"
        actual = convert_dna_to_rna(dna_input=data_input)

        self.assertTrue(actual == expected, f"should be {expected}")


if __name__ == "__main__":
    unittest.main()
