import unittest
import subprocess


class TestCalculator(unittest.TestCase):
    cmd = ["python3", "calculator.py"]

    def test_add_nums(self):
        completed = subprocess.run(
            self.cmd + ["2", "3"], capture_output=True, text=True
        )
        self.assertEqual(completed.stdout, "6")

    def test_bad_input(self):
        completed = subprocess.run(
            self.cmd + ["str", "3"], capture_output=True, text=True
        )
        self.assertEqual(completed.stdout, "")

    def test_no_input(self):
        completed = subprocess.run(self.cmd, capture_output=True, text=True)
        self.assertEqual(completed.stdout, "")

    def test_not_enough_args(self):
        completed = subprocess.run(self.cmd, capture_output=True, text=True)
        self.assertEqual(completed.stdout, "")


if __name__ == "__main__":
    unittest.main()
