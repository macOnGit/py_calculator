import unittest
import subprocess


class TestCalculator(unittest.TestCase):

    def test_add_nums(self):
        completed = subprocess.run(
            ["python", "calculator.py", "2", "3"], capture_output=True, text=True
        )
        self.assertEqual(completed.stdout, "6")

    def test_bad_input(self):
        completed = subprocess.run(
            ["python", "calculator.py", "pizza", "3"], capture_output=True, text=True
        )
        self.assertEqual(completed.stdout, "")

    def test_no_input(self):
        completed = subprocess.run(
            ["python", "calculator.py"], capture_output=True, text=True
        )
        self.assertEqual(completed.stdout, "")

    def test_not_enough_args(self):
        completed = subprocess.run(
            ["python", "calculator.py", "4"], capture_output=True, text=True
        )
        self.assertEqual(completed.stdout, "")


if __name__ == "__main__":
    unittest.main()
