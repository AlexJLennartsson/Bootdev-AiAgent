import os

#def get_files_info(working_directory, directory=None):
  #working_directory_full = os.path.join(working_directory, directory)
  #print(working_directory_full)

def get_files_info(working_directory, directory=None):
  try:
    if directory == ".":
      print("Result for current directory:")
    else:
      print(f"Result for '{directory}' directory")
    working_directory_full = os.path.abspath(working_directory)
    directory_full = os.path.abspath(os.path.join(working_directory, directory))
    if(directory != "." and directory not in os.listdir(working_directory_full)):
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if(not os.path.isdir(directory_full)):
      return f'Error: "{directory}" is not a directory'

    dir_contents = os.listdir(directory_full)
    dot_files = []
    for item in dir_contents:
      if item.startswith('.'):
        dot_files.append(item)
    dir_contents = [item for item in dir_contents if item not in dot_files]

    for item in dir_contents:
      full_item_path = os.path.join(directory_full, item)
      print(f' - {item}: file_size={os.path.getsize(full_item_path)} bytes, is_dir={os.path.isdir(full_item_path)}')
  except Exception as e:
    return(f'Error: {e}')