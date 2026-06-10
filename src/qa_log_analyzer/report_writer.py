import json
from pathlib import Path


def write_json_report(report: dict, output_path: str) -> None:
    path = Path(output_path)

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)