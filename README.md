# tap-parquet

This Singer tap was created using the [Singer SDK](https://gitlab.com/meltano/singer-sdk).

## About Parquet

Parquet is a portable, type-aware, columnar, compressed, splittable, and cloud-friendly format.

For more information why Parquet is increasingly used in big data applications, see
[this comparison](https://www.linkedin.com/pulse/spark-file-format-showdown-csv-vs-json-parquet-garren-staubli/).

## Getting Started

## Testing Guide

Create tests within the `tap_parquet/tests` subfolder and
  then run:

```bash
poetry install
poetry run pytest
```

## Singer SDK Dev Guide

See the [dev guide](../../docs/dev_guide.md) for more instructions on how to use the Singer SDK to 
develop your own taps and targets.

## Config Guide

### Accepted Config Options

Currently only a single config option is expected:

- `filepath` - absolute path to a parquet source file.

### Source Authentication and Authorization

N/A. Cloud support is [not yet](https://github.com/dataops-tk/tap-parquet/issues/3) available.
