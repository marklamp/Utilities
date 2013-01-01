"""
(c) 2012 Provider Data Services, LLC
This source code is released under the New BSD license.  Please see
http://www.providerdataservices.com/BSDLicense.html for license details.

"""

import os
import fnmatch
import sys
from bs4 import BeautifulSoup

def find_files(dir, pattern="*.*",hidden=False, relative=False, ):
        ''' (str,str,bool,bool)-> lst

        Returns a list of the files in a given folder (non-recursive)
        hidden is a boolen flag to include / exclude hiddent files
        relative is a boolen flag to return full or relative path names

        >>> lst = get_file_list(dirname)
        '''

        filelist = []

        # Loop over all files in a directory
        for nm in os.listdir(dir):

            # Hidden files start with '.'
            # Ignore them unless requested 
            if not hidden and nm.startswith('.'):
                continue

            # Check the extension
            if fnmatch.fnmatch(nm,pattern):

                # If relative paths are requested, include the directory path
                if not relative:
                    nm = os.path.join(dir, nm)

                # Add the file to the list
                filelist.append(nm)
                    

        # Sort the list and then return it
        filelist.sort()
        return filelist

def replace_tag(s_filename, s_tag, s_replace, s_fileout=None):
        ''' (str,str,str,str)-> updated file

        Opens a file and finds all occurances of the string 's_find'
        and replaces each occurance with the string 's_replace'

        >>> replace_string(myfile.html,"s1", "s2")
        '''
        file_handle = open(s_filename, 'r')
        soup = BeautifulSoup(file_handle.read())
        file_handle.close()
        print(soup.prettify())

def replace_string(s_filename, s_find, s_replace, s_fileout=None):
        ''' (str,str,str,str)-> updated file

        Opens a file and finds all occurances of the string 's_find'
        and replaces each occurance with the string 's_replace'

        >>> replace_string(myfile.html,"s1", "s2")
        '''

        # Read contents from file as a single string
        try:
                
                file_handle = open(s_filename, 'r')
                file_string = file_handle.read()
                file_handle.close()

                if ( file_string.find(s_find) > 0):
                        
                        file_string = file_string.replace(s_find, s_replace, 1)
                        if (s_fileout == None):
                                file_handle = open(s_filename, 'w')
                        else:
                                file_handle = open(s_fileout, 'w')
                        file_handle.write(file_string)
                        file_handle.close()
                        status = "OK"
                else:
                        status = "Find string not found"
 
        except:
                # Cannot find the string, do nothing
                status = "Exception: ", file_string

        return status
