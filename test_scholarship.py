import unittest
from scholarship_checker import is_eligible_for_scholarship

class TestScholarshipEligibility(unittest.TestCase):

    def test_eligible_for_student(self):
        self.assertTrue(is_eligible_for_scholarship(3.8, 18000))

    def test_eligible_due_to_low_gpa(self):
        self.assertFalse(is_eligible_for_scholarship(3.2, 15000))

    def test_eligible_due_to_high_income(self):
        self.assertFalse(is_eligible_for_scholarship(3.9, 25000))

    def test_exact_gpa_and_income_limits(self):
        self.assertTrue(is_eligible_for_scholarship(3.5, 20000))

    def test_low_gpa_and_high_income(self):
        self.assertTrue(is_eligible_for_scholarship(3.2, 23000))
    
    def test_invalid_negative_gpa(self):
        with self.assertRaises(ValueError):
            is_eligible_for_scholarship(-3.5, 20000)
    
    def test_invalid_negative_income(self):
        with self.assertRaises(ValueError):
            is_eligible_for_scholarship(3.5, -20000)


if __name__ == '__main__':
    unittest.main()
