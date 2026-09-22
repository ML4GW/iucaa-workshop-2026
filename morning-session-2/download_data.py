from gwpy.timeseries import TimeSeries, TimeSeriesDict
from pathlib import Path
import requests

data_dir = Path("./data")
background_dir = data_dir / "background_data"
background_dir.mkdir(parents=True, exist_ok=True)

ifos = ["H1", "L1"]
sample_rate = 2048

segments = [
    (1369890018, 1369908018),
    (1370145618, 1370152818),
]

for (start, end) in segments:
    # Download the data from GWOSC. This will take a few minutes.
    duration = end - start
    fname = background_dir / f"background-{start}-{duration}.hdf5"
    if fname.exists():
        continue

    ts_dict = TimeSeriesDict()
    for ifo in ifos:
        print(f"Fetching open data for {ifo}: {start} .. {end}")
        ts_dict[ifo] = TimeSeries.fetch_open_data(ifo, start, end, cache=True)
    ts_dict = ts_dict.resample(sample_rate)
    ts_dict.write(fname, format="hdf5")

# also download frame files around GW250104
urls = [
    "https://gwosc.org/archive/data/O4b3Disc_4KHZ_R1/1420820480/H-H1_GWOSC_O4b3Disc_4KHZ_R1-1420877824-4096.gwf",
    "https://gwosc.org/archive/data/O4b3Disc_4KHZ_R1/1420820480/L-L1_GWOSC_O4b3Disc_4KHZ_R1-1420877824-4096.gwf",
]

for url in urls:
    fname = url.split("/")[-1]
    print(f"Downloading {fname} ...")
    fname = data_dir / fname
    if fname.exists():
        continue
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(fname, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Saved to {fname}")