#!/usr/bin/env python
import argparse
import json
import os

import jsonschema
import yaml


class Validator(object):
    def validate(self, filename, reader):
        content = reader.read()
        if "schema" not in content:
            print("WARN: schema not set in the file")

        schema = self.get_schema(content.get("schema", ".."))
        try:
            jsonschema.validate(instance=content, schema=schema)
            return True
        except Exception as e:
            print(
                "Failed validating %r in %s%s: %s"
                % (
                    e.validator,
                    e._word_for_schema_in_error_message,
                    jsonschema._utils.format_as_index(
                        list(e.relative_schema_path)[:-1]
                    ),
                    e.message,
                )
            )
            return False

    def get_schema(self, url):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        schema_path = os.path.join(script_dir, "..", "..", "schema", "schema.json")

        with open(schema_path) as fd:
            return json.load(fd)


class DataReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        raise NotImplementedError("Please, implement this method")


class JSONReader(DataReader):
    def read(self):
        with open(self.filename) as fd:
            return json.load(fd)


class YAMLReader(DataReader):
    def read(self):
        with open(self.filename) as fd:
            return yaml.safe_load(fd)


class UnknownFormatException(Exception):
    """Unknown format exception"""

    pass


def reader_builder(filename):
    if filename.lower().endswith("json"):
        return JSONReader(filename)
    if filename.lower().endswith(("yml", "yaml")):
        return YAMLReader(filename)
    raise UnknownFormatException("Unknown format")


def parse_args():
    parser = argparse.ArgumentParser(description="Validate a Manfred Awesomic CV")
    parser.add_argument(
        "filename", nargs="+", help="YAML or JSON files to be validated"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    validator = Validator()

    for filename in args.filename:
        print(f"Validating {filename}")
        reader = reader_builder(filename)
        r = validator.validate(filename, reader)
        if r:
            print("OK")


if __name__ == "__main__":
    main()
