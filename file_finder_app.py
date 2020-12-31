################## File Finder ##################
# File are sorted and save in extension wise folder
# This is a simple file finder app which separates file in path 
# extension wise and save in same extension type of folder.

import os, shutil

#audio_extensions = ('.mp3','.m4a','.wav','.flac','.aif','.wma')
#video_extensions = ('.mp4','.mkv','.flv','.mpeg')
#document_extensions = ('.doc','.pdf','.txt','.csv')
dict_extensions = {
    'audio_extensions' : ('.mp3','.m4a','.wav','.flac','.aif','.wma'),
    'video_extensions' : ('.mp4','.mkv','.flv','.mpeg','.webm'),
    'document_extensions' : ('.doc','.pdf','.txt','.csv'),
    'image_extensions' : ('.jpg','.jpeg','.png','.tif'),
}


folderpath = input('Enter folder path : ')

def file_finder(folder_path, file_extensions):
    files = []
    
    for file in os.listdir(folder_path):
        path, ext = os.path.splitext(file)
        if ext.isupper():
            os.rename(file, path + ext.lower())
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
            
    return files

# print(file_finder(folderpath, document_extensions))

for extension_type, extension_tuple in dict_extensions.items():
    for f in os.listdir(folderpath):
        path1,ext1 = os.path.splitext(f)
        #print(ext1)
        
        if ext1 in extension_tuple:    
            folder_name = extension_type.split('_')[0]+'_Files'
            folder_path = os.path.join(folderpath, folder_name)
            if os.path.exists(folder_path):
                for item in file_finder(folderpath,extension_tuple):
                    item_path = os.path.join(folderpath,item)
                    item_new_path = os.path.join(folder_path,item)
                    shutil.move(item_path,item_new_path)
            else:
                os.mkdir(folder_path)
                for item in file_finder(folderpath,extension_tuple):
                    item_path = os.path.join(folderpath,item)
                    item_new_path = os.path.join(folder_path,item)
                    shutil.move(item_path,item_new_path)
            
    
    #print('Calling file finder')
    #print(file_finder(folderpath,extension_tuple))  
