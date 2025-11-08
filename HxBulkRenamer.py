import os
import subprocess
import sys
import time

# ---------- AUTO INSTALL REQUESTS ----------
try:
    import requests
except ImportError:
    print("📦 'requests' package not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

# ---------- AUTO INSTALL TQDM ----------
try:
    from tqdm import tqdm
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tqdm"])
    from tqdm import tqdm

# ---------- VERSION ----------
VERSION = "V1.2"
GITHUB_VERSION_URL = "https://raw.githubusercontent.com/hidexem/HXUpdates/main/HXbreUpdate.txt"



# ---------- HEADER ----------
print()
print()
print("╺" * 40)
print("📂 HX Bulk File Renamer Pro ")
print("👨‍💻 Developer: 𝗘𝗺𝘁𝗶𝗮𝗿 𝗠𝗮𝗺𝘂𝗻")
print("╺" * 40)
# ---------- VERSION CHECK ----------
try:
    latest_version = requests.get(GITHUB_VERSION_URL, timeout=5).text.strip()
    print(f"🔢 Current version: {VERSION}")
    print(f"🌐 Latest version: {latest_version}")
    if latest_version != VERSION:
        print("⚠️ Update available! Type 'Update' to fetch latest version")
    else:
        print("✅ You are useing the latest version")
except:
    print("⚠️ Could not check latest version online")
time.sleep(0.5)
print("🔄 Tip: Type 'Update' anytime to fetch\n the latest version")
print("▸" * 40)
print()
print()
# ---------- USER INPUT ----------
TARGET_DIR = input("📁 Enter Target Folder Path : ").strip()
if TARGET_DIR.lower() == "Update":
    print("\n🔄 Updating script from GitHub...")
    repo_path = os.path.dirname(os.path.abspath(__file__))
    os.system(f"cd {repo_path} && git fetch origin && git reset --hard origin/main && clear")
    print("✅ Update complete ! Relaunching the script...")
    os.system(f"cd {repo_path} && python {os.path.basename(__file__)}")
    exit()

NEW_EXT = input("🌌 Enter New Extension (e.g. .png): ").strip()
if not NEW_EXT.startswith("."):
    NEW_EXT = "." + NEW_EXT

if not os.path.exists(TARGET_DIR):
    print(f"\n❌ Path not found: {TARGET_DIR}")
    exit()

# ---------- HELPER FUNCTION ----------
def get_unique_name(folder, base_name, ext):
    """
    Conflict হলে sequential number (1,2,3...) যোগ করে unique name তৈরি করবে
    bracket ছাড়া
    """
    new_name = f"{base_name}{ext}"
    counter = 1
    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{base_name}{counter}{ext}"
        counter += 1
    return os.path.join(folder, new_name)

# ---------- COLLECT FILES ----------
all_files = []
for root, dirs, files in os.walk(TARGET_DIR):
    for file in files:
        # Ignore files that already have the target extension
        if file.endswith(NEW_EXT):
            continue
        all_files.append((root, file))

total_files = len(all_files)
if total_files == 0:
    print("\n⚠️ No files found in the Target Directory.")
    exit()

# ---------- MAIN PROCESS ----------
print()
print(f"\n🔍 {total_files} Files Detected. \nStarting Rename Process...\n")
count = 0

for root, file in tqdm(all_files, desc="Processing", unit="file", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} [{elapsed} s]"):
    # Simulate processing):
    old_file = os.path.join(root, file)
    base_name = os.path.splitext(file)[0]  # remove old extension
    new_file = get_unique_name(root, base_name, NEW_EXT)  # sequential number if conflict
    try:
        os.rename(old_file, new_file)
        count += 1
    except Exception as e:
        print(f"\n❌ Error renaming {file}: {e}")

# ---------- SUMMARY ----------
print()
print()
print("\n" + "⚊" * 40)
print(f"✅ Successfully Renamed {count} Files ")
print("Powered By ℍ𝕚𝕕𝕖𝕩𝔼𝕞")
print("⚊" * 40)
print()
print()
