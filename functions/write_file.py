import os

def write_file(working_directory, file_path, content):
  try:
    working_directory_full = os.path.realpath(working_directory)
    file_path_full = os.path.realpath(os.path.join(working_directory, file_path))
    if(working_directory_full not in file_path_full):
      return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    with open(file_path_full, 'w') as file:
      file.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
    return f'Error: {e}'