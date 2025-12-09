import os
from google.genai import types

def write_file_content(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    rel_file_path = os.path.join(abs_working_directory, file_path)
    abs_file_path = os.path.abspath(rel_file_path)
        
    if not abs_file_path.startswith(abs_working_directory):
        return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    file_dir = os.path.dirname(abs_file_path)

    if not os.path.exists(file_dir):
        try:
            os.makedirs(file_dir)
        except Exception as e:
            return f"Error: {e}"
        
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: {e}"
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file_content",
    description="Writes file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The exact text content to write to the file."
            )
        },
        required=["file_path", "content"],
    ),
)