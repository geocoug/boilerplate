# Boilerplate

[![ci/cd](https://github.com/geocoug/boilerplate/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/geocoug/boilerplate/actions/workflows/ci-cd.yaml)

Generalized starter template for developing Python applications.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository: `git clone https://github.com/geocoug/boilerplate.git`
2. Rename the project directory: `mv boilerplate <project-name>`
3. Change to the project directory: `cd <project-name>`
4. Initialize the project environment: `make init`
5. Modify the project content as needed.

## Components

### uv

This project uses [uv](https://github.com/astral-sh/uv) to manage Python virtual environments. To install `uv`, follow these [getting started](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started) instructions.

### Python

This project requires Python 3.10 or higher. To install Python, follow the instructions on the [Python website](https://www.python.org/downloads/).

The following Python packages are required for this project:

- `mkdocs`
- `mkdocs-material`
- `mkdocstrings`
- `mkdocstrings[python]`
- `markdown-include`
- `pytest`
- `pytest-cov`
- `bump-my-version`
- `ruff`
- `pre-commit`
- `twine`

### Makefile

This project uses a `Makefile` to manage commands. The `make` command is required to run the commands in the `Makefile`. To install `make`, follow the instructions for your operating system:

- [Windows](http://gnuwin32.sourceforge.net/packages/make.htm)
- **MacOS**: `brew install make`
- [Linux](https://www.gnu.org/software/make/)

The [`Makefile`](./Makefile) contains a set of commands to help with development. The following commands are available:

```text
help          show this help
init          Initialize the project environment (venv & pre-commit)
clean         Remove temporary files
bump          Show the next version
bump-patch    Bump patch version
bump-minor    Bump minor version
bump-major    Bump major version
update        Update pre-commit
lint          Run pre-commit hooks
test          Run unit tests
build-dist    Generate distribution packages
build-docker  Build Docker image
build-docs    Generate documentation
preview-docs  Serve documentation
publish       Publish to PyPI
build         Build the project
start-api     Start the API
stop-api      Stop the API
```

To run a command, use the following syntax:

```bash
make <command>
```

There are several commands that are useful initializing the project, building the project, running tests, performing cleanup, and more. To get started with the project, run the command `make init` to initialize a virtual environment, install dependencies, and set up pre-commit hooks.

> The `make init` command will create a virtual environment using the [uv](https://github.com/astral-sh/uv) package. If you do not have `uv` installed, you can follow the [getting started instructions here](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started)

### Documentation

Documentation is generated using [MkDocs](https://www.mkdocs.org/). The documentation is written in Markdown and is located in the [`docs`](./docs) directory. The documentation is intended to be hosted on [readthedocs](https://readthedocs.io/), which is configured in the [`.readthedocs.yaml`](./.readthedocs.yaml) file.

To build the documentation locally, run the command `make build-docs`. The documentation will be built in the `site` directory.

To preview documentation, run the command `make serve-docs`.

### Testing

Testing is done using [pytest](https://docs.pytest.org/en/stable/). Tests are located in the [`tests`](./tests) directory. To run tests, run the command `make test`.

### Continuous Integration

Continuous integration is done using GitHub Actions. The workflow is defined in the [`.github/workflows/ci-cd.yaml`](./.github/workflows/ci-cd.yaml) file. The workflow runs tests, builds docker images, and builds then pushes the Python package to [PyPI](https://pypi.org/) on every push to the `main` branch.

### Code Quality

Code quality is enforced using [pre-commit](https://pre-commit.com/). The configuration is defined in the [`.pre-commit-config.yaml`](./.pre-commit-config.yaml) file. To install and run the pre-commit hooks, run the command `make lint`.

### Semantic Versioning

The project uses [semantic versioning](https://semver.org/). The version is stored in the [`pyproject.toml`](./pyproject.toml) file, which also contains instructions for dynamically updating the version in Python code.

To view the current version, run the command `make bump`. To bump the version, run the command `make bump-patch`, `make bump-minor`, or `make bump-major`.

### Docker

The project is containerized using [Docker](https://www.docker.com/). The[`Dockerfile`](./Dockerfile) is used to package the boilerplate module as a Docker image for deployment. A `docker-compose` file is provided to run the API, which uses [Caddy](https://caddyserver.com/) as a reverse proxy to serve the API. The docker-compose file utilizes the same Dockerfile as the boilerplate module to deploy the API. To build the Docker image, run the command `make build-docker`. To run the API, run the command `make start-api`. To stop the API, run the command `make stop-api`.

### Publishing

The project can be published to [PyPI](https://pypi.org/) using the [`twine`](https://twine.readthedocs.io/) package. To publish the package, run the command `make publish`, or use the GitHub Actions workflow to automatically publish the package on every push to the `main` branch.
