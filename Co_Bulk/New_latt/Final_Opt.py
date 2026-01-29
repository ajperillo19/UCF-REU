
import glob
import re
import csv

# 1) Find all matching files
files = sorted(glob.glob("C??Optml_params.txt"))

# 2) Prepare regex patterns 
patterns = {
    "Volume":    re.compile(r"Optimal Volume.*:\s*([-\d\.E+]+)"),
    "Energy":    re.compile(r"Total Energy.*:\s*([-\d\.E+]+)"),
    "BulkMod":   re.compile(r"Bulk Modulus.*:\s*([-\d\.E+]+)"),
    "Lattice":   re.compile(r"Optimal lattice constant.*:\s*([-\d\.E+]+)"),
}

# 3) Data storage
data = []

for fname in files:
    # Extract the label (e.g. "C01" from "C01Optml_params.txt")
    label = fname[:3]
    with open(fname) as f:
        text = f.read()
    row = {"Label": label}
    # Apply each regex
    for key, pat in patterns.items():
        m = pat.search(text)
        if m:
            row[key] = float(m.group(1))
        else:
            row[key] = None
            print(f"⚠️  {key} not found in {fname}")
    data.append(row)


# 5) Write to CSV for analysis
with open("summary.csv", "w", newline="") as csvfile:
    fieldnames = ["Label", "Volume", "Energy", "BulkMod", "Lattice"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print("\nWrote summary.csv")

