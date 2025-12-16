def aggregate(df, metric, column):
    if metric == "count":
        return df[column].value_counts()
    if metric == "average":
        return df.groupby("Semester")["Marks"].mean()
