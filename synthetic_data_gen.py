import random


def generate_bank_transaction_data(num_entries, file_path):
    types = ["Deposit", "Withdrawal", "Deposit"]
    descriptions = [
        "Salary",
        "Phone bill",
        "Zelle from friend",
        "Restaurant",
        "Entertainment",
        "Utilities",
        "Groceries",
        "Rent",
    ]

    with open(file_path, "w") as file:
        file.write("Type,Amount,Description\n")
        for _ in range(num_entries):
            entry = f"{random.choice(types)},{round(random.uniform(5, 10000), 2)},{random.choice(descriptions)}\n"
            file.write(entry)


def generate_student_performance_data(num_entries, file_path):
    genders = ["Male"]
    tracks = ["Track B", "Track C"]
    parental_education = ["Associate's Degree", "Bachelor's Degree"]

    with open(file_path, "w") as file:
        file.write("Gender,Track,ParentalEducation,MathScore,ReadingScore,WritingScore\n")
        for _ in range(num_entries):
            entry = f"{random.choice(genders)},{random.choice(tracks)},{random.choice(parental_education)},"
            entry += f"{random.randint(30, 100)},{random.randint(20, 100)},{random.randint(30, 100)}\n"
            file.write(entry)


# Generate bank transaction data
# generate_bank_transaction_data(10000, "data/bank/bank_transactions_test_21.csv")

# Generate student performance data
generate_student_performance_data(350, "data/student/student_performance_test_12.csv")
