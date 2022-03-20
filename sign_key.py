import getpass
from os import getenv

from passlib.context import CryptContext

from ledger import block_chain
from public_keys import public_keys

pwd_context = CryptContext(schemes=['argon2'], deprecated="auto")

jakes_password = getpass.getpass("jake enter password: ")
vincents_password = getpass.getpass("vincent enter password: ")

jointed_hashed_password = False
if pwd_context.verify(jakes_password, public_keys['jake']):
    if pwd_context.verify(vincents_password, public_keys['vincent']):
        jointed_hashed_password = pwd_context.hash(jakes_password + vincents_password)
        print(jointed_hashed_password)
        exit()

print("Passwords incorrect")
