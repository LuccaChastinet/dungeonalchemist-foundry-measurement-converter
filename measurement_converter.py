import json
import os

# ===============================
# ⚙️ CONFIGURATION SECTION
# ===============================

# Folder path (default: current folder)
folder_path = os.path.dirname(os.path.abspath(__file__))

# New values you want to set
NEW_GRID_UNITS = "m"
NEW_GRID_DISTANCE = 1.5
NEW_LIGHT_DIM = 9.0
NEW_LIGHT_BRIGHT = 4.5

# ===============================
# 🧠 MAIN SCRIPT
# ===============================

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        print(f"🔍 Processing: {filename}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            modified = False

            # --- Update gridUnits ---
            if data.get("gridUnits") != NEW_GRID_UNITS:
                data["gridUnits"] = NEW_GRID_UNITS
                modified = True

            # --- Update gridDistance ---
            if data.get("gridDistance") != NEW_GRID_DISTANCE:
                data["gridDistance"] = NEW_GRID_DISTANCE
                modified = True

            # --- Update lights list ---
            if "lights" in data and isinstance(data["lights"], list):
                for light in data["lights"]:
                    if isinstance(light, dict):
                        if light.get("dim") != NEW_LIGHT_DIM or light.get("bright") != NEW_LIGHT_BRIGHT:
                            light["dim"] = NEW_LIGHT_DIM
                            light["bright"] = NEW_LIGHT_BRIGHT
                            modified = True

            # --- Save only if there were changes ---
            if modified:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"✅ Updated: {filename}")
            else:
                print(f"⚙️ No changes needed: {filename}")

        except json.JSONDecodeError:
            print(f"❌ Skipped (invalid JSON): {filename}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
