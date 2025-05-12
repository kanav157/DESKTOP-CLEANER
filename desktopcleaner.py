# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:26:58 2024

@author: kgarg
"""
import os 
import shutil


desktop_path = os.path.join(os.environ['USERPROFILE'], 'OneDrive\\Desktop')
destinationfolders = {
    "Images" : [".jpg",".jpeg",".png",".gif",".bmp",".svg",".tiff"],
    "Documents" : [".pdf",".docx",".doc",".txt",".xls",".xlsx",".ppt",".pptx"],
    "Videos" : [".mp4",".mkv",".avi",".mov",".wmv",".flv"],
    "Music" : [".mp3",".wav",".aac",".flac",".m4a"],
    "Archives" : [".zip",".rar",".tar",".gz",".7z"],
    "Programs" : [".exe",".msi",".py",".java",".sh",".c",".bat",".app",".apk"],
    "Others" : []
    }

def foldercreation():
    for f in destinationfolders.keys():
        f_path=os.path.join(desktop_path, f)
        try:

            if not os.path.exists(f_path):
                os.mkdir(f_path)
                print(f"Created folder : {f}")
        except Exception as e:
            print(f"Error creating folder {f} : {e}")


def fileorganizer():
    try:

        files = [file for file in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, file))]
    
        for f in files:
            path = os.path.join(desktop_path, f)
            extensions = os.path.splitext(f)[1].lower()
        
            moved = False
        
            for folder, ext in destinationfolders.items():
                if extensions in ext:
                    try:

                        shutil.move(path, os.path.join(desktop_path, folder ,f))
                        print(f"Moved: {f} -> {folder}")
                    except Exception as e:
                        print(f"Error moving {f} to {folder} : {e}")
                
                    moved = True
                    break
        
            if not moved:
                try:

                    shutil.move(path,os.path.join(desktop_path, "Others",f))
                    print(f"Moved : {f} -> Others")
                except Exception as e:
                    print(f"Error moving {f} to Others : {e}")
    except Exception as e:
        print(f"Error organizing files : {e}")         
        

if __name__ == "__main__":
    print("Desktop cleaner started ....")
    foldercreation()
    fileorganizer()
    print("Desktop Cleaner Finished !")
                