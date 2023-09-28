import os
import pytest

from lab5 import analyse_student_data, analyse_bank_data

CURRENT_WORKING_DIR = os.getcwd()
DATA_DIR = os.path.join(CURRENT_WORKING_DIR, "data")


@pytest.mark.parametrize(
    "filename,ans",
    [
        (
            "student_performance.csv",
            (
                870,
                {"Male": 439, "Female": 431},
                {"Track C": 76.58, "Track B": 74.21, "Track A": 73.26},
                "Associate's Degree",
                74.18,
                [
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                ],
            ),
        ),
        (
            "student_performance_1.csv",
            (
                1000,
                {"Male": 469, "Female": 531},
                {"Track C": 74.82, "Track A": 74.47, "Track B": 73.4},
                "Bachelor's Degree",
                74.87,
                [
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Female"),
                ],
            ),
        ),
        (
            "student_performance_2.csv",
            (
                100,
                {"Male": 43, "Female": 57},
                {"Track A": 80.14, "Track B": 75.03, "Track C": 74.15},
                "Associate's Degree",
                76.08,
                [(99, "Female"), (99, "Male"), (99, "Male")],
            ),
        ),
        (
            "student_performance_3.csv",
            (
                4,
                {"Male": 3, "Female": 1},
                {"Track A": 75.0, "Track B": 88.0, "Track C": 60.0},
                "Associate's Degree",
                81.5,
                [(85, "Female"), (85, "Male")],
            ),
        ),
        (
            "student_performance_4.csv",
            (
                4,
                {"Male": 3, "Female": 1},
                {"Track B": 83.67, "Track C": 60.0},
                "Associate's Degree",
                81.5,
                [(85, "Female"), (85, "Male")],
            ),
        ),
    ],
)
@pytest.mark.timeout(0.1)
def test_analyse_student_data(filename, ans):
    filename = os.path.join(DATA_DIR, "student", filename)
    assert analyse_student_data(filename) == ans


@pytest.mark.parametrize(
    "filename,ans",
    [
        ("bank_transactions.csv", (297.65, 2, 8578.79)),
        ("bank_transactions_1.csv", (1963.97, 23, 39607.43)),
        ("bank_transactions_2.csv", (1814.31, 10, -4042.5)),
    ],
)
@pytest.mark.timeout(0.1)
def test_analyse_bank_data(filename, ans):
    filename = os.path.join(DATA_DIR, "bank", filename)
    assert analyse_bank_data(filename) == ans
