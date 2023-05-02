import unittest
import refact


class TestRefact(unittest.TestCase):
    def test_analyze(self):
        self.assertTrue(refact.analyze("mycode.asm"))


if __name__ == "__main__":
    unittest.main()
