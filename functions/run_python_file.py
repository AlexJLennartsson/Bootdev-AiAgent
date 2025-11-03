import os
import subprocess

def run_python_file(working_directory, file_path, args=[]): 
  try:
    working_directory_full = os.path.realpath(working_directory)
    file_path_full = os.path.realpath(file_path)
    if(working_directory_full not in file_path_full):
      return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if(not os.path.isfile(file_path_full)):
      return f'Error: File "{file_path}" not found.'
    if(file_path[-3:] != ".py"):
      return f'Error: "{file_path}" is not a Python file.'

    subprocess.run(args=args, capture_output=True, timeout=30, env=)

  except Exception as e:
    return f'Error: {e}'