from RSA import KeyGen

print("/#/ arguments needed are : -pq 'lock1' 'lock2' -e 'public key'")

keygen_cli = KeyGen()
keygen_cli.generateKeys()
keygen_cli.print_in_cli()