import os
import shutil
import time

def main():
deleted_folders_count=0
deleted_files_count=0
path='/PATH_TO_DELETE'
days=30
seconds=time.time()-(days*24*60*60)

if os.path.exists(path):
    for root_folder,files in os.walk(path):
        
        if seconds >= get_file_or_foler_age(root_folder):
            
            remove_folder(root_folder)
                          deleted)