import os

def get_file_content(working_directory, file_path):
  working_directory_full = os.path.abspath(working_directory)
  file_path_full = os.path.abspath(os.path.join(working_directory, file_path))
  working_directory_list = []
  for item in os.listdir(working_directory_full):
    working_directory_list.append(os.path.abspath(os.path.join(working_directory, item)))
  
  print(os.path.abspath(file_path))
  if(file_path not in os.listdir(working_directory_full)):
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  if(not os.path.isfile(file_path_full)):
    return f'Error: File not found or is not a regular file: "{file_path}"'