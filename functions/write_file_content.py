import os

def write_file(working_directory, file_path, content):
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