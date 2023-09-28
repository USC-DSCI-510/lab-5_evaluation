import csv
import os
from collections import Counter, defaultdict
from statistics import mean
from typing import List, Tuple

import numpy as np


def analyse_student_data(
    filename: str,
) -> Tuple[int, dict, dict, str, float, List[Tuple[float, str]]]:
    if not os.path.exists(filename):
        raise Exception("Invalid input")

    csv_data = defaultdict(list)
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            for k, v in line.items():
                # convert data types
                if k in ("MathScore", "ReadingScore", "WritingScore"):
                    v = int(v)
                csv_data[k].append(v)

    total_num = len(csv_data["Gender"])

    gender_count = dict(Counter(csv_data["Gender"]))

    track = defaultdict(list)
    for idx, k in enumerate(csv_data["Track"]):
        track[k].append(csv_data["MathScore"][idx])
    track = {k: round(mean(v), 2) for k, v in track.items()}

    parental_education = sorted(Counter(csv_data["ParentalEducation"]).items(), key=lambda x: (-x[1], x[0]))[0][0]

    reading_score = round(mean(csv_data["ReadingScore"]), 2)

    writing_score = []
    max_writing_score = max(csv_data["WritingScore"])
    for gender, score in zip(csv_data["Gender"], csv_data["WritingScore"]):
        if score == max_writing_score:
            writing_score.append((score, gender))

    return total_num, gender_count, track, parental_education, reading_score, writing_score


def analyse_bank_data(filename: str) -> Tuple[float, int, float]:
    if not os.path.exists(filename):
        raise Exception("Invalid input")

    csv_data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            line["Amount"] = float(line["Amount"])
            csv_data.append(line)

    q1, q2, q3 = 0, 0, 0
    for row in csv_data:
        if row["Description"] == "Phone bill":
            q1 = max(q1, row["Amount"])

        if row["Description"] == "Rent":
            q2 += 1

        if row["Type"] == "Withdrawal":
            q3 -= row["Amount"]
        elif row["Type"] == "Deposit":
            q3 += row["Amount"]

    return round(q1, 2), q2, round(q3, 2)
