import base64
from cryptography.fernet import Fernet  # type: ignore
from cryptography.hazmat.backends import default_backend  # type: ignore
from cryptography.hazmat.primitives import hashes  # type: ignore
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # type: ignore
from os import urandom
from typing import ByteString, Tuple, Optional


class ClamyFernet:
    """Fernet implementation by clamytoe

    Takes a bytestring as a password and derives a Fernet
    key from it. If a key is provided, that key will be used.

    :param password: ByteString of the password to use
    :param key: ByteString of the key to use, else defaults to None

    Other class variables that you should implement that are hard set:

    salt, algorithm, length, iterations, backend, and generate a base64
    urlsafe_b64encoded key using self.clf().
    """

    @property
    def kdf(self):
        """Derives the key from the password

        Uses PBKDF2HMAC to generate a secure key. This is where you will
        use the salt, algorithm, length, iterations, and backend variables.
        """
        pass

    @property
    def clf(self):
        """Generates a Fernet object

        Key that is derived from cryptogrophy's fermet.
        """
        pass

    def encrypt(self, message: str) -> ByteString:
        """Encrypts the message passed to it"""
        pass

    def decrypt(self, token: ByteString) -> str:
        """Decrypts the encrypted message passed to it"""
        pass