import os
from config import MAX_CHARS

# MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
        try:
            working_dir = os.path.abspath(working_directory)
            target_file_path = os.path.normpath(os.path.join(working_dir,file_path))
            if os.path.commonpath([working_dir, target_file_path]) != working_dir:
                return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
            if not os.path.isfile(target_file_path):
                return f'Error: File not found or is not a regular file: "{file_path}"'
            with open(target_file_path,'r') as f:
                file_content_string = f.read(MAX_CHARS+1)
            if len(file_content_string) > MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
        except Exception as e:
             return f'Error retrieving file content: "{e}"' 
