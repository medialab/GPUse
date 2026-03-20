import os
import sys
import csv
import json


HEADERS = [
    "datetime",
    "gpu_name",
    "usage_percent",
    "memory",
    "memory_percent",
    "energy",
    "temperature",
    "fan_speed",
    "users",
    "processes"
]

def parse(filename):
    indices = {}
    listfile = os.path.join("data", "list.json")
    if os.path.exists(listfile):
        with open(listfile, "r") as f:
            indices = {gpu: idx for (idx, gpu) in enumerate(json.load(f)["gpus"])}

    with open(filename) as f:
        data = json.load(f)

    listgpus = []
    for gpu in data["gpus"]:
        listgpus.append(gpu["uuid"])
        row = {
            "datetime": data["query_time"],
            "gpu_name": "%s #%s" % (gpu["name"], indices[gpu["uuid"]] or gpu["index"]),
            "usage_percent": gpu["utilization.gpu"],
            "memory": gpu["memory.used"],
            "memory_percent": round(100 * gpu["memory.used"] / gpu["memory.total"], 3),
            "energy": gpu["power.draw"],
            "temperature": gpu["temperature.gpu"],
            "fan_speed": gpu["fan.speed"],
            "users": "§".join([p["username"] for p in gpu["processes"] or []]),
            "processes": "§".join([" ".join(p["full_command"]) for p in gpu["processes"] or []])
        }

        csvfilename = os.path.join("data", "%s_%s.csv" % (gpu["uuid"], row["datetime"][:7]))

        if not os.path.exists(csvfilename):
            with open(csvfilename, "w") as f:
                writer = csv.writer(f)
                writer.writerow(HEADERS)

        with open(csvfilename, "a") as f:
            writer = csv.writer(f)
            writer.writerow([row[h] for h in HEADERS])

    listfile = os.path.join("data", "list.json")
    if not os.path.exists(listfile):
        with open(listfile, "w") as f:
            json.dump({
                "gpus": listgpus,
                "start": data["query_time"]
            }, f)


if __name__ == "__main__":
    FILE = sys.argv[1]
    parse(FILE)
