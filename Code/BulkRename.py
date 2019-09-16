import os

#This function renames and moves all the files in the source folder to the destination folder

def BulkRename():

    #Number that increment to provider unique names
    NumberIncrement = 0;
    #Source directory containing files 
    SourcePath = 'C:\\Users\\USER\\Documents\\Code\\SourceFolder'
    #Destination directory to which the renamed files are moved
    DestinationPath = 'C:\\Users\\USER\\Documents\\Code\\DestinationFolder'
       
    FileObj = os.listdir(SourcePath)

    for file in FileObj:
        #Change the renamed fileName and its Extension here
        os.rename( os.path.join(SourcePath, file), os.path.join(DestinationPath, 'RenamedFileName'+str(NumberIncrement)+'.fileExtension'))
        NumberIncrement += 1

BulkRename()