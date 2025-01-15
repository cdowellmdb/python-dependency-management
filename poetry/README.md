
# Managing Python Dependencies with Poetry

This demonstrates a simple data science workflow using `pandas` and `scikit-learn`, managed with Poetry for streamlined dependency and environment management.

## Why Use Poetry?

Poetry simplifies Python project management by combining dependency management and virtual environment handling into a single tool. It offers:

- Easy creation and management of project environments.
- Automatic resolution of dependency conflicts.
- Lockfile generation for reproducible environments.
- Enhanced dependency declaration using `pyproject.toml`.

## Prerequisites

Ensure Poetry is installed on your system. Follow the [Poetry installation guide](https://python-poetry.org/docs/#installation) if needed.

## Setting Up the Project

1. **Initialize a Poetry Project:**

```bash
poetry init
```

    Answer the prompts to create a `pyproject.toml` file. Alternatively, use the `--no-interaction` flag for defaults.

2. **Add Dependencies:**

```bash
poetry add pandas scikit-learn
```

Poetry automatically resolves and locks dependencies in the `poetry.lock` file for consistent environments.

3. **Activate the Virtual Environment:**

```bash
poetry shell
```

4. **Run the Script:**

```bash
python data_pipeline.py
```

Or, if you prefer to run  without entering the poetry shell:

```bash
poetry run python data_pipeline.py
```

## Reproducing the Environment

To replicate the environment on a new machine:

1. **Clone the repository:**

```bash
git clone <repository-url> && cd <repository-directory>
```

2. **Install dependencies from the lockfile:**

```bash
poetry install
```

This ensures the exact versions of dependencies are used.

## Key Improvements Over pip/venv

- Unified Tooling: Poetry handles both dependency management and virtual environments, reducing the need for multiple tools like pip and venv.

- Reproducibility: The `poetry.lock` file ensures all collaborators use identical dependency versions, avoiding "it works on my machine" issues.

- Dependency Resolution: Poetry automatically resolves complex dependency trees and prevents version conflicts.

- Modern Syntax: The `pyproject.toml` file simplifies dependency declaration and aligns with modern Python packaging standards.

- Simplified Workflow: Common commands like `poetry add` and `poetry install` replace the need for manual `pip install` and `pip freeze` workflows.

## Deactivating the Environment

Exit the Poetry-managed shell with:
```bash
exit
```
or 

Notes for Data Science Projects
Poetry’s enhanced reproducibility is particularly useful in data science projects where library versions can significantly impact model behavior.
The poetry.lock file ensures environments are consistent across development, testing, and production.