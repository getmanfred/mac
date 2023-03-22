Utilities to work with MAC.

`jsonschema_generator.py` generates valid MACs with random values.

`mac_validate.py` checks if a MAC is valid or not, showing the errors.

# Usage

Despite not required, it is useful to create a virtual environment to avoid
installing global dependencies:

```
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $
```

then you can install dependencies:

```
(venv) $ pip install -r requirements.txt
```

And now you can generate a new CV and then check it:

```
python jsonschema_generator.py ../../schema/schema.json -o example1.json; ./mac_validate.py example1.json
```

Do not expect values to have sense, just to be valid according to the MAC
jsonschema.

Also, to exit the previously created virtual environment:
```
(venv) $ deactivate
$
```