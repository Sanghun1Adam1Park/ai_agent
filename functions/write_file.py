import os 

def write_file(working_directory, file_path, content):
    expanded_base_path = os.path.expanduser("~/Projects/ai_agent/")
    working_directory = os.path.join(expanded_base_path, working_directory)

    ls_working_dir = os.listdir(working_directory)
    file_paths = file_path.split('/')
    if len(file_paths) > 1:
        if file_paths[0] not in ls_working_dir:
            return f'Error: Cannot write to "{file_paths[0]}" as it is outside the permitted working directory'
        return write_file(
            os.path.join(working_directory, file_paths[0]),
            '/'.join(file_paths[1:]),
            content
        )

    file = os.path.join(working_directory, file_path)
    try:
        with open(file, 'w') as f:
            f.write(content)
    except FileNotFoundError as e:
        return f'Error: File not found or is not a regular file: "{file}"'

    return f'Successfully wrote to "{file}" ({len(content)} characters written)'
