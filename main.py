from scanner import scan_directory
from analyzer import detect_size_anomalies
from reporter import generate_report
from utils import save_baseline, load_baseline
from utils import compare_with_baseline

directory = input("Enter directory path: ")

data = scan_directory(directory)
data = detect_size_anomalies(data)

baseline = load_baseline()

if baseline:
    data = compare_with_baseline(data, baseline)
else:
    print("No baseline found. Creating one.")

save_baseline(data)

df = generate_report(data)

print("Report generated: Forensic_Report.xlsx")