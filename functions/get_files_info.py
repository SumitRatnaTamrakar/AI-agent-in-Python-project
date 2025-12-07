import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    
    relative_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(relative_path)
    working_directory_absolute_path = os.path.abspath(working_directory)

    if absolute_path.startswith(working_directory_absolute_path):
        try:
            if os.path.isdir(absolute_path):
                directory_contents = os.listdir(absolute_path)
                string = ""
                for content in directory_contents:
                    path_to_content = os.path.join(absolute_path, content)
                    string += (f"- {content}: file_size={os.path.getsize(path_to_content)} bytes, is_dir={os.path.isdir(path_to_content)}") + "\n"
                return string
            else:
                return(f'Error: "{directory}" is not a directory')
        except Exception as e:
            return f"Error: {str(e)}"            
    else:    
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')


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

available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
)

