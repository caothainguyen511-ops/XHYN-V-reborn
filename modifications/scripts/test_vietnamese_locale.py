#!/usr/bin/env python3
"""Host checks for the Vietnamese launcher locale bundle."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
locale = ROOT / "assets/xhyn-locale-vi.json"
data = json.loads(locale.read_text(encoding="utf-8"))
assert len(data) >= 50, f"Expected a useful Vietnamese dictionary, got {len(data)} entries"
assert all(isinstance(k, str) and k and isinstance(v, str) and v for k, v in data.items())
assert data["Language"] == "Ngôn ngữ"
assert data["Close"] == "Đóng"
assert data["Menu and game language"] == "Ngôn ngữ menu và trò chơi"
source = (ROOT / "java/com/gtavsource/android/RebornLocale.java").read_text()
assert '"vi"' in source and '"Tiếng Việt"' in source
hooks = (ROOT / "scripts/apply_hooks.py").read_text()
assert "locale_source=R/'assets/xhyn-locale-vi.json'" in hooks
assert "locale_target=D/'assets/xhyn-locale-vi.json'" in hooks
print(f"PASS: {len(data)} Vietnamese strings; language selector and APK asset-copy hook are present")
