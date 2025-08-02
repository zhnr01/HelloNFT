# HelloNFT
A simple NFT smart contract written in Vyper.

## NFT Deployment with Ape Framework (Vyper + Sepolia)

This guide explains how to set up the [Ape Framework](https://docs.apeworx.io/) for deploying an NFT smart contract written in Vyper to the **Sepolia testnet** using **Alchemy**.

---

## 1️⃣ Prerequisites

- **Python 3.10+** installed
- **pip** installed
- An **Alchemy account** ([Sign up here](https://www.alchemy.com/))
- A **MetaMask wallet** (for creating/importing accounts)
---

## 2️⃣ Install Ape Framework

```bash
# Install Ape
pip install eth-ape'[recommended-plugins]'
```
---

## 3️⃣ Set Up an Alchemy Project (Sepolia)

1. Go to [Alchemy Dashboard](https://dashboard.alchemy.com/).
2. Click **Create App**.
3. Select:

   * **Name**: NFT Deployment
   * **Chain**: Ethereum
   * **Network**: Sepolia
4. Once created, click **View Key** and copy your **API KEY** — it will look like:
---

## 4️⃣ Create or Import an Account in Ape

### Option 1: Create a new account

```bash
ape accounts create dev
```

You’ll be prompted to set a password.
Ape will generate and store the account securely.

### Option 2: Import an existing account (from MetaMask)

1. In MetaMask, **export your private key**.
2. In Ape:

```bash
ape accounts import dev
```

Paste your private key when asked.

---

## 5️⃣ Configure Ape for Sepolia + Alchemy

Edit `ape-config.yaml` in your project root:

```yaml
ethereum:
  sepolia:
    default_provider: alchemy
```

Set your Alchemy API key in environment variables (explained below).

---

## 6️⃣ Set Environment Variables

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

## 7️⃣ Compile the Contract

```bash
ape compile
```

---

## 8️⃣ Deploy to Sepolia

Run:

```bash
ape run deploy.py --network ethereum:sepolia:alchemy
```
