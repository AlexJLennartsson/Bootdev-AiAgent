import os
from functions.config import FILE_CHARACTER_LIMIT

def get_file_content(working_directory, file_path):
  working_directory_full = os.path.realpath(working_directory)
  file_path_full = os.path.realpath(os.path.join(working_directory, file_path))
  
  if(working_directory_full not in file_path_full):
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  if(not os.path.isfile(file_path_full)):
    return f'Error: File not found or is not a regular file: "{file_path}"'

  file = open(file_path_full, 'r')
  if(len(file) > FILE_CHARACTER_LIMIT):
    file = file[0:10001] + f'...File "{file_path}" truncated at {FILE_CHARACTER_LIMIT} characters'
  print(file)