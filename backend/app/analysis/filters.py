def filter_student(df, student_name=None, student_id=None):
    if student_name:
        return df[df["Student_Name"].str.contains(
            student_name, case=False, na=False
        )]

    if student_id:
        return df[df["Student_ID"] == student_id]

    return df
