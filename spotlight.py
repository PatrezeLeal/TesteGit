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
targetPath = os.environ['USERPROFILE']+r'\OneDrive\Pictures\\Backgrounds\\'

def create():
    try:
        os.chdir(spotlightPath)
        cwd = os.getcwd()
        logger.debug("Succesfully cd to "+cwd)
        listings = os.listdir(cwd)
    except:
        logger.error("Something wrong with specified directory. Exception- "+sys.exc_info())
    # This would print all the files and directories
    for file in listings:
        targetFile=targetPath+file+'.jpg'
        img = Image.open(file)
        #print(file + " " + str(img.width))
        if img.width==1920:
            #image is for desktop, continue processing
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
