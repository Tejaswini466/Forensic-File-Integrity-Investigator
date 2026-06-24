import pickle

def save_baseline(data, filename="baseline.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def load_baseline(filename="baseline.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except:
        return None
    
def compare_with_baseline(current, baseline):
    baseline_map = {f["path"]: f for f in baseline}

    results = []

    for f in current:
        old = baseline_map.get(f["path"])

        if old:
            if f["hash"] != old["hash"]:
                f["status"] = "MODIFIED"
            else:
                f["status"] = "UNCHANGED"
        else:
            f["status"] = "NEW"

        results.append(f)

    return results