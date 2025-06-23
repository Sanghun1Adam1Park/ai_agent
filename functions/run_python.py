import os 
import sys 
import subprocess

def run_python_file(working_directory, file_path):
    expanded_base_path = os.path.expanduser("~/Projects/ai_agent/")
    working_directory = os.path.join(expanded_base_path, working_directory)

    ls_working_dir = os.listdir(working_directory)
    file_paths = file_path.split('/')
    if (file_paths[-1].split('.')[-1] != "py"):
        return f'Error: "{file_path}" is not a Python file.'
    if len(file_paths) > 1:
        if file_paths[0] not in ls_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        else: 
            return write_file(
                os.path.join(working_directory, file_paths[0]),
                '/'.join(file_paths[1:]),
                content
            )
    if len(file_paths) == 1 and file_paths[0] not in ls_working_dir:
        return f'Error: File "{file_path}" not found.'

    file = os.path.join(working_directory, file_path)
    try:
        result = subprocess.run(
            [sys.executable, file.split('/')[-1]],
            timeout=30, 
            capture_output=True,
            text=True, 
            cwd=working_directory
        )
        
        res = f"Ran {file}:\n"

        res += f"Process exited with code {result.returncode}\n"
        if result.returncode == 0:
            res += f"STDOUT:\n {result.stdout}\n"
        else:
            res += f"STDERR:\n {result.stderr}\n"
     
        return res 
    except Exception as e:
        return f"Error: executing Python file: {e}"




