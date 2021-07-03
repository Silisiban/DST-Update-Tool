import os;
import shutil;
import zipfile;

#Path var that is what is changed when the game has updated.
updatePath = "C:/Program Files (x86)/Steam/steamapps/common/Don't Starve Together/data/databundles/scripts.zip";
removePath = "C:/Program Files (x86)/Steam/steamapps/common/Don't Starve Together/data";
renamePath = "C:/Program Files (x86)/Steam/steamapps/common/Don't Starve Together/data/databundles/scripts_backup.zip";
replacePath =  "C:/Program Files (x86)/Steam/steamapps/common/Don't Starve Together/data/scripts/prefabs/";
replaceFilesPath = "lua";
replaceFiles = ["birdcage.lua", "rocks.lua", "birds.lua", "veggies.lua"];

#Checks to see if the scripts file has been updated. before we do anything else.
def CheckIfUpdated():
    if (os.path.exists(updatePath)):
        return True;        
    else:
        print("The Game Has Not Been Updated.");
        return False;

#Deletes the old script folder from the lasttime it was updated.
def DeleteOldScriptFolder():
    try:
        if (os.path.exists(f"{removePath}/scripts")):            
            shutil.rmtree(f"{removePath}/scripts");   
            print("Scripts Folder was removed successfully.");     
        else:
            print("Scripts Folder Doesn't Exist Skipping step.");            
    except OSError as e:
        print(f"Error {removePath}/scripts : {e.strerror}.");

#Unzips the new scripts folder to the correct path so we can update the files and removes the the old zip file from the previous update.
def UnzipScriptsFolder():
    try:
        with zipfile.ZipFile(updatePath, 'r') as zip_ref:
            zip_ref.extractall(removePath);            
            print("Scripts Folder Has Successfully Been Extracted.");
            os.remove(renamePath);
            print("The old backup scripts have been removed successfully.");      
    except OSError as e:
        print(f"There Was An Error Unzipping the Directory: {e.strerror}.");

#Replaces the modified files for the custom gaming experience.
def ReplaceFiles():
    try:
        for file in replaceFiles:
            shutil.copy(os.path.join(replaceFilesPath,file),os.path.join(replacePath,file));                                  
            print(f"{file} Was Replaced Successfully.");
    except FileNotFoundError as e:
            print(f"Error Replacing File {e.strerror}.");

#Responsiple for calling all functions that are nessessary to do the update. Also Renames the Scripts.zip file so we dont update if we dont need to.
def DoUpdate():
    if(CheckIfUpdated()):
        DeleteOldScriptFolder();
        UnzipScriptsFolder();        
        os.rename(updatePath, renamePath);
        ReplaceFiles();
        print("Update Completed.");
    else:
        print("Update Failed.");

#Calls the main function that handles the update.
print("********************************");
DoUpdate();
print("********************************");