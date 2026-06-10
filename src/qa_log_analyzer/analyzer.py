from pathlib import Path


def analyze_log(file_path: str) -> dict:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {file_path}")

    total_lines = 0
    errors = 0
    warnings = 0
    failures = 0
    exceptions = 0
    timeouts = 0

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1
            upper_line = line.upper()

            if "ERROR" in upper_line:
                errors += 1

            if "WARN" in upper_line:
                warnings += 1

            if "FAIL" in upper_line:
                failures += 1

            if "EXCEPTION" in upper_line:
                exceptions += 1

            if "TIMEOUT" in upper_line:
                timeouts += 1

    status = "FAILED" if errors or failures or exceptions or timeouts else "PASSED"

    return {
        "total_lines": total_lines,
        "errors": errors,
        "warnings": warnings,
        "failures": failures,
        "exceptions": exceptions,
        "timeouts": timeouts,
        "status": status,
    }