from pathlib import Path
import subprocess
import shutil

# Define the path to the "slides" folder as a relative path
slides_path = Path("slides")

# Check if the "slides" folder exists
if slides_path.exists() and slides_path.is_dir():

    # Run the conda command to create the environment with Python 3.11
    try:
        subprocess.run(
            f"cd {slides_path.resolve()} && conda create --prefix ./env python=3.11 -y", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running the conda command: {e}")

    # Open a new Terminal window and activate the Conda environment
    try:
        osascript_command = f'''
        tell application "Terminal"
            do script "cd {slides_path.resolve()}; conda activate ./env"
        end tell
        '''
        subprocess.run(["osascript", "-e", osascript_command])
    except Exception as e:
        print(f"Error while opening a new Terminal window: {e}")

    # Move the "requirements.txt" file to the "env" folder
    try:
        shutil.move(str(slides_path / "requirements.txt"),
                    str(slides_path / "env/requirements.txt"))
    except FileNotFoundError:
        print("requirements.txt not found. Skipping the move operation.")
 #   except FileNotFoundError:
 #       print(f"The folder {slides_path} does not exist or is not a directory.")


####################################
# Nächste Schritte

# Alternativ:  activate in vs code
# conda activate ./env

# Export pip
# python3 -m pip freeze > requirements.txt

# Installation der Module
# python3 -m pip install -r requirements.txt

# Export anaconda yml
# conda env export > environment.yml

# Restore env
# conda env create --prefix env -f environment.yml
