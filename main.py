import os

def create_subfolder_name (index :int, Name:str):
    formatted_number = f"{index:04d}"
    merged_string = f"{formatted_number}_{Name}"
    return merged_string

def get_subdirectories (directory:str):
    try:
        return [subdir for subdir in os.listdir(directory) if os.path.isdir(os.path.join(directory, subdir))]
    except (FileNotFoundError, PermissionError) as e:
        print(f"Fehler: {e}")
        return []

def get_id_from_subfolders(subfolders):
    numbers = []
    for folder in subfolders:
        if len(folder) >= 4:
            try:
                number = int(folder[:4])  # Versuch, die ersten 4 Zeichen in eine Zahl umzuwandeln
                numbers.append(number)
            except ValueError:
                pass  #
    return numbers

def folder_name_valid (folder_name:str,subfolders:list):
    if len(folder_name) < 5 or folder_name in subfolders:
        return False
    target_prefix = folder_name[:4]
    return not(any(s[:4] == target_prefix for s in subfolders)) #True if target_prefix is new

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Beispielaufruf
    input_directory = "D:\Programmierung\BYD-OPL"
    subfolders = get_subdirectories(input_directory)
    new_folder_name  = create_subfolder_name (6,"Camshaft-spec")
    if folder_name_valid(new_folder_name,subfolders ):
        path = os.path.join(input_directory, new_folder_name)
        os.makedirs(path)
    else:
        print ("Couldn't create folder "+new_folder_name+ " .ID or complete name existing.")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
