import csv
import os

github_folder = "code"
output_filename = "output.csv"


def get_current_folder_name():
    # Get the current working directory
    current_directory = os.getcwd()

    # Extract the current folder name from the path
    current_folder_name = os.path.basename(current_directory)

    return current_folder_name


lab_name = get_current_folder_name()


def list_notebook_files(directory="code"):
    # List all files in the given directory
    files = os.listdir(directory)

    # Filter out only .ipynb files
    notebook_files = [file for file in files if file.endswith('.ipynb')]

    return notebook_files


notebook_files = list_notebook_files()


def generate_csv(lab_name, github_folder, notebook_files, output_filename):
    # Initialize list to store data rows
    data = []
    header = ["nr", "lab", "github", "name", "colab", "link"]
    data.append(header)

    base_url = "https://colab.research.google.com/github/kirenz/{}/blob/main/{}/{} "

    # Loop through each notebook file and generate the required data
    for idx, file in enumerate(notebook_files, start=1):
        colab_link = base_url.format(lab_name, github_folder, file)
        markdown_link = "- [💻 Jupyter Notebook]({})".format(colab_link)

        row = [idx, lab_name, github_folder, file, colab_link, markdown_link]
        data.append(row)

    # Write the data to the CSV file
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


generate_csv(lab_name, github_folder, notebook_files, output_filename)


def list_notebook_files(directory="code"):
    # List all files in the given directory
    files = os.listdir(directory)

    # Filter out only .ipynb files
    notebook_files = [file for file in files if file.endswith('.ipynb')]

    return notebook_files


def generate_csv(lab_name, github_folder, notebook_files, output_filename):
    # Initialize list to store data rows
    data = []
    header = ["Markdown Link"]
    data.append(header)

    base_url = "https://colab.research.google.com/github/kirenz/{}/blob/main/{}/{}"

    # Loop through each notebook file and generate the required data
    for file in notebook_files:
        colab_link = base_url.format(lab_name, github_folder, file)
        markdown_link = "- [💻 Jupyter Notebook]({})".format(colab_link)

        row = [markdown_link]
        data.append(row)

    # Write the data to the CSV file
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def get_current_folder_name():
    # Get the current working directory
    current_directory = os.getcwd()

    # Extract the current folder name from the path
    current_folder_name = os.path.basename(current_directory)

    return current_folder_name


# Usage:
lab_name = get_current_folder_name()
github_folder = "code"
notebook_files = list_notebook_files()
output_filename = "output_links.csv"

generate_csv(lab_name, github_folder, notebook_files, output_filename)
