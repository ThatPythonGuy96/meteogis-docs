.. MeteoGIS documentation master file, created by
   sphinx-quickstart on Sat Aug 22 19:17:54 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MeteoGIS documentation
======================

**meteogis** is a lightweight Python toolkit for geospatial processing and
climate index analysis. It provides utilities for raster/vector conversion,
geospatial file I/O, and hydrometeorological indices like SPI and SPEI —
built on `rasterio`_ and `geopandas <https://geopandas.org/>`_, with no system GDAL install required.

.. _rasterio: https://rasterio.readthedocs.io/

Features
========


- **Climate index analysis** — Standardized Precipitation Index (SPI),
  Standardized Precipitation-Evapotranspiration Index (SPEI), kriging and
  IDW interpolation, zonal statistics
- **Raster utilities** — clipping, contour generation, hillshade, raster
  algebra, polygonize, raster-to-point extraction
- **Vector utilities** — buffer, clip, dissolve, merge, reproject,
  simplify, union
- **I/O helpers** — read/write GeoTIFF, GeoJSON, GeoPackage, Shapefile,
  and CSV through a single `read_file()` / `to_file()` API that
  auto-dispatches on file extension


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   quickstart
   API Reference <api/modules>
