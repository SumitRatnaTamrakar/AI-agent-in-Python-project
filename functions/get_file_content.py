import os
from config import MAX_CHARS

from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    rel_file_path = os.path.join(abs_working_directory, file_path)
    abs_file_path = os.path.abspath(rel_file_path)

    if not abs_file_path.startswith(abs_working_directory):
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(abs_file_path):
        return (f'Error: File not found or is not a regular file: "{file_path}"')
        
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1)

        if len(file_content_string) > MAX_CHARS:
            file_content_string = file_content_string[:MAX_CHARS]
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except Exception as e:
        return (f"Error: {e}")
    

schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the contents of a single file at file_path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)