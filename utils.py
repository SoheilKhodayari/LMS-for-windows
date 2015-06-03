__author__ = 'soheil'
import os

def isExtensionSupported(filename):
    """ Supported extensions viewable in SlideShow
    """
    if filename.endswith('PNG') or filename.endswith('png') or\
     filename.endswith('JPG') or filename.endswith('jpg'):
        return True

def imageFilePaths(paths):
    imagesWithPath = []

    try:
        dirContent = os.listdir(paths)
    except OSError:
        raise OSError("Provided path '%s' doesn't exists." % paths)

    for each in dirContent:
            selFile = os.path.join(paths, each)
            if os.path.isfile(selFile) and isExtensionSupported(selFile):
                imagesWithPath.append(selFile)
    return list(set(imagesWithPath))