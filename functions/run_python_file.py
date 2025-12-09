import os
import subprocess

from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    # abs_working_directory = os.path.abspath(working_directory)
    # rel_file_path = os.path.join(abs_working_directory, file_path)
    # abs_file_path = os.path.abspath(rel_file_path)

    abs_working_directory = os.path.abspath(working_directory)
    rel_file_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(rel_file_path)

# Boot's suggested approach
    # abs_working_directory = os.path.abspath(working_directory)
    # abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:

        commands = ["python", abs_file_path] # abs_file_path is your absolute path to the Python script
        
        if args: # This checks if the 'args' list is not empty
            commands.extend(args)

        # Now, the 'commands' list is ready to be passed to subprocess.run
        # It will contain ["python", abs_file_path]
        # AND, if 'args' had items, it will also contain all those items at the end.

        completed_process = subprocess.run(
            commands,
            timeout=30,
            capture_output=True,
            text = True,
            cwd=abs_working_directory,)

        output_lines = []
        if completed_process.stdout:
            output_lines.append(f"STDOUT:\n{completed_process.stdout}")

        if completed_process.stderr:
            output_lines.append(f"STDERR:\n {completed_process.stderr}")
        
        if completed_process.returncode:
            output_lines.append(f"Process exited with code {completed_process.returncode}")

        if len(output_lines) == 0:
            output_lines.append("No output produced")
    
        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs Python files in the specified file_path along with the response outputs, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to the python file to run, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)