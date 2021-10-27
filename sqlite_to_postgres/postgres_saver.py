import logging
import time
from typing import Iterator

from models import Data, T
from psycopg2.extensions import connection
from psycopg2.extras import execute_values

logger = logging.getLogger(__name__)


class PostgresSaver:
    def __init__(self, connection: connection, chunk_size: int) -> None:
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.chunk_size = chunk_size

    def _save_table(self, table_name: str, table_data: Iterator[T]) -> None:
        t = time.perf_counter()

        execute_values(
            self.cursor,
            f"""INSERT INTO {table_name} VALUES %s ON CONFLICT (id) DO NOTHING;""",
            (row.values for row in table_data),
            page_size=self.chunk_size,
        )

        elapsed = time.perf_counter() - t
        logger.info("%s table saved in %s", table_name, elapsed)

    def save_all_data(self, data: Data) -> None:
        for table_name, table_data in data.items():
            self._save_table(table_name, table_data)

    def __del__(self) -> None:
        self.cursor.close()
