# Boilerplate

[![ci](https://github.com/geocoug/boilerplate/actions/workflows/ci.yml/badge.svg)](https://github.com/geocoug/boilerplate/actions/workflows/ci.yml)
[![pre-commit.ci](https://results.pre-commit.ci/badge/github/geocoug/boilerplate/main.svg)](https://results.pre-commit.ci/latest/github/geocoug/boilerplate/main)
![license](https://img.shields.io/github/license/geocoug/boilerplate)

Generalized starter template for developing Python applications.

## Notes

### Unit Testing

There are two popular unit testing frameworks for Python: [unittest](https://docs.python.org/3/library/unittest.html) and [pytest](https://docs.pytest.org). Unittest is a standard Python library while Pytest comes from a third party. At least one of them should be used on your codebase.

- Test with unittest: `python -m unittest discover -v`

- Test with pytest: `python -m pytest -v`

### Pre-commit

[Pre-commit](https://pre-commit.com/) hooks will be triggered by `git commit` which inspects the snapshot of a staged commit. Pre-commit hooks are a good way to enforce standards.

1. Install the hook environments: `python -m pre_commit install --install-hooks`
1. Run the hooks: `python -m pre_commit run --all-files`
1. Keep hooks updated: `python -m pre_commit autoupdate`

### Docker

[Docker](https://www.docker.com/) may not be necessary for stand-alone codes that do not have many dependencies, but is extremely useful when working with multiple tools that all require their own set of dependencies. Docker will keep your environment(s) isolated so you don't have to worry about messing up your own system.

#### Using Docker containers to run your code

1. Build the image: `docker build -t api .`
1. Run an instance of the image using a bind mount to attach our application code (`./app/`) to the container:
   1. Terminate container when finished: `docker run -it --rm -v $(pwd)/app:/usr/local/app api`
   1. Run in background: `docker run -d --name api-container -v $(pwd)/app:/usr/local/app api`

Shorthand: `docker run -it --rm -v $(pwd)/app:/usr/local/app $(docker build -q -t api .)`

#### Alternatively

1. Create a [docker-compose.yml](docker-compose.yml) file and build multiple services with `docker compose up -d`
