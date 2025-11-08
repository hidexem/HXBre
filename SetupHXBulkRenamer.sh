
# -------------------------------
# Code Setup By 𝗘𝗺𝘁𝗶𝗮𝗿 𝗠𝗮𝗺𝘂𝗻
# -------------------------------
REPO_URL="https://github.com/hidexem/HXBre.git"
REPO_NAME=$(basename $REPO_URL .git)
REPO_PATH="$HOME/$REPO_NAME"


echo "🔧 Installing Git and Python..."
pkg install git python -y


echo "📦 Upgrading pip..."
python -m ensurepip
python -m pip install --upgrade pip setuptools wheel


if [ -d "$REPO_PATH" ]; then
    echo "📁 Repo exists. Pulling latest updates..."
    cd $REPO_PATH
    git fetch origin
    git reset --hard origin/main
else
    echo "📥 Cloning GitHub repository..."
    git clone $REPO_URL $REPO_PATH
    cd $REPO_PATH
fi


echo "📦 Installing Python packages..."
python - <<END
import subprocess
import sys

packages = ["tqdm", "requests"]

for pkg in packages:
    print(f"📦 Installing {pkg}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", pkg])
END


echo "🚀 Running HxBulkRenamer..."
clear
python HxBulkRenamer.py

echo "✅ Setup & Execution Completed!"
read -p "Press Enter to Exit..."
