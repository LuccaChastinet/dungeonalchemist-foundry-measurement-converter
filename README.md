# 🧭 Dungeon Alchemist → FoundryVTT Metric Converter

A simple and configurable **Python tool** for converting **Dungeon Alchemist (DA)** FoundryVTT exports to your preferred **system of measurement** (like Metric).

This script was made to help the community easily switch from feet-based maps to meters (or any other unit system) without tedious manual edits.

---

## ⚙️ What It Does

* 🔁 **Convert units:** Change the system from **feet (ft)** to **meters (m)** — or any unit you want.
* 📏 **Adjust grid size:** Modify the **grid distance** (e.g., from `5.0` to `1.5`).
* 💡 **Resize light sources:** Update **light radius** (`dim` and `bright`) for all light objects in your exported maps.
* 📂 **Batch process:** Automatically scans **every `.json` file** in its folder and applies your chosen changes.

---

## 🧠 How It Works

1. **Export from Dungeon Alchemist** using the *FoundryVTT Export* option.
2. **Place this script** in the same folder as your exported `.json` files.
3. **Edit the configuration section** at the top of the script:

   ```python
   NEW_GRID_UNITS = "m"
   NEW_GRID_DISTANCE = 1.5
   NEW_LIGHT_DIM = 9.0
   NEW_LIGHT_BRIGHT = 4.5
   ```
4. **Run the script**:

   ```bash
   python measurement_converter.py
   ```
5. **Import into FoundryVTT** using Dungeon Alchemist’s official guide:
   👉 [https://www.dungeonalchemist.com/import-to-foundry](https://www.dungeonalchemist.com/import-to-foundry)

---

## 🪄 Example Flow

```
Dungeon Alchemist Export → Run Script in Folder → Import into FoundryVTT
```

---

## 📬 Interested?

If this sounds useful, feel free to **open an issue**, **star the repo**, or **send me a message**!
I’ll be happy to share and collaborate with anyone who wants to expand or improve the tool.
