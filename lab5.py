import csv
from typing import List, Tuple


def unique_two_sum(nums: List[int], target: int) -> List[Tuple[int, int]]:
    try:
        num_indices = {}
        result = set()

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                for index in num_indices[complement]:
                    result.add((min(index, i), max(index, i)))
            if num in num_indices:
                num_indices[num].append(i)
            else:
                num_indices[num] = [i]

        return list(result)
    except:
        raise Exception("Invalid Input")


def analyse_student_data(file_name: str) -> Tuple[int, dict, dict, str, float, tuple]:
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()

        header = lines[0].strip().split(",")
        data = [line.strip().split(",") for line in lines[1:]]

        total_students = len(data)

        gender_count = {"Male": 0, "Female": 0}
        for row in data:
            gender_count[row[0]] += 1

        track_math = {"Track A": [], "Track B": [], "Track C": []}
        for row in data:
            track_math[row[1]].append(int(row[3]))
        average_math_score_by_track = {
            track: sum(scores) / len(scores) for track, scores in track_math.items()
        }

        education_counts = {
            "High School": 0,
            "Associate's Degree": 0,
            "Bachelor's Degree": 0,
        }
        for row in data:
            education_counts[row[2]] += 1
        most_common_education = max(education_counts, key=education_counts.get)

        reading_scores = [int(row[4]) for row in data]
        average_reading_score = sum(reading_scores) / len(reading_scores)

        max_writing_score_val = max([int(row[5]) for row in data])
        for row in data:
            if int(row[5]) == max_writing_score_val:
                max_writing_score = (max_writing_score_val, row[0])
                break

        return (
            total_students,
            gender_count,
            average_math_score_by_track,
            most_common_education,
            average_reading_score,
            max_writing_score,
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

        return highest_phone_bill, rent_count, balance
    except:
        raise Exception("Invalid file/filename")
