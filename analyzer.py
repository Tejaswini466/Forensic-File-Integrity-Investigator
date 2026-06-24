import numpy as np

def detect_size_anomalies(file_data):

    if not file_data:
        print("No files found.")
        return file_data

    sizes = np.array([f["size"] for f in file_data if f["size"] is not None])

    if len(sizes) == 0:
        return file_data

    mean = np.mean(sizes)
    std = np.std(sizes)

    for f in file_data:
        if f["size"] > mean + 3 * std:
            f["size_anomaly"] = True
        else:
            f["size_anomaly"] = False

    return file_data