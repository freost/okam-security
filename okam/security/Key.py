import os

class Key:

    @staticmethod
    def encode(data: bytes) -> str:
        return 'hex:%s' % (data.hex())

    @staticmethod
    def decode(string: str) -> bytes:
        if string.find('hex:') == 0:
            return bytes.fromhex(string[4:])
        raise RuntimeError('Unable to decode key: "%s".' % (string))

    @staticmethod
    def generate(length: int = 32) -> bytes:
        return os.urandom(length)

    @staticmethod
    def generate_encoded(length: int = 32) -> str:
        return Key.encode(Key.generate(length))
