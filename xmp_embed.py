import subprocess

def run_exiftool(image_path):
    subprocess.run(["exiftool.exe", image_path], check=True)

def write_xmp(image_path, tilt, roll, azimuth):
    cmd = [
        "exiftool",
        "-config", "argus.config",
        f"-XMP-argus:TiltRad={tilt}",
        f"-XMP-argus:RollRad={roll}",
        f"-XMP-argus:AzimuthRad={azimuth}",
        image_path,
    ]

    subprocess.run(cmd, check=True)