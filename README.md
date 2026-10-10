# Urtuk: The Desolation — Mutators, Upkeep & Unlocks (unofficial)

An unofficial mod package for **Urtuk: The Desolation**, assembled from previously prepared game-class patches. **Tested game version:** `1.0.0+91` is the version of the saves these patches were used alongside; compatibility with other game versions is **not verified**.

## Features

- **Mutator absorption interval:** low / normal / always rates -> **4 battles**. Non-absorbable (`none`) stays blocked.
- **Mutator absorption cap:** class-definition default cap **15** (not 20).
- **Special weekly wages:** zero alcohol and blood requirements for special characters from the patched event repositories.
- **FleshConsumer:** no periodic flesh upkeep or corresponding starvation penalty.
- **Starting unlocks:** global progress initialized with zone/difficulty unlock values **99**, and Permon faction unlocked (for new/default progress).
- **Trilium wages remain unchanged.**

**Not included:** 1000 starting medicine, healing adjustments, Victor, arena/elite events, secret monarch allies, save edits.

## Install (manual, Windows)

1. Close the game and back up the original `desktop-1.0.jar` (or the appropriate game JAR).
2. Open the JAR in 7-Zip.
3. Inside this archive, open `patch/` and drag **only** its `kaleta` folder into the root of the game JAR. Confirm replacement of **6 `.class` files**.
4. Run the game and test on a **new campaign**. Existing save-specific caps/progress may be retained.
5. If the game crashes, restore the original JAR from your backup.

For convenience you can also run `python install.py path/to/desktop-1.0.jar`. The script backs up the JAR before patching, verifies game classes are present, and replaces only the six targets.

## Uninstall

Restore your original JAR backup. Do not copy the entire `backup/` directory into the game; there is no bundled universal backup because it must match **your specific game build**.

## Limitations / distribution

- **Not affiliated with the game developer.** These are replacement compiled game classes, *not* original source code; distributing game `.class` files may require permission from the game's rights holder. Obtain permission before publicly publishing the `patch/` folder.
- Game compatibility, anti-cheat considerations, and interactions with other mods are not guaranteed.
- This repository does **not** contain the full game or assets. No open-source license is claimed for the included game classes.
- Patches are provided as assembled from existing local archives, not independently end-to-end playtested in this exact combination.

## Technical manifest

See `manifest.json` for SHA-256 checksums of all 6 patched `.class` files.
