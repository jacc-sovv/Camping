# Rocky Mountain National Park Automatic Camping Availability
### Motivation
I got sick and tired of constantly checking RMNP for available campsites in the summer. They can be impossible to find, and if you don't reserve them months in advance, your only chance is to check availabilities after somebody cancels. I kept forgetting to check this, so I made a program to run nightly and e-mail me with any available campsites!

### How it works
This project scrapes available campsites form Rocky Mountain National Park. Once all availabilities are found, the program will either send an email to the user or output the results, depending on the status of the 'send_email' flag (see below).  
The main purpose of sending an email is to set up this program to automatically run using cron, Windows task scheduler, or a related program. Otherwise, you can manually run the program whenever you want to find an available campsite. The program checks for any available campsites throughout June, July, and August
To run, simply clone the repo and type python availability.py  


## Weekends Flag
If Weekends is set to True, it will only find available campsites on weekends (Fridays-Sundays).  
If Weekends is set to False, it will find all campsite availability on any day of the week.

## allow_group_sites Flag
allow_group_sites determines whether or not to include group sites in the results. By default, this is false. Group sites require 25+ people to reserve. 

## send_email Flag
Determines whether or not an email is sent. Default value of false. If send_email is false, program will instead print the available campsites. If send_email is true, you will have to ensure the other flags (see below) are set up appropriately.


## SERVER Flag
Determines what type of email server to connect to. Is set to gmail by default.  

## FROM
The email address you would like to send the availability update from. This will be the email you sign into. Can be a dummy email, a real email, up to you.  

## TO
The email address you would like to receive the updates at. Updates will be sent from FROM to TO.

