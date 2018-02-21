from unittest import TestCase
import pandas as pd

original_return = pd.read_csv('q01_australian/tests/Original_classes.csv', header=None)
student_return = pd.read_csv('q01_australian/predicted_class.csv', header=None)


class TestHackathon(TestCase):
    def test_return(self):
        self.assertEqual(student_return, 138,
                         "Expected list of variables does not match returned list of variables")
