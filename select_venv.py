"""<-------------------------------------------Venv Activation Program-------------------------------------------------------------->
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Created by: Alan Cyriac$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#Date: 10/09/2020$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
<----------------------------------------------Venv Activation Program-------------------------------------------------------------->
"""
# import libraries
import os

#  "activate_venv" is the function to activate particular virtual enviornment
def activate_venv(path, venvs, flag):
    # declare command variable
    command = ""
    # list all the virtual enviornment
    print("-" * 30)
    print("Index No. Virtual Enviornment")
    print("-" * 30)
    for count, venv in enumerate(venvs, start= 1):
        print( "  " + str(count) + "         " + venv )
    print("\n")
    # ask for index number of virtual enviornment
    index = int(input("Enter index number: ")) - 1
    #  Ckeck the user input to this condition
    if index > -1 and index <= (len(venvs) - 1):
        # append the specific value in the list to the path which is pre-defined
        command = 'cmd /k "E:\\pyworld\\venvworld\\{}\\Scripts\\activate.bat"'.format(venvs[index])
        # make flag as true
        flag = True
    # return three variables
    return command, index, flag

if __name__ == "__main__":
    # declare variable 'path' and assing path where the cluster of venvs are loacted
    path = "E:\\pyworld\\venvworld"
    # since each venvs have diferent folder name, collect all the folder names and insert it into variable 'venvs' as a list
    venvs = os.listdir( path )
    #  setflag as false
    flag = False
    # call "activate_venv" function
    command, index, flag = activate_venv(path, venvs, flag)
    # check the flag, 
    # if flag is true activate the virtual enviornment
    if flag == True:
        action = " '{}' virtual enviornment is activated now.".format(venvs[index])
        # activating virtual enviornment here
        os.system(command)
    # else do nothing
    else:
        action = "choose index from the listed virtual enviornments"
    # printing the action taken
    print( action )