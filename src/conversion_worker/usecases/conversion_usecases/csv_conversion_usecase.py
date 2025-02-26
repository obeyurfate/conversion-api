import asyncio
import csv
import tempfile

import pandas
from . import errors


class CSVConversionUsecase:
    async def execute(self, file_content: bytes) -> str:
        return await asyncio.to_thread(self._convert_file_content, file_content)

    def _convert_file_content(self, file_content: bytes) -> str:
        file_text = file_content.decode("utf-8")
        sniffer = csv.Sniffer()

        try:
            detected_delimiter = sniffer.sniff(file_text).delimiter
        except csv.Error as exc:
            raise errors.InvalidFileFormatError() from exc

        if detected_delimiter != ",":
            msg_exc = "Unknown delimiter for basic CSV."
            raise errors.InvalidFileFormatError(msg_exc)

        with tempfile.NamedTemporaryFile(mode="r+", delete=False) as f:
            f.write(file_text)
            f.seek(0)
            df = pandas.read_csv(f.name, delimiter=",")
        return df.to_json(orient='records')
