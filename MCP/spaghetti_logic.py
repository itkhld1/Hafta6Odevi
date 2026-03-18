def process_data(data):
    res = []
    for d in data:
        val = d * 1.15
        s = f"Total: {val:.2f}"
        print(s)
        res.append(val)
    with open("log.txt", "a") as f:
        f.write(str(res) + "\n")
    return res
