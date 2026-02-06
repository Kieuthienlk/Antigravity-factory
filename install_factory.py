import os
import zipfile
import sys
from pathlib import Path

def install_factory():
    print("🏭 Installing Antigravity Factory...")
    
    current_dir = Path.cwd()
    agent_dir = current_dir / ".agent"
    
    if agent_dir.exists():
        print("⚠️  .agent directory already exists. Skipping installation to avoid overwrite.")
        return

    # 1. Install Core
    core_zip = Path("factory-core.zip")
    if core_zip.exists():
        print(f"📦 Installing Core from {core_zip}...")
        try:
            with zipfile.ZipFile(core_zip, 'r') as zip_ref:
                zip_ref.extractall(current_dir)
        except Exception as e:
            print(f"❌ Failed to extract core: {e}")
            return
    else:
        print("❌ Error: factory-core.zip not found.")
        return

    # 2. Install Skills Parts
    skill_parts = sorted(current_dir.glob("factory-skills-part*.zip"))
    if not skill_parts:
        print("⚠️  No skill parts found. Factory will be limited.")
    
    for part in skill_parts:
        print(f"📦 Installing Skills from {part.name}...")
        try:
            with zipfile.ZipFile(part, 'r') as zip_ref:
                zip_ref.extractall(current_dir)
        except Exception as e:
            print(f"❌ Failed to extract {part.name}: {e}")

    print("✅ Factory Core installed successfully!")
    print("🚀 Run 'python .agent/scripts/verify_all.py' to check status.")

if __name__ == "__main__":
    install_factory()
