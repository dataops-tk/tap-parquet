"""Parquet tap class."""

from pathlib import Path
from typing import List
import click
from singer_sdk import Tap, Stream
from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

# TODO: Import your custom stream types here:
from tap_parquet.streams import (
    ParquetStream,
    UsersStream,
    GroupsStream,
)


# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    UsersStream,
    GroupsStream,
]


class TapParquet(Tap):
    """Parquet tap class."""

    name = "tap-parquet"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = PropertiesList(
        Property("start_date", DateTimeType),
        Property("filepath", StringType),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


# CLI Execution:

cli = TapParquet.cli
