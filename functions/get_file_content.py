import os
import asyncio 

def read_file(file: str) -> str:
    """Read content of the file.

    Args:
        file (str): path to the file.

    Returns:
        str: contnet of the file in a format.
    """
    result = ""
    with open(file, 'r') as f:
        result += f.read(10000)
        leftover = f.read()
        if leftover:
            result+=f'\n[...File "{file}" truncated at 10000 characters]'
    
    return result

async def get_file_content(working_directory, file_path):
    
    expanded_base_path = await asyncio.to_thread(os.path.expanduser, "~/Projects/ai_agent/")
    working_directory = os.path.join(expanded_base_path, working_directory)

    ls_working_dir = await asyncio.to_thread(os.listdir, working_directory)
    file_paths = file_path.split('/')
    if file_paths[0] not in ls_working_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if len(file_paths) > 1:
        return await get_file_content(
            os.path.join(working_directory, file_paths[0]),
            '/'.join(file_paths[1:])
        )
    file = os.path.join(working_directory, file_path)
    if not os.path.isfile(file):
        return f'Error: File not found or is not a regular file: "{file}"'

    try:
        result = await asyncio.to_thread(read_file, file)
    except FileNotFoundError as e:
        return f'Error: File not found or is not a regular file: "{file}"'

    return result

