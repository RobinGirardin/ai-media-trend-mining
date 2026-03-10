"""Module contain helper functions."""

import itertools
import json
import os
import pathlib
import pickle
import pprint
import re
from typing import List, Optional, Tuple

import langextract as lx
import numpy as np

DIR = pathlib.Path(os.getcwd())
PROCESSED_DATA_DIR = pathlib.Path(DIR, "data", "processed")

def parse_string_into_list(
        string: str,
        parsing_pattern: re.Pattern = re.compile(r"(?<=\')[^,].*?(?=\', '|'])", flags=re.MULTILINE)
) -> List[str]:
    """Parse `tags` and `content` features into list of string."""
    parsed_string = parsing_pattern.findall(string)

    return parsed_string


def get_entity_match(
        entity_text: str,
        entity_has_attributes: list[dict]
) -> Optional[int]:
    """Retrieve the entity id for a given entity text."""
    for record in entity_has_attributes:
        ent_type = entity_text.strip().lower()
        text = record["text"].strip().lower()

        if ent_type == text:
            id_match = record["entity_id"]

    return id_match


def isin(table: List[dict], **kv_pair):
    """Check for a table record matching the specified key:value pairs."""
    keys = np.array(list(kv_pair.keys()))
    values = np.array(list(kv_pair.values()))

    for record in table:
        record_key_values = np.array(
            [record.get(key) for key in keys if record.get(key) is not None]
        )
        if np.equal(record_key_values, values).all():  # True is full match
            return True

    return False

def parse_attributes(attr: dict | None) -> dict:
    if isinstance(attr, dict):
        return attr
    elif attr is None:
        return {}
    else:
        raise AttributeError(
            f"'attr' must ne either a 'dict' or 'NoneType', not '{type(attr)}'"
        )

def langextract_to_json(
    media_id: int,
    annotated_doc: lx.data.AnnotatedDocument
) -> List[dict]:
    """Parse the extraction result in a manageable format.

    Returns:
        list_flattened_extractions (list[dict]):
            a list of extracted informations
    """
    extraction: lx.data.Extraction
    list_flattened_extractions: List[dict] = []
    for extraction in annotated_doc.extractions:

        start_pos = (
            extraction.char_interval.start_pos if extraction.char_interval is not None else None
        )
        end_pos = (
            extraction.char_interval.end_pos if extraction.char_interval is not None else None
        )
        flattened: dict = {
            "media_id": media_id,
            "media_text": annotated_doc.text,
            extraction.extraction_class: {
                "entity_text": extraction.extraction_text,
                "start_pos": start_pos,
                "end_pos": end_pos,
                **parse_attributes(extraction.attributes)
            }
        }
        list_flattened_extractions.append(flattened)

    return list_flattened_extractions


if __name__ == "__main__":
    with open("notebook/langextract_extraction_results.pkl", "rb") as file:
        documents = pickle.load(file)

    json_annotations: List[dict] = []
    for doc in documents:
        flattened_extraction = langextract_to_json(
            doc["media_id"], doc["extraction"]
        )
        json_annotations.extend(flattened_extraction)

    # For futur usage and analysis.
    with open(
        "data/processed/langchain_extractions_json.pkl", "wb"
    ) as file:
        pickle.dump(json_annotations, file)

    # For visual purpose only
    with open(
        "data/processed/langchain_extractions.json", "w"
    ) as fileson:
        json.dump(json_annotations, fileson)
