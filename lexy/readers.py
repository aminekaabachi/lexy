
from typing import Union
import pandas as pd
from lexy.core.glossary import Glossary
from lexy.core.reader import BaseReader


class CSVReader(BaseReader):
    source_type: str = "CSV"

    def _prepare_df(self, **options) -> pd.DataFrame:
        super()._prepare_df(**options)
        return pd.read_csv(filepath_or_buffer=options.get("filepath"), delimiter=options.get("delimiter"))


class ExcelReader(BaseReader):
    source_type: str = "Excel"

    def _prepare_df(self, **options) -> pd.DataFrame:
        super()._prepare_df(**options)
        return pd.read_excel(filepath=options.get("filepath"), sheet_name=options.get("sheet_name"))


def from_csv(filepath: str, delimiter: str = None, name_column: str = "name", definition_column: str = "definition") -> Glossary:
    return CSVReader(name_column, definition_column).read(filepath=filepath, delimiter=delimiter)


def from_excel(filepath: str, sheet_name: Union[str, int] = 0, name_column: str = "name", definition_column: str = "definition") -> Glossary:
    return ExcelReader(name_column, definition_column).read(filepath=filepath, sheet_name=sheet_name)
