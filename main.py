import getpass
from os import getenv

from passlib.context import CryptContext

from ledger import block_chain

pwd_context = CryptContext(schemes=['argon2'], deprecated="auto")

jakes_password = getpass.getpass("jake enter password: ")
vincents_password = getpass.getpass("vincent enter password: ")
jointed_hashed_password = pwd_context.hash(jakes_password + vincents_password)

for data, key in block_chain.items():
    if pwd_context.verify(jakes_password + vincents_password, key):
        print(data)
