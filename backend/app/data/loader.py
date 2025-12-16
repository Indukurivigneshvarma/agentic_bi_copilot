import pandas as pd
from fastapi import UploadFile
from io import BytesIO

REQUIRED_COLUMNS = {
    "Student_ID",
    "Student_Name",
    "Subject",
    "Marks",
    "Grade",
    "Semester"
}

def load_excel(file: UploadFile):
    content = file.file.read()
    excel_bytes = BytesIO(content)
    df = pd.read_excel(excel_bytes)

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return df
