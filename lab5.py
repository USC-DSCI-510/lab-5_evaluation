import csv
from typing import List, Tuple


def analyse_student_data(
    filename: str,
) -> Tuple[int, dict, dict, str, float, List[Tuple[float, str]]]:
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        header = lines[0].strip().split(",")
        data = [line.strip().split(",") for line in lines[1:]]

        total_students = len(data)

        gender_count = {"Male": 0, "Female": 0}
        for row in data:
            gender_count[row[0]] += 1

        track_math = {}
        for row in data:
            track_math[row[1]] = track_math.get(row[1], [])
            track_math[row[1]].append(int(row[3]))

        average_math_score_by_track = {
            track: round(sum(scores) / len(scores), 2)
            for track, scores in track_math.items()
        }

        education_counts = {
            "Associate's Degree": 0,
            "Bachelor's Degree": 0,
            "High School": 0,
        }

        for row in data:
            education_counts[row[2]] += 1
        most_common_education = max(education_counts, key=education_counts.get)

        reading_scores = [int(row[4]) for row in data]
        average_reading_score = round(sum(reading_scores) / len(reading_scores), 2)

        max_writing_score_val = max([int(row[5]) for row in data])

        max_writing_scores = []
        for row in data:
            if int(row[5]) == max_writing_score_val:
                max_writing_score = (max_writing_score_val, row[0])
                max_writing_scores.append(max_writing_score)

        return (
            total_students,
            gender_count,
            average_math_score_by_track,
            most_common_education,
            average_reading_score,
            max_writing_scores,
        )
    except:
        raise Exception("Invalid File/filename")


def analyse_bank_data(filename: str) -> Tuple[float, int, float]:
    try:
        highest_phone_bill = 0.0
        rent_count = 0
        balance = 0.0

        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                transaction_type, amount, description = row
                amount = float(amount)

                if transaction_type == "Deposit":
                    balance += amount
                elif transaction_type == "Withdrawal":
                    balance -= amount

                if description == "Phone bill" and amount > highest_phone_bill:
                    highest_phone_bill = amount

                if description == "Rent":
                    rent_count += 1

        return round(highest_phone_bill, 2), rent_count, round(balance, 2)
    except:
        raise Exception("Invalid file/filename")


print(analyse_bank_data("bank_transactions_2.csv"))
