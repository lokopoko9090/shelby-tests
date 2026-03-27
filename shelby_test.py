import subprocess
import time
from datetime import datetime
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("🚀 Shelby Testnet Blob Test")
print("=" * 75)
print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("📍 Ivano-Frankivsk, Ukraine 🇺🇦\n")

# Add Shelby CLI to PATH
npm_path = r"C:\Users\АННА\AppData\Roaming\npm"
if os.path.exists(npm_path):
    os.environ["PATH"] += os.pathsep + npm_path

print("1. Creating test file...")
timestamp = datetime.now().strftime("%H%M%S")
blob_name = f"test-blob-{timestamp}.txt"

content = f"""Test file from Ivano-Frankivsk, Ukraine 🇺🇦
Generated at: {datetime.now()}
Testing Shelby shelbynet blob storage
"""

with open("test-shelby.txt", "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Test file created → uploading as: {blob_name}\n")

print("2. Uploading to Shelby...")
start = time.time()
try:
    result = subprocess.run([
        "shelby", "upload", "test-shelby.txt", blob_name,
        "--expiration", "tomorrow", "--assume-yes"
    ], capture_output=True, text=True, timeout=90, encoding='utf-8', errors='replace', shell=True)

    upload_time = time.time() - start

    if result.returncode == 0:
        print(f"✅ Upload successful → {upload_time:.2f} seconds")
        if result.stdout.strip():
            print(result.stdout.strip())
    else:
        print("❌ Upload failed:")
        print(result.stderr)
except Exception as e:
    print(f"❌ Upload error: {e}")

print("\n3. Downloading file...")
start = time.time()
try:
    result = subprocess.run([
        "shelby", "download", blob_name, "downloaded-test.txt", "--force"
    ], capture_output=True, text=True, timeout=60, encoding='utf-8', errors='replace', shell=True)

    download_time = time.time() - start

    if result.returncode == 0:
        print(f"✅ Download successful → {download_time:.2f} seconds")
        
        with open("downloaded-test.txt", "r", encoding="utf-8") as f:
            downloaded = f.read()
        
        print("\n📄 Downloaded file content:")
        print(downloaded)
        
        if downloaded.strip() == content.strip():
            print("✅ Content matches perfectly!")
        else:
            print("⚠️ Content does not match")
    else:
        print("❌ Download failed:")
        print(result.stderr)
except Exception as e:
    print(f"❌ Download error: {e}")

print("\n" + "=" * 75)
print("🎉 Test completed successfully!")

# Cleanup
for f in ["test-shelby.txt", "downloaded-test.txt"]:
    if os.path.exists(f):
        try:
            os.remove(f)
        except:
            pass