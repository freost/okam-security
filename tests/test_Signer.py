import unittest

from okam.security import Key
from okam.security import Signer

class TestKeyMethods(unittest.TestCase):

    def test_sign(self):
        string = 'hello, world!'

        signer = Signer(Key.generate())

        signed = signer.sign('hello, world!')

        self.assertEqual(len(string) + Signer.MAC_LENGTH, len(signed))

        self.assertEqual(string, signed[Signer.MAC_LENGTH:])

    def test_validate(self):
        string = 'hello, world!'

        signer = Signer(Key.generate())

        signed = signer.sign('hello, world!')

        self.assertEqual(string, signer.validate(signed))

        signer = Signer(Key.generate())

        self.assertEqual(False, signer.validate(signed))

    def test_validate_with_php_signed_string(self):
        key = 'hex:8e0cafb6032544502662b396dd8f22c847031b2e9b578bb514755a5825205d38'

        signer = Signer(Key.decode(key))

        self.assertEqual('foobar', signer.validate('4d72902b15eac7808fb11816643f425cc4e5a11bccf3413e01e9c4983b70ea85foobar'))

if __name__ == '__main__':
    unittest.main()
