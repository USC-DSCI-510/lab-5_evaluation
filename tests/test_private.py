import os
import pytest

from lab5 import analyse_student_data, analyse_bank_data

CURRENT_WORKING_DIR = os.getcwd()
DATA_DIR = os.path.join(CURRENT_WORKING_DIR, "data")


@pytest.mark.parametrize(
    "filename,ans",
    [
        (
            "student_performance_test.csv",
            (
                986,
                {"Female": 506, "Male": 480},
                {"Track C": 75.26, "Track A": 75.38, "Track B": 74.93},
                "Associate's Degree",
                54.81,
                [
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Male"),
                    (90, "Male"),
                    (90, "Male"),
                    (90, "Female"),
                    (90, "Male"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Male"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Male"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Male"),
                ],
            ),
        ),
        (
            "student_performance_test_1.csv",
            (
                2000,
                {"Male": 991, "Female": 1009},
                {"Track A": 51.26, "Track C": 50.41, "Track B": 50.6},
                "High School",
                51.13,
                [
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Female"),
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Male"),
                    (100, "Male"),
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Male"),
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Male"),
                    (100, "Female"),
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Male"),
                    (100, "Female"),
                ],
            ),
        ),
        (
            "student_performance_test_2.csv",
            (
                321,
                {"Male": 153, "Female": 168},
                {"Track B": 73.96, "Track A": 73.78},
                "Associate's Degree",
                55.73,
                [(90, "Male"), (90, "Female"), (90, "Female"), (90, "Male")],
            ),
        ),
        (
            "student_performance_test_3.csv",
            (
                5,
                {"Male": 2, "Female": 3},
                {"Track B": 74.5, "Track A": 61},
                "Bachelor's Degree",
                56.6,
                [(89, "Female")],
            ),
        ),
        (
            "student_performance_test_4.csv",
            (
                5,
                {"Male": 2, "Female": 3},
                {"Track C": 64.5, "Track A": 74},
                "Associate's Degree",
                21.4,
                [(89, "Male")],
            ),
        ),
        (
            "student_performance_test_12.csv",
            (
                350,
                {"Male": 350},
                {"Track C": 65.57, "Track B": 68.61},
                "Bachelor's Degree",
                58.32,
                [(100, "Male"), (100, "Male"), (100, "Male"), (100, "Male")],
            ),
        ),
        (
            "student_performance_test_10.csv",
            (
                500,
                {"Female": 244, "Male": 256},
                {"Track A": 75.29, "Track B": 74.13, "Track C": 70.74},
                "Associate's Degree",
                74.71,
                [
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Male"),
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Female"),
                    (100, "Female"),
                    (100, "Female"),
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Female"),
                    (100, "Female"),
                    (100, "Male"),
                    (100, "Female"),
                ],
            ),
        ),
        (
            "student_performance_test_11.csv",
            (
                1230,
                {"Female": 1230},
                {"Track A": 75.34, "Track C": 75.52, "Track B": 74.76},
                "High School",
                76.03,
                [
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                    (90, "Female"),
                ],
            ),
        ),
    ],
)
@pytest.mark.timeout(0.25)
def test_analyse_student_data(filename, ans):
    filename = os.path.join(DATA_DIR, "student", filename)
    assert analyse_student_data(filename) == ans


@pytest.mark.parametrize(
    "filename,ans",
    [
        ("bank_transactions_test.csv", (840.18, 13, 908.32)),
        ("bank_transactions_test_1.csv", (2399.03, 9, 3380.65)),
        ("bank_transactions_test_2.csv", (1996.58, 0, 9714.91)),
        ("bank_transactions_test_3.csv", (0, 0, 44506.44)),
        ("bank_transactions_test_11.csv", (4964.56, 0, 1352110.02)),
        ("bank_transactions_test_12.csv", (4994.72, 108, 927911.3)),
        ("bank_transactions_test_21.csv", (9998.13, 1216, 16875732.78)),
    ],
)
@pytest.mark.timeout(0.25)
def test_analyse_bank_data(filename, ans):
    filename = os.path.join(DATA_DIR, "bank", filename)
    assert analyse_bank_data(filename) == ans


@pytest.mark.parametrize(
    "filename,ans",
    [
        ("student_performance_test_1_dne.csv", "Invalid Input"),
        ("student_performance_test_2_dne.csv", "Invalid Input"),
        ("student_performance_test_3_dne.txt", "Invalid Input"),
    ],
)
@pytest.mark.timeout(0.25)
def test_analyse_bank_data_does_not_exist(filename, ans):
    filename = os.path.join(DATA_DIR, "bank", filename)
    with pytest.raises(Exception) as e_info:
        analyse_bank_data(filename)
    assert str(e_info.value).lower() == ans.lower()


@pytest.mark.parametrize(
    "filename,ans",
    [
        ("bank_transactions_sample_dne.csv", "Invalid Input"),
        ("bank_transactions_test_dne_234.csv", "Invalid Input"),
        ("bank_transactions_dne_767.txt", "Invalid Input"),
    ],
)
@pytest.mark.timeout(0.25)
def test_analyse_student_data_does_not_exist(filename, ans):
    filename = os.path.join(DATA_DIR, "student", filename)
    with pytest.raises(Exception) as e_info:
        analyse_bank_data(filename)
    assert str(e_info.value).lower() == ans.lower()
