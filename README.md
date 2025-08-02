# HelloNFT
A simple NFT smart contract.

## Contract Features

This NFT contract is implemented in Vyper and follows the ERC‑721 standard.

### Main Features

- ERC‑721 compliant — Implements the standard NFT interface.
- ERC‑165 support — For interface detection.
- Minting — Only the contract minter can mint new tokens.
- Burning — Token owners (or approved addresses) can burn NFTs.
- Transfer & Safe Transfer — Supports both `transferFrom` and `safeTransferFrom`.
- Approval — Allows single token approval and operator approval for all tokens.
- Metadata Support:
  - `name` and `symbol` stored on‑chain.
  - `baseURL` used to generate `tokenURI`.
  - Token metadata follows `{baseURL}{tokenId}.json` format.
- Set Base URL — Minter can update the metadata base URL.

The smart contract is deployed on Sepolia testnet.

- Contract Address: `0x5b28067aFb45744559Da74Cf55Aa19a01f05e38f`
- Etherscan Link: [View on Sepolia Etherscan](https://sepolia.etherscan.io/address/0x5b28067aFb45744559Da74Cf55Aa19a01f05e38f)

---

## Metadata Hosting (Pinata Cloud)

This contract’s metadata is stored on IPFS and pinned using [Pinata Cloud](https://pinata.cloud/).

- Base URL (set at deployment):
```
ipfs://bafybeigjerexlbyz6q5ak5ad3bmz3r676j3i7picfs6zjwkhtkn5wogslq/
```

- Token Metadata format:
```
{baseURL}{tokenId}.json
```

Example for token ID 1:
```
ipfs://bafybeigjerexlbyz6q5ak5ad3bmz3r676j3i7picfs6zjwkhtkn5wogslq/1.json
```

- JSON Metadata Example:
```json
{
  "name": "Hello NFT #1",
  "description": "A sample NFT from the Hello NFT collection",
  "image": "ipfs://QmSomePinataImageHash/hellonft1.png",
  "attributes": [
    { "trait_type": "Background", "value": "Blue" },
    { "trait_type": "Eyes", "value": "Happy" }
  ]
}
```

---

## NFT Deployment with Ape Framework (Vyper + Sepolia)

This guide explains how to set up the [Ape Framework](https://docs.apeworx.io/) for deploying an NFT smart contract written in Vyper to the Sepolia testnet using Alchemy.

### Prerequisites

- Python 3.10+ installed
- pip installed
- An Alchemy account ([Sign up here](https://www.alchemy.com/))
- A MetaMask wallet (for creating/importing accounts)

---

### Install Ape Framework

```bash
# Create virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install Ape with recommended plugins
pip install eth-ape'[recommended-plugins]'
```

---

### Set Up an Alchemy Project (Sepolia)

1. Go to [Alchemy Dashboard](https://dashboard.alchemy.com/).
2. Click "Create App".
3. Select:
   - Name: NFT Deployment
   - Chain: Ethereum
   - Network: Sepolia
4. Once created, click "View Key" and copy your API KEY.

---

### Create or Import an Account in Ape

**Option 1: Create a new account**
```bash
ape accounts create dev
```
You’ll be prompted to set a password. Ape will generate and store the account securely.

**Option 2: Import an existing account (from MetaMask)**
1. In MetaMask, export your private key.
2. In Ape:
```bash
ape accounts import dev
```
Paste your private key when asked.

---

### Configure Ape for Sepolia + Alchemy

Edit `ape-config.yaml` in your project root:
```yaml
ethereum:
  sepolia:
    default_provider: alchemy
```
Set your Alchemy API key in environment variables as described below.

---

### Set Environment Variables

Create a `.env` file in your project root:
```env
# Ape account alias
MY_ACCOUNT=dev

# NFT details
NFT_NAME=Hello NFT
NFT_SYMBOL=HEL
BASE_URL=ipfs://bafybeigjerexlbyz6q5ak5ad3bmz3r676j3i7picfs6zjwkhtkn5wogslq/

# Alchemy API key
WEB3_ALCHEMY_API_KEY=your_alchemy_api_key_here
```

---

### Compile the Contract
```bash
ape compile
```

---

### Deploy to Sepolia
```bash
ape run deploy --network ethereum:sepolia:alchemy
```

---

## Contract Interaction Guide

Once the contract is deployed, you can interact with it using Ape Framework or any Web3 library (Web3.py, ethers.js, etc.).

### 1. Open Ape Console
```bash
ape console --network ethereum:sepolia:alchemy
```
Inside the console:
```python
from ape import Contract

# Replace with your deployed contract address
address = "0x5b28067aFb45744559Da74Cf55Aa19a01f05e38f"
contract = Contract(address)
```

### 2. Mint a New NFT
Only the minter (the address that deployed the contract) can mint.
```python
contract.mint("0xRecipientAddressHere", 1, sender=accounts.load("MY_ACCOUNT"))
```

### 3. Transfer an NFT
```python
contract.transferFrom(
    "0xFromAddressHere",
    "0xToAddressHere",
    1,
    sender=accounts.load("MY_ACCOUNT")
)
```

### 4. Safe Transfer
```python
contract.safeTransferFrom(
    "0xFromAddressHere",
    "0xToAddressHere",
    1,
    sender=accounts.load("MY_ACCOUNT")
)
```

### 5. Approve Another Address
```python
contract.approve(
    "0xApprovedAddressHere",
    1,
    sender=accounts.load("MY_ACCOUNT")
)
```

### 6. Approve an Operator for All Tokens
```python
contract.setApprovalForAll(
    "0xOperatorAddressHere",
    True,
    sender=accounts.load("MY_ACCOUNT")
)
```

### 7. Burn an NFT
```python
contract.burn(
    1,
    sender=accounts.load("MY_ACCOUNT")
)
```

### 8. View Token Metadata
```python
contract.tokenURI(1)
# Example: ipfs://.../1.json
```

### 9. Change Base Metadata URL
Only the minter can do this.
```python
contract.setBaseURL(
    "ipfs://new-ipfs-hash/",
    sender=accounts.load("MY_ACCOUNT")
)
```
