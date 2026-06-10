from qa_log_analyzer.analyzer import analyze_log


def test_analyze_log():
    report = analyze_log("sample_logs/app.log")

    assert report["errors"] == 2
    assert report["warnings"] == 1
    assert report["failures"] == 3
    assert report["exceptions"] == 1
    assert report["timeouts"] == 2
    assert report["status"] == "FAILED"