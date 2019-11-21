import unittest

from okam.security import Key

class TestKeyMethods(unittest.TestCase):

    def test_generate(self):
        self.assertEqual(32, len(Key.generate()))

        self.assertEqual(16, len(Key.generate(16)))

    def test_encode_and_decode(self):
        key = Key.generate()

        encoded = Key.encode(key)

        self.assertEqual(key, Key.decode(encoded))

    def test_generate_encoded(self):
        self.assertEqual(36, len(Key.generate_encoded(16))) # prefix = 4, random string = 32

        self.assertEqual('hex:', Key.generate_encoded(16)[:4])

        self.assertEqual(68, len(Key.generate_encoded(32))) # prefix = 4, random string = 64

        self.assertEqual('hex:', Key.generate_encoded(16)[:4])

if __name__ == '__main__':
    unittest.main()
