# Quickstart

## Reading and writing raster/vector files

`meteogis` exposes a single `read_file()` / `to_file()` pair that
auto-dispatches on file extension — the same call works for GeoTIFF,
GeoJSON, GeoPackage, Shapefile, and CSV.

```python
import numpy as np
from meteogis.read_file import read_file
from meteogis.to_file import to_file

# Write a raster
array = np.ones((100, 100), dtype="float32")
to_file(
    array, "rainfall.tif",
    xsize=100, ysize=100,
    crs="EPSG:4326",
    geotransform=(3.0, 0.01, 0, 9.0, 0, -0.01),
)

# Read it back
dataset = read_file("rainfall.tif")
print(dataset.array.shape, dataset.crs)
```

```python
from shapely.geometry import Point
from meteogis.to_file import to_file
from meteogis.read_file import read_file

# Write a vector layer
stations = [
    (Point(3.9, 7.4), {"name": "Ibadan", "rainfall_mm": 120}),
    (Point(7.5, 9.1), {"name": "Abuja", "rainfall_mm": 95}),
]
to_file(stations, "stations.geojson", crs="EPSG:4326")

# Read it back
features = read_file("stations.geojson")
```

## Climate index analysis

```python
import pandas as pd
from meteogis.analysis.spi import spi

rainfall = pd.Series([12, 45, 0, 88, 34, 5, 60, 22, 15, 40, 5, 70])
spi_values = spi(rainfall, thresh=3)
```

See the {doc}`API reference <api/modules>` for the full list of
raster, vector, and analysis functions.
