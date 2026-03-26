# Shelby Testnet Blob Storage Monitor

Simple tests and monitoring for Shelby (shelbynet) blob upload and download.

## Test Results (March 26, 2026)

**Network:** shelbynet (Testnet)  
**Account:** `0x2b2b059354ff1d14b0ac941174057c3824aecbde0c7ff173048c11cfd53dfbd6`

### Performance
- **Upload time**: ~10.09 seconds
- **Download time**: ~0.6 seconds
- **File size**: small text file
- **Expiration**: 1 day

### Commands Used
```bash
shelby upload test-shelby.txt my-first-blob.txt --expiration "tomorrow" --assume-yes

shelby download my-first-blob.txt downloaded-test.txt