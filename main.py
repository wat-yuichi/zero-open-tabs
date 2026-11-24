from pathlib import Path


TAB_COUNT = "0"
output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(TAB_COUNT, encoding="utf-8")
