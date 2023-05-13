import sys
import math

import sys


class CliArgs:

    def __init__(self):
        # * Default values
        self.P = 1009  # ? This is the first value of the Lock
        self.Q = 2741  # ? This is the second value of the Lock
        self.E = 1  # ? This is the public key
        self.Phi = 1
        self.N = 1
        self.digest = 1
        self.message = 1
        self.key = 1

    # ! Getting the Lock from the system arguments
    def PQ_args(self):
        if '-pq' in sys.argv:
            pq_index = sys.argv.index('-pq')
            pq_index += 1
            self.P = int(sys.argv[pq_index])
            pq_index += 1
            self.Q = int(sys.argv[pq_index])
        else:
            print('you must provide p and q arguments using the -pq flag...')
            sys.exit(1)

    # ! Getting the Public Key value from the system arguments
    def E_args(self):
        if '-e' in sys.argv:
            e_index = sys.argv.index('-e')
            e_index += 1
            self.E = int(sys.argv[e_index])
        else:
            print('you must provide a public key argument using the -e flag...')

    # ! Getting the Digest value from the system arguments
    def digest_args(self):
        if '-digest' in sys.argv:
            digest_index = sys.argv.index('-digest')
            digest_index += 1
            self.digest = int(sys.argv[digest_index])
        else:
            print('you must provide a digest argument using the -digest flag...')

    def key_args(self):
        if '--key' in sys.argv:
            key_index = sys.argv.index('--key')
            key_index += 1
            self.key = int(sys.argv[key_index])
        else:
            print('you must provide a key argument using the --key flag...')

    def msg_args(self):
        if '-m' in sys.argv:
            msg_index = sys.argv.index('-m')
            msg_index += 1
            self.msg = int(sys.argv[msg_index])
        else:
            print('you must provide a message argument using the -m flag...')

    # ! Getting the Phi Value
    @property
    def getPhi(self):
        self.Phi = (self.P - 1) * (self.Q - 1) + 1
        return self.Phi

    # ! Getting the Product of P and Q
    @property
    def getN(self):
        self.N = self.P * self.Q
        return self.N

    # ! Getters of the values
    @property
    def getP(self):
        return self.P

    @property
    def getQ(self):
        return self.Q

    @property
    def getE(self):
        return self.E

    @property
    def getDigest(self):
        return self.digest

    @property
    def getKey(self):
        return self.key

    @property
    def getMessage(self):
        return self.message




class RSA:
    digest = 1
    key = 1
    message = 1

    def __init__(self):
        self.cli_args = CliArgs()

    def crypt(self):
        # ? The Crypt function is for both encryption and decryption purposes
        self.cli_args.digest_args()
        self.cli_args.key_args()
        self.cli_args.msg_args()
        self.digest = self.cli_args.getDigest()
        self.key = self.cli_args.getKey()
        self.message = self.cli_args.getMessage()

        exponent = self.message ** self.key
        encrypted_message = exponent % self.digest
        print('Your de/encrypted message :: ' + str(encrypted_message))


class KeyGen:
    # ? This is the private key and public key
    private_key = 1
    public_key = 1
    digest = 1

    def __init__(self):
        self.cli_args = CliArgs()

    def isPrime(cls, num):
        # ? Checking if a number is even
        if (num != 2 and num % 2 == 0) or num <= 1:
            return False

        sqrt = int(math.sqrt(num)) + 1

        # ? Check for primality
        for divisor in range(3, sqrt, 2):
            if num % divisor == 0:
                return False
        # ? Else its a Prime
        return True

    def generateKeys(self):
        # ? First :  getting PQ from cli
        self.cli_args.PQ_args()
        # ? Second : getting Public Key from cli
        self.cli_args.E_args()
        self.public_key = self.cli_args.getE()

        # ? Third :  getting the product
        self.digest = self.cli_args.getN()
        # ? Fourth :  getting Phi
        Phi = self.cli_args.getPhi()

        # ? Fifth :  calculating the private key
        product = self.public_key * self.private_key
        # ? Algorithm
        while product != Phi:
            self.public_key += 1
            self.private_key = Phi / self.public_key
            product = self.public_key * self.private_key

    def print_in_cli(self):
        self.generateKeys()
        print("Public Key == " + str(self.public_key))
        print("Private Key == " + str(self.private_key))
        print('Digest == ' + str(self.digest))
