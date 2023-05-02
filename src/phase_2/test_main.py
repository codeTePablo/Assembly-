import unittest
import refact


class TestRefact(unittest.TestCase):
    def test_analyze(self):
        self.assertTrue(refact.analizeDataSegment(["mov ax, 1"]))


if __name__ == "__main__":
    unittest.main()
