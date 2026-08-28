# Installation

meteogis requires Python 3.9+.

```bash
pip install meteogis
```

This pulls in `rasterio`, `geopandas`, `pyogrio`, `shapely`, `pyproj`,
`numpy`, `pandas`, and `scipy` automatically — all of which ship
self-contained wheels, so no separate system GDAL install is needed on
Windows, Linux, or macOS.

## Development install

To work on meteogis itself (e.g. to build these docs or run the test
suite), clone the repo and install it in editable mode:

```bash
git clone https://github.com/Thatpythonguy96/meteogis
cd meteogis
pip install -e .
```
