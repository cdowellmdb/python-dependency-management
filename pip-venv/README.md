# Managing Python Dependencies with pip and venv for Data Science

This project demonstrates a simple data science workflow using `pandas` for data manipulation and `scikit-learn` for machine learning.

## Prerequisites

Ensure you have Python 3.7 or later installed on your system.

## Setting Up the Environment

1. **Create a Virtual Environment**

    Run the following command in the project directory to create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

2. **Activate the Virtual Environment**

    - Linux/MacOS:
    ```bash
    source venv/bin/activate
    ```
    - Windows:
    ```bash
    venv\Scripts\activate
    ```

3. **Install Dependencies**

    Use pip to install the required packages:
    ```bash
    pip install pandas scikit-learn
    ```

4. **Run the Script**

    Execute the script:

    ```bash
    python data_pipeline.py
    ```
The script trains a simple linear regression model and evaluates it, printing the Mean Squared Error to the console.

## Managing Dependencies

1. **Freeze Dependencies**

    Save the environment's dependencies to a `requirements.txt` file:

    ```bash
    pip freeze > requirements.txt
    ```
    This ensures reproducibility of the environment.

2. **Reinstall Dependencies**

To recreate the environment on a new machine, run:

    ```bash
    pip install -r requirements.txt
    ```

## Deactivating the Environment
    Exit the virtual environment by running:

    ```bash
    deactivate
    ```

## Notes
- Always have to manually update the `requirements.txt` file when installing new libraries or updating existing ones.
- `requirements.txt` does not provide any information on python versioning.

