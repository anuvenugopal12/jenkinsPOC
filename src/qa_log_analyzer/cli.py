import argparse
import sys

from qa_log_analyzer.analyzer import analyze_log
from qa_log_analyzer.report_writer import write_json_report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analyze QA logs and generate a JSON report."
    )

    parser.add_argument(
        "log_file",
        help="Path to the log file to analyze"
    )

    parser.add_argument(
        "--output",
        default="reports/report.json",
        help="Path to save the JSON report"
    )

    args = parser.parse_args()

    report = analyze_log(args.log_file)
    write_json_report(report, args.output)

    print(report)

    if report["status"] == "FAILED":
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())