# Validation Log Analyzer

A Python-based modular framework to parse hardware validation 
test logs, extract test results, and generate summary reports 
with pass/fail statistics and CSV export.

## Author
Megha U — Platform Validation Engineer

## Files
- `log_analyser.py`    — basic version (string parsing)
- `log_analyser_v2.py` — modular version (regex + functions)

## Features
- Parses validation log files (.txt / .log)
- Extracts timestamp, status, test name, and message
- Counts PASS / FAIL / ERROR / WARN using Counter
- Calculates pass rate and fail rate
- Exports results to CSV report
- Modular design — each function does one job

## How to Run
1. Clone the repo
2. Add your log file to the `logs/` folder
3. Run basic version:
   python log_analyser.py
4. Run modular version:
   python log_analyser_v2.py
## Sample Output
========================================
      SUMMARISED REPORT
========================================
Total Tests : 10
Pass        : 3
Fail        : 4
Error       : 2
Warning     : 1
Pass Rate   : 30.0%
Fail Rate   : 40.0%
========================================
CSV report saved!

## Tech Stack
- Python 3
- re (Regex)
- csv module
- collections.Counter
- File I/O, String Parsing

## Use Case
Built to automate manual log review during hardware validation
and HLK certification testing on Intel SoC platforms.