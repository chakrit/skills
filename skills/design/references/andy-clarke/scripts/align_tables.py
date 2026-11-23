"""Align the pipes of every Markdown table in a file, in place.

Usage: python3 align_tables.py <file.md>
"""
import sys


def is_row(line):
    return line.startswith("|") and line.rstrip().endswith("|")


def cells(line):
    return [c.strip() for c in line.strip()[1:-1].split("|")]


def is_rule(row):
    return all(c and set(c) <= set("-:") for c in row)


def format_table(lines):
    rows = [cells(l) for l in lines]
    width = [0] * max(len(r) for r in rows)
    for r in rows:
        if is_rule(r):
            continue
        for i, c in enumerate(r):
            width[i] = max(width[i], len(c), 3)
    out = []
    for r in rows:
        r = r + [""] * (len(width) - len(r))
        if is_rule(r):
            out.append("|" + "|".join("-" * (w + 2) for w in width) + "|")
        else:
            out.append("| " + " | ".join(c.ljust(w) for c, w in zip(r, width)) + " |")
    return out


def main(path):
    text = open(path, encoding="utf-8").read().split("\n")
    result, block = [], []
    for line in text + [""]:
        if is_row(line):
            block.append(line)
            continue
        if block:
            result.extend(format_table(block))
            block = []
        result.append(line)
    open(path, "w", encoding="utf-8").write("\n".join(result[:-1]))


main(sys.argv[1])
