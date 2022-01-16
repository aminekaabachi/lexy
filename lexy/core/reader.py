from typing import Dict, List, Tuple
from lexy.core.glossary import Glossary
from lexy.core.term import Term
from abc import ABC, abstractmethod
import pandas as pd


class BaseReader(ABC):
    source_type = ""

    def __init__(self, name_column: str = "name", definition_column: str = "definition"):
        self.name_column = name_column
        self.definition_column = definition_column

    @abstractmethod
    def _prepare_df(self, **options) -> pd.DataFrame:
        pass

    def read(self, **options) -> Glossary:
        df = self._prepare_df(**options)
        self.columns = df.columns
        self.metadata_columns = list(set(self.columns).difference(
            set([self.name_column, self.definition_column])))
        return self._handle_pandas_df(df)

    def _check_requirements(self, columns: List[str]):
        if self.name_column not in columns:
            raise Exception(
                f"Name column '{self.name_column}' not present. Check that the column exists in {self.source_type} source.")
        elif self.definition_column not in columns:
            raise Exception(
                f"Definition column '{self.definition_column}' not present. Check that the column exists in  {self.source_type} source.")

    def _merge_metadata_as_dict(self, df: pd.DataFrame) -> pd.DataFrame:
        merged_df = pd.DataFrame()
        merged_df[self.name_column] = df[self.name_column]
        merged_df[self.definition_column] = df[self.definition_column]
        if len(self.metadata_columns) > 0:
            merged_df["metadata"] = df[self.metadata_columns].to_dict(
                orient='records')
        else:
            merged_df["metadata"] = [{}
                                     for _ in range(len(merged_df))]
        return merged_df

    def _prepare_terms_and_relationships(self, merged_df: pd.DataFrame) -> Tuple[Dict, Dict]:
        merged_dict = merged_df.to_dict(orient='records')
        terms = {}
        relations = {}
        for item in merged_dict:
            terms = dict(terms, **{str(item.get(self.name_column)): Term(
                item.get(self.name_column), item.get(self.definition_column), **item.get("metadata"))})
            relations = dict(
                relations, **{str(item.get(self.name_column)): []})
        return terms, relations

    def _handle_pandas_df(self, df: pd.DataFrame) -> Glossary:
        columns = df.columns

        self._check_requirements(columns)
        merged_df = self._merge_metadata_as_dict(df)
        terms, relations = self._prepare_terms_and_relationships(merged_df)

        return Glossary(terms, relations)
