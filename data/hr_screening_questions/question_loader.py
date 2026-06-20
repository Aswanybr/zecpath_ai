import json
import os


def load_questions(role):
    """
    Load role specific HR screening questions
    """

    file_path = (
        f"data/hr_screening_questions/"
        f"{role}_questions.json"
    )

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Question file not found: {file_path}"
        )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)