
import sys
sys.path.append('C:\Users\Mark\Development\Python\Libraries')
import PDS_FileManager as fm

foldername = 'C:\\Users\\Mark\\Development\\pdsweb - Copy\\site\\'
findtextfile = 'C:\\Users\\Mark\\Development\\pdsweb - Copy\\findtext.html'
replacetextfile = 'C:\\Users\\Mark\\Development\\pdsweb - Copy\\replacetext.html'

filelist = fm.find_files(foldername,"*.html",False,True)

# read the find text
file_handle = open(findtextfile, 'r')
s_find = file_handle.read()
file_handle.close()

# read the replace text
file_handle = open(replacetextfile, 'r')
s_replace = file_handle.read()
file_handle.close()

for filename in filelist:
    try:
        filein = foldername + filename
#        fm.replace_tag(filein, s_find, s_replace)
        status = fm.replace_string(filein, s_find, s_replace)
        print "Updating: ", filein, ":", status

    except:
        print "Could not update: ", filein

        
    


