#!/usr/bin/env python
import argparse
import json
import logging

import yaml
from faker import Faker

logger = logging.getLogger(__name__)


def init_logging(debug=0):
    levels = (logging.WARNING, logging.INFO, logging.DEBUG)
    level = levels[min(debug, len(levels) - 1)]
    formatter = logging.Formatter(
        "** %(asctime)s.%(msecs)03d %(levelname)s: [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger.setLevel(level)
    logger.addHandler(handler)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate random data for jsonschema")
    parser.add_argument("schema", help="Schema to be used")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument(
        "-v", "--verbosity", action="count", default=0, help="Output file"
    )

    return parser.parse_args()


class Generator:
    def __init__(self, schema):
        self.schema = schema
        self.fake = Faker()

    def generate(self):
        result = self.generate_dict("", self.schema)
        if "schema" not in result:
            result["schema"] = self.schema["$schema"]
        return result

    def generate_dict(self, name, schema):
        result = {}
        for k, v in schema["properties"].items():
            generator = self.get_generator(v["type"])
            if generator is None:
                continue
            result[k] = generator(k, v)
        return result

    def generate_array(self, name, schema):
        n = self.fake.random_int(1, 5)
        generator = self.get_generator(schema["items"]["type"])
        result = []
        for i in range(n):
            result.append(generator(name, schema["items"]))
        if "enum" in schema["items"]:
            # remove duplicated
            result = list(set(result))
        return result

    def generate_string(self, name, schema):
        if "enum" in schema:
            return self.fake.random_element(schema["enum"])

        # some intelligence for MAC:
        fake_aliases = {
            "birthday": self.fake.past_date,
            "from": self.fake.past_date,
            "until": self.fake.past_date,
            "image": self.fake.image_url,
        }
        if name in fake_aliases:
            return str(fake_aliases[name]())

        if name.lower() in vars(self.fake):
            return getattr(self.fake, name.lower())()
        return self.fake.sentence()

    def generate_number(self, name, schema):
        return self.fake.random_number(1)

    def get_generator(self, kind):
        if kind == "object":
            return self.generate_dict
        if kind == "array":
            return self.generate_array
        if kind == "string":
            return self.generate_string
        if kind == "number":
            return self.generate_number
        print(f"No generator for {kind}")
        return None


def main():
    args = parse_args()
    init_logging(args.verbosity)

    with open(args.schema) as fd:
        generator = Generator(json.load(fd))
    data = generator.generate()

    with open(args.output, "w+") as fd:
        if args.output.lower().endswith(("yml", "yaml")):
            yaml.dump(data, fd)
        else:
            json.dump(data, fd, indent=2)


if __name__ == "__main__":
    main()
