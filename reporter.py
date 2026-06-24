import pandas as pd
import time

def generate_report(data):

    if not data:
        print("No data available for report.")
        return pd.DataFrame()

    df = pd.DataFrame(data)

    df["mtime_readable"] = df["mtime"].apply(
        lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x))
    )

    now = time.time()

    df["age_days"] = (now - df["mtime"]) / (60 * 60 * 24)

    df["age_category"] = pd.cut(
        df["age_days"],
        bins=[-1, 1, 7, 30, 3650],
        labels=["Today", "This Week", "This Month", "Old"]
    )

    df.to_excel("Forensic_Report.xlsx", index=False)

    return df