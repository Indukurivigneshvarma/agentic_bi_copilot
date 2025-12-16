from app.data.data_store import DATA_STORE
from app.agent.intent_extractor import extract_intent
from app.analysis.filters import filter_student
from app.analysis.analysis_plan import decide_analysis_plan

from app.visualization.pie import plot_pie
from app.visualization.bar import plot_bar
from app.visualization.line import plot_line
from app.visualization.histogram import plot_histogram
from app.utils.chart_utils import encode_chart


def run_agent(query: str):
    df = DATA_STORE["df"]
    intent = extract_intent(query)

    # -------- Filter by student if needed --------
    df = filter_student(
        df,
        intent.get("student_name"),
        intent.get("student_id")
    )

    if df is None or df.empty:
        return {
            "chart_type": intent["chart_type"],
            "image_base64": "",
            "summary": "No data found for the given query."
        }

    # -------- Decide analysis plan --------
    plan = decide_analysis_plan(query, intent)

    x = plan["x_axis"]
    agg = plan["aggregation"]

    # -------- PIE --------
    if intent["chart_type"] == "pie":
        data = df[x].value_counts()
        plot_pie(data)

    # -------- BAR --------
    elif intent["chart_type"] == "bar":
        if agg == "mean":
            data = df.groupby(x)["Marks"].mean()
            plot_bar(data, y_label="Average Marks")
        else:
            data = df[x].value_counts()
            plot_bar(data, y_label="Count")

    # -------- LINE --------
    elif intent["chart_type"] == "line":
        data = df.groupby(x)["Marks"].mean()
        plot_line(data, x_label=x)

    # -------- HISTOGRAM --------
    elif intent["chart_type"] == "histogram":
        plot_histogram(df["Marks"])

    image_base64 = encode_chart()

    return {
        "chart_type": intent["chart_type"],
        "image_base64": image_base64,
        "summary": "Chart generated successfully"
    }
