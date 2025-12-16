from app.data.data_store import DATA_STORE
from app.agent.intent_extractor import extract_intent
from app.analysis.filters import filter_student
from app.visualization.pie import plot_pie
from app.visualization.bar import plot_bar
from app.visualization.line import plot_line
from app.visualization.histogram import plot_histogram
from app.utils.chart_utils import encode_chart

def run_agent(query: str):
    df = DATA_STORE["df"]
    intent = extract_intent(query)

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

    if intent["chart_type"] == "pie":
        plot_pie(df["Grade"].value_counts())

    elif intent["chart_type"] == "bar":
        plot_bar(df["Grade"].value_counts())

    elif intent["chart_type"] == "line":
        plot_line(df.groupby("Semester")["Marks"].mean())

    elif intent["chart_type"] == "histogram":
        plot_histogram(df["Marks"])

    image_base64 = encode_chart()

    return {
        "chart_type": intent["chart_type"],
        "image_base64": image_base64,
        "summary": "Chart generated successfully"
    }
