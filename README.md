# phantomdata

**phantomdata** is an open-source Python tool designed to generate synthetic datasets based on schema definitions. It helps with integration testing and data pipeline validation by producing realistic, schema-compliant data.

## 🚀 Features

- **Schema-Driven Generation**: Produce data that adheres to defined schemas, ensuring consistency across tests.
- **Multiple Output Formats**: Support for CSV, Parquet, and other common data formats.
- **Customizable Data Profiles**: Define data characteristics to match specific testing scenarios.
- **CLI Interface**: Easily generate data via command-line commands.

## 📦 Installation

Ensure you have Python 3.12 or higher installed.

### Using Poetry

```bash
poetry add phantomdata
```
Then enbale the virtual environment. To find the virtual environment,
```bash
poetry env activate
```
Run the command from the above to start the environment and you're good to go.

## 🛠️ Usage
After installation, you can generate synthetic data using the CLI:

```bash
phantomdata generate --schema examples/tables.yaml --rows 1000 --outputformat csv --outputpath data
```

## 📄 Schema Definition
Schemas are defined in YAML format. Here’s an example schema:

```yaml
tables:
  - table:
    name: users
    count: 1000
    columns:
      - name: id
        type: integer
        domain: id
      - name: name
        type: string
        domain: name
      - name: signup_date
        type: date

```
This schema defines three fields: an integer id, a name string matching a regex pattern, and a signup_date.

## Data Types
| Data Type |  What you get |
|----------:|:--------------|
| integer   | A random integer, between min and max if set. Otherwise any value to max_int. |
| decimal   | A random decimal value, fitting the scale and precision requirements defined. |
| string    | A random string value. If the domain 'upper' is defined, ths is then used.  |
| boolean   | A random true or false value. |

## Data Domains

Phantomdata makes use of the term 'domain' to support a variety of pre-canned data formats that enable you to define a range of pre-formatted variables. Note that some domains will enforce the data type based on the data domain defintion and will ignore the data type setting above if specified.

The following domains are available:

| Domain      | Data Type |  What you get |
|------------:|----------:|:--------------|
| id          | integer   | Each row is numbered from 1 to the actual row count. |
| fixed       | any       | Each row contains the exact value specified in the value column. |
| list        | string    | Each row gets a random word from a predefined list of thousands of words. |
| name        | string    | Each row gets a random name generated from thousands of names.  |
| email       | string    | Each row gets a randomly generated email address. |
| age         | integer   | Each row gets a generated age between the ages of 18 to 80. |
| date        | date      | Each row gets a random date from this year. |
| datetime    | datetime  | Each row gets a random date and time from this year. |
| time        | time      | Each row gets a random time value.  |
| upper       | string    | Each row gets random uppercase text to string length specified. |

## Output formats
Phantomdata will output to a number of output formats with more to be added in the future. The following are currently supported.

### CSV/JSON/Parquet
Data is written out to an output file in the output path specified.

### Postgres
Given postgres connection details in the command line, Phantomdata will create (or replace, if specified), tables in the postgres database with the structure defined in the defintion file and the data generated from the process. The following additional command line arguments are required:

dbconnection - Postgres connection string
dbschema  - The Postgres DB schema to write the table to
dbreplace - If you want the existing table overwritten (the default setting)

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
