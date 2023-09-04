from pathlib import Path
import subprocess

# Define the path to the "slides" folder as a relative path
slides_path = Path("slides")

# Check if the "slides" folder exists
if slides_path.exists() and slides_path.is_dir():

    # Run the command to create a virtual environment using Python's built-in venv module
    try:
        subprocess.run(
            f"python -m venv {slides_path.resolve()}/env", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running the venv command: {e}")

    # Open a new Terminal window, activate the virtual environment, install packages from requirements.txt,
    # and move the "requirements.txt" to the "env" folder
    try:
        osascript_command = f'''
        tell application "Terminal"
            do script "cd {slides_path.resolve()}; source env/bin/activate; pip install -r requirements.txt; mv requirements.txt env/"
        end tell
        '''
        subprocess.run(["osascript", "-e", osascript_command])
    except Exception as e:
        print(f"Error while opening a new Terminal window: {e}")
else:
    print(f"The folder {slides_path} does not exist or is not a directory.")

# source env/bin/activate
