from pathlib import Path

def parse_filename(filename: str) -> dict:
    name = Path(filename).name
    parts = name.split(".")

    return {
        "timestamp": int(parts[0]),
        "station": parts[6],
        "camera_number": int(parts[7][1:]),
    }

image_details = parse_filename("1485390607.Thu.Jan.26_11_30_07.AEST.2017.goldcst.c5.snap.jpg")

