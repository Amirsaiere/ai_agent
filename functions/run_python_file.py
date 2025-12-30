import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir,file_path))
        if os.path.commonpath([working_dir, target_file]) != working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if target_file[-3:] != '.py':
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args:
            command.extend(args)
        result = subprocess.run(command,capture_output=True,text=True,timeout=30)
        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}"
        if not result.stderr and not result.stdout:
            output += "No output produced"
        elif result.stdout:
            output += f"STDOUT:{result.stdout}"
        elif result.stderr:
            output += f"STDERR:{result.stderr}"
        return output
    except Exception as e:
        return f'Executing Python file: "{e}"'