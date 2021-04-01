"""Stream class for tap-parquet."""

import requests

from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable


from singer_sdk.streams import Stream


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

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ParquetStream(Stream):
    """Stream class for Parquet streams."""

    def get_records(self, partition: Optional[dict] = None) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects."""
        # TODO: Write logic to extract data from the upstream source.
        # rows = mysource.getall()
        # for row in rows:
        #     yield row.to_dict()
        raise NotImplementedError("The method is not yet implemented (TODO)")


# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.
class UsersStream(ParquetStream):
    name = "users"

    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = PropertiesList(
        Property("name", StringType),
        Property("id", StringType),
        Property("age", IntegerType),
        Property("email", StringType),
        Property("street", StringType),
        Property("city", StringType),
        Property("state", StringType),
        Property("zip", StringType),
    ).to_dict()


class GroupsStream(ParquetStream):
    name = "groups"

    primary_keys = ["id"]
    replication_key = "modified"
    schema = PropertiesList(
        Property("name", StringType),
        Property("id", StringType),
        Property("modified", DateTimeType),
    ).to_dict()
