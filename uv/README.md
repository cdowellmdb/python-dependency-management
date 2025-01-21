# Managing Python Dependencies with uv

## Why Use `uv`?

`uv` is a modern Python dependency management tool that simplifies environment management and enhances reproducibility. It builds on the strengths of tools like `pip`, `venv`, and `poetry` while offering unique benefits:

- Native Python Syntax: Leverages `pyproject.toml` for cleaner project configuration.

- Python Version Management: Installs and manages multiple Python versions seamlessly. 

- Enhanced Isolation: Fully isolates dependencies and avoids interference with global Python installations.

- Streamlined Workflows: Handles environment creation, dependency resolution, and lockfile management seamlessly.

- Performance: Efficient dependency resolution and installation speed.

## Why not use `uv`?

It's a VC backed company that owns this entire tool and, while it's open source, there's always the questioning of the company changing the licensing.

## Links

[Github Link to UV](https://github.com/astral-sh/uv)
[Docs](https://docs.astral.sh/uv/)

## Setting Up the Project with `uv`
1. **Install `uv`**

    First, ensure you have uv installed on your system. If not, install it using pip:

    ```bash
    pip install uv
    ```

    Verify you have `uv` installed by running:

    ```bash
    uv
    ```

2. **Initialize the Project**

    Create a new `uv` environment and initialize the project:

    ``bash
    uv init --no-package --no-readme --no-workspace
    ```
    This sets up a virtual environment and creates a `pyproject.toml` file in the current directory.

3. **Manage Python Versions**

    `uv` allows you to specify and manage Python versions. To install a specific Python version:

    ```bash
    uv python install 3.11.4
    ```

    To set this version as the default for the project
    ```bash
    uv python pin 3.11.4
    ```

    This will ensure the project uses Python 3.11.4, providing consistency across different development environments.

4. **Add Dependencies**

    Add the required libraries for the project:

    ```bash
    uv add pandas scikit-learn
    ```
    This automatically resolves dependencies and locks versions in a `uv.lock` file.

5. **Run the Script**

    Execute the script directly:

    ```bash
    uv run python data_pipeline.py
    ```

## Reproducing the Environment

To replicate the environment on a new machine:

1. **Clone the repository:**

    ```bash
    git clone <repository-url> && cd <repository-directory>
    ```
2. **Install dependencies:**

    ```bash
    uv install
    ```

3. **Run the script:**

    ```bash
    uv run python data_pipeline.py
    ```

## Key Benefits of uv Over Other Tools

- Integrated Python Version Management: `uv` installs and manages multiple Python versions, allowing seamless switching and ensuring compatibility with project requirements. 

- Unified Workflow: `uv` combines environment creation, dependency management, and isolation in a single tool, reducing complexity.

- Reproducibility: The `uv.lock` file ensures consistent environments across systems, just like Poetry.

- Performance: `uv` is optimized for speed, especially when resolving dependencies and creating environments.

- Simplicity: Minimal boilerplate and commands for setup and execution.

- Portability: Fully isolated environments reduce issues with system-level Python dependencies.


## Other Benefits

### Script Support with Inline Metadata:

`uv` allows you to manage dependencies directly within single-file scripts using inline metadata.

This feature enables automatic creation of isolated environments tailored to each script's requirements, enhancing reproducibility and simplifying script execution.

Example:
```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
# ]
# ///
import rich
```
By including this metadata, running the script with `uv` ensures that the specified Python version and dependencies are automatically managed. 

### Ephemeral Environment Execution:

uv facilitates running Python applications in ephemeral (temporary) environments, ensuring that your global environment remains unaffected.

This is useful for testing or running scripts with specific dependencies without long-term environment modifications.
Example:

```bash
uvx pycowsay 'hello world!'
```
This command runs `pycowsay` in an ephemeral environment, installing it if necessary, without altering your global setup. 

### Comprehensive Project Management:

`uv` provides tools for initializing and structuring Python projects, making it easier to maintain organized and consistent project directories.

It supports building and publishing packages, facilitating the distribution of your data science tools and models.
Example:
```bash
uv init example-project
cd example-project
uv add pandas scikit-learn
```
These commands set up a new project with the necessary dependencies, streamlining project initialization. 

### Support for Cargo-Style Workspaces:

`uv` supports Cargo-style workspaces, allowing you to manage multiple related projects within a single repository.

This is advantageous for complex data science projects that involve multiple components or modules, enabling efficient management and integration.

This command adds project-a and project-b to the workspace, facilitating coordinated development. 

### Exporting Dependencies

`uv` supports exporting `uv.lock` dependencies to alternative formats:

```bash
uv export > requirements.txt
```

This is useful for other environments where you may still need to provide a `requirements.txt` file.

### Building Packages with uv**

`uv` simplifies the creation of source distributions and wheels, essential for sharing your Python projects.

1. **Prepare Your Project:** 

    Ensure your project includes a `pyproject.toml` file with the necessary metadata. This file defines your project's build system and dependencies.

2. **Build the Package:**

    Execute the following command in your project's root directory:

    ```bash
    uv build
    ```

This command generates distribution files (e.g., `.tar.gz` and .`whl`) in the `dist/` directory, ready for distribution. 

### Publishing Packages with uv

`uv` facilitates seamless uploading of your packages to package registries like PyPI.

1. **Configure Publishing Credentials:**

    Set your registry credentials using environment variables or command-line options. For example:

    ```bash
    export UV_PUBLISH_TOKEN=your_pypi_token
    ```

    Alternatively, pass the token directly:

    ```bash
    uv publish --token your_pypi_token
    ```

    Ensure your `pyproject.toml` includes the appropriate metadata, such as the package name, version, author, and description.

2. **Publish the Package:** 

    Run:

    ```bash
    uv publish
    ```
    This command uploads your package to the specified registry, making it available for installation. 
