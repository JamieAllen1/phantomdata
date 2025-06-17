# phantomdata

**phantomdata** is an open-source Python tool designed to generate synthetic datasets based on schema definitions. It helps with integration testing and data pipeline validation by producing realistic, schema-compliant data.

## 🚀 Features

- **Schema-Driven Generation**: Produce data that adheres to defined schemas, ensuring consistency across tests.
- **Multiple Output Formats**: Support for CSV, Parquet, and other common data formats.
- **Customizable Data Profiles**: Define data characteristics to match specific testing scenarios.
- **CLI Interface**: Easily generate data via command-line commands.

## 📦 Installation

Ensure you have Python 3.10 or higher installed.

### Using pip

```bash
pip install phantomdata
```

### Using Poetry

```bash
poetry add phantomdata
```

## 🛠️ Usage
After installation, you can generate synthetic data using the CLI:

```bash
phantomdata generate --schema path/to/schema.yaml --rows 1000 --output data.csv
```

## 📄 Schema Definition
Schemas are defined in YAML format. Here’s an example schema:

```yaml
fields:
  - name: id
    type: integer
    min: 1
    max: 1000
  - name: name
    type: string
    pattern: "[A-Za-z]{5,10}"
  - name: signup_date
    type: date
    start: "2020-01-01"
    end: "2021-12-31"
```
This schema defines three fields: an integer id, a name string matching a regex pattern, and a signup_date within a specified range.

## Testing

To run tests using Poetry:
```bash
poetry run pytest
```
Make sure all dependencies are installed and the virtual environment is activated.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss your proposed modifications.

Make sure your code adheres to the project’s coding standards and passes all tests.

## License

This project is licensed under the GNU General Public License v3.0.
You may copy, distribute, and modify the software as long as you track changes/dates in source files.
Any derivative work must also be open-sourced under the same GPL license.

See the [COPYING](COPYING) file for the full text.
