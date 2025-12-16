def decide_analysis_plan(query: str, intent: dict):
    q = query.lower()

    # -------- X AXIS --------
    if "subject" in q:
        x_axis = "Subject"
    elif "semester" in q:
        x_axis = "Semester"
    else:
        x_axis = "Grade"

    # -------- Y AXIS / AGGREGATION --------
    if "average" in q or "highest" in q or "compare" in q:
        y_axis = "Marks"
        aggregation = "mean"
    else:
        y_axis = "count"
        aggregation = "count"

    return {
        "x_axis": x_axis,
        "y_axis": y_axis,
        "aggregation": aggregation
    }
