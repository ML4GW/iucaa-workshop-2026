# ML4GW tutorial LVK Pune 2026

This is a one-hour tutorial on [ML4GW](https://ml4gw.github.io/ml4gw/) tools,
showcasing the different components and how they are useful in the context of
training neural network models for GW science.

Dependency requirements are specified in `requirements.txt`. You can use
[uv](https://docs.astral.sh/uv/getting-started/installation/) to install dependencies.
```bash
$ uv venv --python=3.12 && uv pip install -r requirements.txt
```
Start the `jupyter-notebook` using the `uv` entrypoint:
```bash
$ uv run jupyter-notebook
```

# Pre-download the data from GWOSC

Participants are encouraged to pre-download the data from GWOSC before
the session. This is to prevent slow download speeds over the network
with multiple participants. Do this via
```
uv run python download_data.py
```
This will download some open data from GWOSC to your local machine in
the following directory structure.
```
.
├── data
│   └── background_data
│       ├── background-1369890018-18000.hdf5
│       └── background-1370145618-7200.hdf5
├── H-H1_GWOSC_O4b_4KHZ_R1-1420877824-4096.gwf
├── L-L1_GWOSC_O4b_4KHZ_R1-1420877824-4096.gwf

```
The notebook will use use these files for the examples.
