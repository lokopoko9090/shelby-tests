# 🚀 Shelby Testnet Blob Storage Tester

**Professional test suite for Shelby decentralized blob storage on Aptos (Shelbynet)**

Clean, reliable and well-documented Python script for testing upload/download performance and content integrity on **Shelby Testnet**.

---

## ✨ Features

- ✅ Automatic unique blob naming with timestamp
- ✅ Upload with customizable expiration (`--expiration tomorrow`)
- ✅ Download with force overwrite
- ✅ Full content verification (original vs downloaded)
- ✅ Detailed timing (upload + download)
- ✅ Automatic cleanup of temporary files
- ✅ Clean English output with emojis and links
- ✅ Easy wallet configuration
- ✅ `.gitignore` included

---

## 📊 Latest Test Results (Example)

| Operation     | Time     | Status          | Content Check     |
|---------------|----------|-----------------|-------------------|
| Upload        | ~9-12s   | ✅ Success      | -                 |
| Download      | ~4-6s    | ✅ Success      | ✅ Matches        |

**Network**: `shelbynet` (Shelby Testnet)  
**Location**: Ivano-Frankivsk, Ukraine 🇺🇦

---

## 🛠 Requirements

- Python 3.8 or higher
- Node.js + npm
- Shelby CLI: `npm install -g @shelby-protocol/cli`
- Configured Shelby account on **shelbynet** (`shelby init`)

Official Docs: [https://docs.shelby.xyz/tools/cli](https://docs.shelby.xyz/tools/cli)

---

## 🚀 Quick Start

```bash
git clone https://github.com/lokopoko9090/shelby-tests.git
cd shelby-tests
python shelby_test.py
