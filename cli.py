import sys
import argparse
import subprocess

parser = argparse.ArgumentParser()

## Adding the available flags and their corresponding script files
parser.add_argument('--key_gen','--option_keygen',action="store_true", help="Generate the public and private keys...")
parser.add_argument('--rsa','--option_rsa',action="store_true",help="En/Decrypt the giving input using keys...")
parser.add_argument('--helper','--option_helper',action="store_true",help="Adding helper for the user of the cli")
# Parse the command-line arguments
args = parser.parse_args()

# Execute the script based on the flag
if args.helper:
    subprocess.run(['python', 'helper.py'])
elif args.rsa:
    subprocess.run(['python', 'rsa_cli.py'])
elif args.key_gen:
    subprocess.run(['python', 'key_gen_cli.py'])
else:
    print('No option selected...')
    sys.exit(1)
