import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):




# - - - - - - - - - C O R E - - - - - - - - - - - 

    def test_compare_3_1_returns_3_is_greater_than_1(self):
       self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_5_11_returns_5_is_smaller_than_11(self):
        self.assertEqual("5 is smaller than 11", compare(5,11))

    def test_100_equals_100_returns_100_is_euqual_to_100(self):
        self.assertEqual("both numbers are equal", compare(100,100))

# - - - - - - - E X T E N D E D - - - - - - -

    # def test_both_values_were_the_same_string(self):
    #     self.assertEqual("both inputs were equal strings of value: McGruuuber", compare("McGruuuber","McGruuuber"))


    # def test_compare_3_1_returns_3_is_greater_than_1(self):
    #     self.assertEqual("3 is greater than 1", compare(str(3), str(1)))

    # def test_compare_5_11_returns_5_is_smaller_than_11(self):
    #     self.assertEqual("5 is smaller than 11", compare(str(5),str(11)))

    # def test_100_equals_100_returns_100_is_euqual_to_100(self):
    #     self.assertEqual("both numbers are equal", compare(str(100),str(100)))

    #def test_compare_3_pt_1_1_pt_3_returns_3_pt_1_is_greater_than_1_pt_3(self):
    #    self.assertEqual("3 is greater than 1", compare(3.1, 1.2))

    # def both_values_were_the_same_string(self):
    #     self.assertEqual("both inputs were equal strings of value: McGruuuber", compare(str("McGruuuber"),str("McGruuuber")))

    #def both_values_were_the_same_string(self):
    #    self.assertEqual("both inputs were equal strings of value: McGruuuber", compare("McGruuuber","McGruuuber"))


    # def test_first_value_is_a_string_and_cannot_be_compared_with_number_two(self):
    #     pass

    # def test_second_value_is_a_string_and_cannot_be_compared_with_number_one(self):
    #     pass

    
    #def test_both_values_were_a_string_and_the_first_was_alphabetically_ahead_of_the_second(self):
    #    pass
    #def test_both_values_were_a_string(self):
    #    pass
    
