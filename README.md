# Validation Log Analyzer

A Python tool to parse validation test logs, extract test results,
and generate a summary report with pass/fail statistics.

## Author
Megha U — Platform Validation Engineer

## Features
- Parses validation log files (.txt / .log)
- Extracts timestamp, status, test name, and message
- Counts PASS / FAIL / ERROR / WARN results
- Calculates pass rate
- Exports results to CSV report

## How to Run
1. Clone the repo
2. Add your log file to the `logs/` folder
3. Run:
   python log_analyser.py

## Sample Output
========================================
    VALIDATION LOG ANALYSIS REPORT
========================================

PASS        : 3
FAIL        : 4
ERROR       : 2
WARN        : 1
TOTAL TESTS : 10
PASS RATE   : 30.0%
========================================
report.csv saved!

## Tech Stack
- Python 3
- csv module
- File I/O
- String parsing

## Use Case
Built to automate manual log review during hardware validation
and HLK certification testing on Intel SoC platforms.