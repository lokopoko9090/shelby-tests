import subprocess
import time
import os
from datetime import datetime

print("🚀 Shelby Testnet Blob Storage Test")
print("=" * 60)
print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Створюємо тестовий файл
test_content = f"Test file from Ivano-Frankivsk, Ukraine. Generated at: {datetime.now()}"
with open("test-shelby.txt", "w", encoding="utf-8") as f:
    f.write(test_content)

print("📄 Test file created (test-shelby.txt)")

# Upload
print("\n📤 Uploading to Shelby shelbynet...")
start = time.time()

try:
    result = subprocess.run([
        "shelby", "upload", "test-shelby.txt", "my-test-blob.txt",
        "--expiration", "tomorrow", "--assume-yes"
    ], capture_output=True, text=True, timeout=60)

    upload_time = time.time() - start

    if result.returncode == 0:
        print(f"✅ Upload successful! Time: {upload_time:.2f} seconds")
        print(result.stdout.strip())
    else:
        print("❌ Upload failed:")
        print(result.stderr)

except Exception as e:
    print(f"❌ Error during upload: {e}")

# Download
print("\n📥 Downloading blob...")
start = time.time()

try:
    result = subprocess.run([
        "shelby", "download", "my-test-blob.txt", "downloaded-test.txt"
    ], capture_output=True, text=True, timeout=30)

    download_time = time.time() - start

    if result.returncode == 0:
        print(f"✅ Download successful! Time: {download_time:.2f} seconds")
        
        # Перевіряємо вміст
        with open("downloaded-test.txt", "r", encoding="utf-8") as f:
            content = f.read()
        print(f"📋 Downloaded content preview: {content[:100]}...")
        
    else:
        print("❌ Download failed:")
        print(result.stderr)

except Exception as e:
    print(f"❌ Error during download: {e}")

print("\n" + "=" * 60)
print("Test completed!")