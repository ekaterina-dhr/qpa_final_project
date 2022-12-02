import unittest

from main import convert_dna_to_rna, convert_rna_to_protein, gc_content_ratio


class TestDnaToRna(unittest.TestCase):
    def test_basic(self):
        """Test checks if DNA sequence is converted to RNA correctly"""
        data_input = "ATTTGGCTACTAACAATCTA"
        expected = "AUUUGGCUACUAACAAUCUA"
        actual = convert_dna_to_rna(dna_input=data_input)

        self.assertTrue(actual == expected, f"should be {expected}")

    def test_empty(self):
        """Test checks the result if DNA sequence is empty"""
        data_input = ""
        expected = ""
        actual = convert_dna_to_rna(dna_input=data_input)

        self.assertTrue(actual == expected, f"should be {expected}")

    def test_none(self):
        """Test checks the result if input is None"""
        data_input = None

        with self.assertRaises(TypeError):
            actual = convert_dna_to_rna(dna_input=data_input)


class TestRnatoProtein(unittest.TestCase):
    def test_basic(self):
        """Test checks if RNA sequence is converted to protein correctly"""
        data_input = "AUUUGGCUACUAACAAUCUA"
        expected = "IWLLTI"
        actual = convert_rna_to_protein(rna_input=data_input)

        self.assertTrue(actual == expected, f"should be {expected}")

    def test_empty(self):
        """Test checks the result if RNA sequence is empty"""
        data_input = ""
        expected = ""
        actual = convert_rna_to_protein(rna_input=data_input)

        self.assertTrue(actual == expected, f"should be {expected}")

    def test_none(self):
        """Test checks the result if input is None"""
        data_input = None

        with self.assertRaises(TypeError):
            actual = convert_rna_to_protein(rna_input=data_input)


class TestGCcontentRatio(unittest.TestCase):
    def test_basic(self):
        """Test checks the list of GC ratio in each part of the window"""
        data_input = ["GCTAACTAAC", 2]
        expected = [100.0, 0.0, 50.0, 0.0, 50.0]
        actual = gc_content_ratio(*data_input)

        self.assertTrue(actual == expected, f"should be {expected}")

    def test_empty(self):
        """Test checks the GC ratio if window step is 0"""
        data_input = ["GCTAACTAAC", 0]

        with self.assertRaises(ValueError):
            actual = gc_content_ratio(*data_input)

    def test_none(self):
        """Test checks the result if input is None"""
        data_input = None

        with self.assertRaises(TypeError):
            actual = gc_content_ratio(*data_input)


if __name__ == "__main__":
    unittest.main()
