# CovidVaccineSlotFinder

These scripts help you find a vaccine slot in a desired districts for a given age range.


# cowinAuto.py

This script is used to automatically check vaccine slots avilability and send mail at specified times without any manual intervention

Following changes must be made before running the script - 

FROM_USER - Enter the Email id from which you want to send the email 
PASSWORD - Enter the password for the email id you entered in FROM_USER
TO_USER - Enter the Email id to which you want to send the email 
DIST_ID =  Enter the district id for which you want to check slots (you may use stateDistrictDetails.py script to get distict id and name)
DIST_NAME= Enter the district id for which you want to check slots (you may use stateDistrictDetails.py script to get distict id and name)
MIN_AGE - Enter the minimum age to 18 or 45 for the vaccine availability 


After making these chnages create a bat file from this script --> Follow these step to create a bat file from .py file https://datatofish.com/batch-python-script/
Once you have your batfile ready you can schedule this script using Task schedluer in windows or with other alternative options in Mac and Linux.
To schedule a python script run at specified time follow the instructions here --- https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279


# stateDistrictDetails.py 

This script is used to display the state along with the state id and districts along with the disctrict id of the selected state. 
On running the command stateDistrictDetails.py , you will be prompted to key in the state id of the state of your choice after which you can view the districts along with the district id 


# vaccineSlot.py

This scrpit is used to display the information about the available vaccine slots for the next 7 days in the district of your choice.
On running the command vaccineSlot.py , you will be prompted to key in the state id of the state of your choice after which you can key in the district id from the displayed list of districts and their correspoding disctrict ids.Once the details are keyed in , the available vaccine slots will be displayed. In case of non-availablity , a message will be displayed saying that no vaccines slots are available.

# vaccineSlotMail.py

This script is used to send an email about the vaccine slots .

Following changes must be made before running the script - 

FROM_USER - Enter the Email id from which you want to send the email 
PASSWORD - Enter the password for the email id you entered in FROM_USER
TO_USER - Enter the Email id to which you want to send the email 
MIN_AGE - Enter the minimum age to 18 or 45 for the vaccine availability 

Once the above changes are made , run the script , you will be prompted to key in the state id of the state of your choice after which you can key in the district id from the displayed list of districts and their correspoding disctrict ids.Once the details are keyed in , the available vaccine slots will be mailed. In case of non-availablity , a message will be sent saying that no vaccines slots are available.
