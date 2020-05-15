import sys
import os
from shutil import copyfile
import logging
from PIL import Image, ExifTags

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#create file handler and set level 
#I store the spotlight.log file in your User folder. If you want to change this, update the path on the next line.
fh = logging.FileHandler(os.environ['USERPROFILE']+r'\spotlight.log')

#create formattter
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

#add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

#add ch to logger
#logger.addHandler(ch)
logger.addHandler(fh)


spotlightPath = os.environ['LocalAppData']+r'\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
#change the targetPath for where you want to save the images fetched from Windows Spotlight. I put these in my OneDrive\Pictures folder.
#I've created a subfolder called Backgrounds. I use OneDrive because I sync OneDrive across multiple computers and so that the images 
#automatically appear on all my PCs
targetPath = os.environ['USERPROFILE']+r'\OneDrive\Pictures\\Backgrounds\\'

def create():
    try:
        os.chdir(spotlightPath)
        cwd = os.getcwd()
        logger.debug("Succesfully cd to "+cwd)
        listings = os.listdir(cwd)
    except:
        logger.error("Something wrong with specified directory. Exception- "+sys.exc_info())
    # For each file found in listings.
    for file in listings:
        #prepare the target file name. We basically add the .jpg extension
        targetFile=targetPath+file+'.jpg'
        #use the Pillow image module. We need to know the width.
        img = Image.open(file)
        #print(file + " " + str(img.width))
        #Checking the width of 1920. The Spotlight feature stores images for Desktop and Mobile. We only want the Desktop images.
        if img.width==1920:
            #image is for desktop, continue processing
            #check if the File has already been copied to the target. We don't want to re-copy. This is useful if you set this 
            #script up as a Windows Scheduled Task. If this runs every day or before Spotlight images are updated, then we don't
            #unncessarily copy the images again.
            if not os.path.exists(targetFile):
                try:
                    copyfile(file,targetFile)
                except IOError as e:
                    logger.error("Unable to copy file. %s"+e)
                    exit(1)
                except:
                    logger.error("Unexpected Error:"+sys.exc_info())
                logger.debug("copied "+targetFile)
            else:
                logger.debug("File Exists - copy not performed, skipping " + file)
        else:
            logger.debug("File is not meant for desktop, skipping " + file)

if __name__=="__main__":
    create()
