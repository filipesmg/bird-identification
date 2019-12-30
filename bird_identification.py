###############################################################################
# Routine to show image, ask a question. Accordinng to the answer, perform an action
# @author Filipe Guimaraes
# @date 17.02.2019
################################################################################
import numpy as np                            # Numerical library
import os
import sys                                    # System library (to read arguments from command line)
import glob                                   # Unix style pathname pattern expansion
import cv2 as cv
import shutil

question = "Is this a bird?"
frst_folder = "bird/"
scnd_folder = "nobird/"

################################################################################
# How to use the script
################################################################################
def usage():
   """ Prints usage info and exists. """
   print("Files required. Use:")
   print("ipython bird_identification.py folder")
   print("where 'folder' is the path containing the image files.")
   print("Keystrokes:")
   print("y - Answer yes. Copy to first folder.")
   print("n - Answer no. Copy to second folder.")
   print("ESC - Stop program.")
   print("Any other key skip current image.")
   sys.exit()

################################################################################
# Get all files in the input path(s)
################################################################################
def get_filenames(path):
  # glob return a list with all the files listed by path
  files = glob.glob(path+'*')
  return files


################################################################################
# Main program
################################################################################
if __name__ == "__main__":
  # Check if folder is given
  if(len(sys.argv) < 2):
    usage()

  filenames = get_filenames(sys.argv[1])

  for filename in filenames:
    # print(filename, os.path.basename(filename))
    img = cv.imread(filename)
    ims = cv.resize(img, (960, 540))
    # print(img.shape, img.max(), img.min())
    cv.imshow(question,ims)
    key = cv.waitKey(0)
    if key==27:    # Esc key to stop
        cv.destroyAllWindows()
        break
    elif key == ord('y'): # not a bird
        cv.destroyAllWindows()
        print("Yes. Copying to "+frst_folder+os.path.basename(filename)) # else print its value
        shutil.move(filename, frst_folder+os.path.basename(filename))
        continue
    elif key == ord('n'): # not a bird
        cv.destroyAllWindows()
        print("No. Copying to "+scnd_folder+os.path.basename(filename)) # else print its value
        shutil.move(filename, scnd_folder+os.path.basename(filename))
        continue
    else:
        cv.destroyAllWindows()
        print(chr(key)+" pressed. Skipping image.")
        continue
    sys.exit(0)
