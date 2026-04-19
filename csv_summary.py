#!/usr/bin/env python3
"""Print a summary of each column in a CSV file."""

import csv
import sys
from collections import Counter


def summarize_csv(filepath):
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("CSV file is empty or has no data rows.")
        return

    columns = list(rows[0].keys())
    total_rows = len(rows)

    print(f"File: {filepath}")
    print(f"Total rows: {total_rows}")
    print(f"Columns: {len(columns)}")
    print("-" * 50)

    for col in columns:
        values = [row[col] for row in rows]
        non_empty = [v for v in values if v.strip() != ""]
        missing = total_rows - len(non_empty)

        numeric_values = []
        for v in non_empty:
            try:
                numeric_values.append(float(v))
            except ValueError:
                pass

        print(f"\nColumn: {col}")
        print(f"  Non-empty: {len(non_empty)} / {total_rows}  (missing: {missing})")

        if len(numeric_values) == len(non_empty) and numeric_values:
            print(f"  Type: numeric")
            print(f"  Min:  {min(numeric_values)}")
            print(f"  Max:  {max(numeric_values)}")
            print(f"  Mean: {sum(numeric_values) / len(numeric_values):.4f}")
        else:
            print(f"  Type: text")
            unique = set(non_empty)
            print(f"  Unique values: {len(unique)}")
            top = Counter(non_empty).most_common(5)
            print(f"  Top values: {top}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_csv>")
        sys.exit(1)
    summarize_csv(sys.argv[1])
