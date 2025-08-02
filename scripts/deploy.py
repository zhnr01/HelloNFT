from ape import accounts, project

def main():
    acct = accounts.load("dev") 
    acct.set_autosign(True)
    contract = acct.deploy(
        project.VerySimpleNFT  
    )
    print(f"Deployed at {contract.address}")
