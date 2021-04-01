"""Tests init and discovery features for tap-parquet."""

import datetime
from pathlib import Path

from singer_sdk.testing import get_standard_tap_tests

from tap_parquet.tap import TapParquet

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "filepath": str(Path(__file__).parent / "resources/testfile.parquet"),
}


# Get built-in 'generic' tap tester from SDK:
def test_parquet_tap_standard_tests():
    """Run standard tap tests against Parquet) tap."""
    tests = get_standard_tap_tests(TapParquet, tap_config=SAMPLE_CONFIG)
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
