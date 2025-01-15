# Template Project

This is a template project for a Python application using `uv` for dependency management and `pytest` for testing.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/)

To install `uv`, run the following command:

```sh
pip install uv -U
```

### How to use this template

1. Clone the repository:

    ```sh
    git clone https://github.com/rodneyxr/python-uv-template.git
    cd python-uv-template
    rm -rf .git
    ```

2. Install the dependencies:

    ```sh
    uv sync
    ```

### Running the application

```sh
uv run myapp
```

### Running Tests

```sh
uv run pytest --cov
```

#### Project Files
- `myapp/__main__.py`: Entry point for the command-line interface.
- `myapp/settings.py`: Application settings and configuration (automatically loads from `.env` using [`pydantic-settings`](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)).
- `myapp/utils/logger.py`: Custom logger configuration with source code info.
- `test/hello_test.py`: Example test file.

#### Configuration
- `pyproject.toml`: Project configuration file for `uv`.
- `poetry.lock`: Lock file for `uv` dependencies.
- `.python-version`:  Defines which Python version to use when creating the project's virtual environment.
- `.vscode/launch.json`: VS Code launch configuration.
- `.vscode/settings.json`: VS Code settings.

### License
This project is licensed under the MIT License.
