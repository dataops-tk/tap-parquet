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
)


class TapParquet(Tap):
    """Parquet tap class."""

    name = "tap-parquet"

    config_jsonschema = PropertiesList(
        Property("start_date", DateTimeType),
        Property("filepath", StringType, required=True),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        result: List[Stream] = []
        for filename in [self.config["filepath"]]:
            new_stream = ParquetStream(
                tap=self,
                name=filename,
                schema=self.detect_json_schema(filename),
            )
            new_stream.primary_keys = self.detect_primary_keys(filename)
            result.append(new_stream)
        return result

    def detect_json_schema(self, parquet_filepath: str) -> dict:
        return PropertiesList(
            Property("f0", StringType, required=True),
            Property("f1", StringType),
            Property("f2", StringType),
        ).to_dict()

    def detect_primary_keys(self, parquet_filepath: str) -> List[str]:
        return ["f0"]


# CLI Execution:

cli = TapParquet.cli
