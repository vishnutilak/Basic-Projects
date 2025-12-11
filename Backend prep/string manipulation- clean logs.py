def sort_logs(logs):
    # Split each log: "user,action,timestamp"
    parsed = []
    for log in logs:
        user, action, ts = log.split(',')
        parsed.append((user, action, int(ts)))  # convert ts to int for sorting

    # Sort by timestamp
    parsed.sort(key=lambda x: x[2])

    return parsed
