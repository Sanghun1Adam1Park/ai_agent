import os 

def get_files_info(working_directory, directory=None):
    
    expanded_base_path = os.path.expanduser("~/Projects/ai_agent/")
    working_directory = os.path.join(expanded_base_path, working_directory)
    # if directory is out of working_D 
    ls_working_dir = os.listdir(working_directory)
    if directory != '.' and directory not in ls_working_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    directory = os.path.join(working_directory, directory)
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'


    ls_dir = list(map(lambda x: os.path.join(directory, x), os.listdir(directory)))
    result = ""
    for file in ls_dir:
        is_dir = os.path.isfile(file)
        size = os.path.getsize(file)
        result += f"- {file}: file_size={size} bytes, is_dir={is_dir} \n"

    return result

