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
        (
            "student_performance_test.csv",
            (
                986, 
                {'Female': 506, 'Male': 480}, 
                {'Track C': 75.26, 'Track A': 75.38, 'Track B': 74.93}, 
                "Associate's Degree", 
                54.81, 
                [(90, 'Female'), (90, 'Female'), (90, 'Female'), (90, 'Male'), (90, 'Male'), (90, 'Male'), (90, 'Female'), (90, 'Male'), (90, 'Female'), (90, 'Female'), (90, 'Male'), (90, 'Female'), (90, 'Female'), (90, 'Male'), (90, 'Female'), (90, 'Female'), (90, 'Female'), (90, 'Male')],
            ),
        ),
        (
            "student_performance_test_1.csv",
            (
                2000, 
                {'Male': 991, 'Female': 1009}, 
                {'Track A': 51.26, 'Track C': 50.41, 'Track B': 50.6}, 
                'High School', 
                51.13, 
                [(100, 'Female'), (100, 'Male'), (100, 'Female'), (100, 'Female'), (100, 'Male'), (100, 'Male'), (100, 'Male'), (100, 'Female'), (100, 'Male'), (100, 'Male'), (100, 'Female'), (100, 'Male'), (100, 'Female'), (100, 'Male'), (100, 'Female'), (100, 'Male'), (100, 'Male'), (100, 'Female'), (100, 'Female'), (100, 'Male'), (100, 'Male'), (100, 'Female')],
            ),
        ),
        (
           "student_performance_test_2.csv",
           (
               321, 
               {'Male': 153, 'Female': 168}, 
               {'Track B': 73.96, 'Track A': 73.78}, 
               "Associate's Degree", 
               55.73, 
               [(90, 'Male'), (90, 'Female'), (90, 'Female'), (90, 'Male')],
            ),
        ),
        (
            "student_performance_test_3.csv",
            (
                5, 
                {'Male': 2, 'Female': 3}, 
                {'Track B': 74.5, 'Track A': 61}, 
                "Bachelor's Degree", 
                56.6, 
                [(89, 'Female')],
            ),
        ),
        (
            "student_performance_test_4.csv",
            (
                5, 
                {'Male': 2, 'Female': 3}, 
                {'Track C': 64.5, 'Track A': 74}, 
                "Associate's Degree", 
                21.4, 
                [(89, 'Male')],
            ),
        )
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
        ("bank_transactions_test.csv", (840.18, 13, 908.32)),
        ("bank_transactions_test_1.csv", (2399.03, 9, 3380.65)),
        ("bank_transactions_test_2.csv", (1996.58, 0, 9714.91)),
        ("bank_transactions_test_3.csv", (0, 0, 44506.44)),
    ],
)
@pytest.mark.timeout(0.1)
def test_analyse_bank_data(filename, ans):
    filename = os.path.join(DATA_DIR, "bank", filename)
    assert analyse_bank_data(filename) == ans
