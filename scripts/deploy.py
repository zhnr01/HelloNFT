from ape import accounts, project

def main():
    acct = accounts.load("dev") 
    contract = acct.deploy(
        project.VerySimpleNFT  
    )
    print(f"✅ Deployed at {contract.address}")
