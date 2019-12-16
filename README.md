# Python API Example

This is an example for python api projects.

![Github Workflow](https://github.com/claick-oliveira/python-api-example/workflows/Python%20package/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<a href="https://asciinema.org/a/288589?autoplay=1"><img src="https://asciinema.org/a/288589.svg" width="836"/></a>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project.

### Prerequisites

- git
- make
- python 3.7
- pip
- virtualenv
- vscode

### Installing

First of all you need to clone this repository:

``` bash
git clone https://github.com/claick-oliveira/python-api-example.git
```

After clone access the folder and create your virtual env:

``` bash
cd python-package-example
make venv
```

Now let's activate your virtual env:

``` bash
make activate
```

To start to code you need to install the requirements and de dev requirements:

``` bash
make requirements
make requirementsdev
```

## Running the tests

To run the tests you need to execute:

``` bash
make test
```

### And coding style tests

In this project we'll use [PEP 8](https://www.python.org/dev/peps/pep-0008/) as style guide.

## Running the server

To run the server you need to execute:

``` bash
make server
```

## Clean

To clean the files generated as coverage, builds, env you can use:

``` bash
make clean
```

If you prefer to clear all, use:

```bash
make cleanfull
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/claick-oliveira/python-api-example/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Claick Oliveira** - *Initial work* - [claick-oliveira](https://github.com/claick-oliveira)

See also the list of [contributors](https://github.com/claick-oliveira/python-api-example/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
