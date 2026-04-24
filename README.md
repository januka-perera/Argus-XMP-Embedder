# Argus-XMP-Embedder

Queries an Argus database for data related to an image collected from an Argus station and embeds it as custom XMP metadata into JPEG images using ExifTool.

## Setup

### 1. Create a Python virtual environment

```bash
python -m venv venv
```

Activate it:

- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

The following packages will be installed:

| Package | Purpose |
|---|---|
| `PyMySQL` | Connect to the Argus MySQL database |
| `python-dotenv` | Load database credentials from a `.env` file |

### 3. Configure environment variables

Create a `.env` file in the project root:

```
DB_HOST=your-database-host
DB_USER=your-database-user
PASSWORD=your-database-password
```

### 4. Install ExifTool and add it to PATH

ExifTool is required to write XMP metadata to image files.

1. Download ExifTool from [https://exiftool.org](https://exiftool.org)
2. **Windows**: Download the Windows executable (`exiftool(-k).exe`), rename it to `exiftool.exe`, and place it in a directory on your PATH (e.g. `C:\Windows\System32` or a custom `C:\tools` folder added to your PATH via System Properties > Environment Variables)
3. **macOS**: Install via Homebrew: `brew install exiftool`
4. **Linux**: Install via your package manager, e.g. `sudo apt install libimage-exiftool-perl`

Verify the installation:

```bash
exiftool -ver
```

## Configuration — `argus.config`

`argus.config` is an ExifTool configuration file that defines a custom XMP namespace for Argus-specific metadata tags. It is passed to every `exiftool` call via the `-config argus.config` flag.

### Namespace URI

The namespace URI uniquely identifies your XMP schema and must be a URI you control. Update the placeholder before use:

```perl
NAMESPACE => { 'argus' => 'http://argus.example.com/ns/1.0/' },
```

Replace `http://argus.example.com/ns/1.0/` with a URI that belongs to your organisation, for example:

```perl
NAMESPACE => { 'argus' => 'http://yourorganisation.com/argus/xmp/1.0/' },
```

The URI does not need to resolve to a real web page — it just needs to be globally unique and consistent across all files you write.

### Namespace prefix

The prefix `argus` is the short label used in XMP tag names (e.g. `XMP-argus:TiltRad`). It is defined in two places and both must match:

```perl
%Image::ExifTool::UserDefined = (
    'Image::ExifTool::XMP::Main' => {
        argus => { ... },          # <-- prefix here
    },
);

%Image::ExifTool::UserDefined::argus = (  # <-- and here
    GROUPS    => { 0 => 'XMP', 1 => 'XMP-argus', 2 => 'Image' },
    NAMESPACE => { 'argus' => 'http://argus.example.com/ns/1.0/' },
    ...
);
```

If you rename the prefix, update all three occurrences and the tag references in `xmp_embed.py`.

### Defined tags

| Tag | Type | Description |
|---|---|---|
| `TiltRad` | real | Camera tilt angle in radians |
| `RollRad` | real | Camera roll angle in radians |
| `AzimuthRad` | real | Camera azimuth angle in radians |
| `StationID` | string | Argus station identifier |
| `CameraNumber` | string | Camera number at the station |
| `Timestamp` | string | Image capture timestamp |

## Usage

```bash
python run.py
```


