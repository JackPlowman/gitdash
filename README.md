# gitdash

## Table of Contents

- [gitdash](#gitdash)
  - [Table of Contents](#table-of-contents)
  - [Development](#development)
  - [Contributing](#contributing)

<!-- Add documentation -->

## Development

Install Python 3.13 and uv 0.13.5 or later in the 0.13 series, then run:

```sh
uv sync --locked
uv run --locked python src/run.py
uv run --locked python -m unittest discover -s tests -v
```

Use Prek 0.5.7 or later to install and run the Git hooks:

```sh
prek install
prek run --all-files
```

## Contributing

We welcome contributions to the project. Please read the [Contributing Guidelines](docs/CONTRIBUTING.md) for more information.
