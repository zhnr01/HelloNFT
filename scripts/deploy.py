import os
from dotenv import load_dotenv
from ape import project, accounts

load_dotenv()

def main():
    account = os.getenv("MY_ACCOUNT")
    if not account:
        raise ValueError("MY_ACCOUNT is not set in .env")
    acct = accounts.load(account)

    nft_name = os.getenv("NFT_NAME")
    nft_symbol = os.getenv("NFT_SYMBOL")
    base_url = os.getenv("BASE_URL")

    if not nft_name or not nft_symbol or not base_url:
        raise ValueError("One or more NFT environment variables are missing in .env")

    contract = acct.deploy(
        project.VerySimpleNFT,
        nft_name,
        nft_symbol,
        base_url
    )

    print(f"Contract deployed at: {contract.address}")
