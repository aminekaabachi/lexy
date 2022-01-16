
import pandas as pd
from lexy.core.glossary import Glossary
from lexy.core.term import Term
from typing import List
from cattr import structure

def from_csv(filepath: str, delimiter:str = None, name_column: str = "name", definition_column : str = "definition") -> Glossary:
    df = pd.read_csv(filepath, delimiter=delimiter)
    return _handle_pandas_df(df, name_column, definition_column)

def _handle_pandas_df(df: pd.DataFrame, name_column: str = "name", definition_column : str = "definition"):
    columns = df.columns

    #Check if name_column and definition_column are present in df
    if name_column not in columns:
        raise Exception(f"Name column '{name_column}' not present.")
    elif definition_column not in columns:
        raise Exception(f"Denifintion column '{definition_column}' not present.")

    #Transform df into target format
    metadata = list(set(columns).difference(set([name_column, definition_column])))

    transformed_df = pd.DataFrame()
    transformed_df[name_column] = df[name_column]
    transformed_df[definition_column] = df[definition_column]
    
    if len(metadata) > 0:
        transformed_df["metadata"] = df[metadata].to_dict(orient='records')
    else:
        transformed_df["metadata"] = [{} for _ in range(len(transformed_df))]
    
    D = transformed_df.to_dict(orient='records')
    terms={}
    relations={}
    for e in D:
        terms = dict(terms, **{str(e.get(name_column)): Term(e.get(name_column), e.get(definition_column), **e.get("metadata"))})
        relations = dict(relations, **{str(e.get(name_column)): []})
    return Glossary(terms, relations)