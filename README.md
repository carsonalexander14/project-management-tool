# Project Management Tool (Social Team Builder)

This project is the final Unit 12 project for the Python Web Development Team Treehouse Techdegree.

## Description

Users can sign up to find projects that need help or post their own projects for other people to join. Users create a brief profile for themselves after they sign up with an avatar, a bio, and pick their skills from a list. Users projects, too, giving it a title, description, and other details. They also list the positions they need filled for that job with a brief description of what the position will be responsible for. Users are able to find a project and ask to join it. If you're a project owner, you can approve or deny the person asking to join. Finally, users are able to login and logout of their account. 

## Features

•	As a user of the site, I should be able to sign up for an account.

•	As a user of the site, I should be able to log into my account.

•	As a user of the site, I should be able to edit my profile.

•	As a user of the site, I should be able to upload an avatar image for my profile.

•	As a user of the site, I should be able to pick my skills for my profile.

•	As a user of the site, I should be able to create a project that I need help on.

•	As a user of the site, I should be able to specify the positions my project needs help in with a name, a description, and related skill.

•	As a user of the site, I should be able to see all of the applicants for my project's positions.

•	As a user of the site, I should be able to approve an applicant for a position in my project.

•	As a user of the site, I should be able to reject an applicant for a position in my project.

•	As a user of the site, I should get a notification if I've been rejected or approved for a position.

•	As a user of the site, I should be able to search for projects based on words in their titles or descriptions.

•	As a user of the site, I should be able to filter projects by the positions they need filled.

•	As a user of the site, I should be able to apply for a position in a project.

•	As a user of the site, I should be able to log out.

## Getting Started

### Dependencies

* Install the requirements.txt file linked with the project build.
* Windows 10 or latest Mac OS version required.
* Python 3

### Installing

* Feel free to download the project locally with your own virtual env!
* Any modifications needed to be made to your local files/folders not to the GitHub repo.

### Executing program

Be sure to be rooted into the main PMT folder to create virtual enviroment. (cd "C:\project-management-tool-master\PMT")

* Step 1: Create and activate virtual enviroment

```
python3 -m venv env
```

```
.\env\Scripts\activate  
```

* Step 2: Install requirements.txt

```
pip install -r requirements.txt
```

* Note: PIP will need to install Pillow seperatly so use the following command.

```
pip install pillow
```

* Step 3: Rename the file in PMT/PMT/local_dist.py to:

```
local.py
```

* Step 4: Migrate the database

```
python manage.py migrate
```

* Step 5: Create admin account to login with 

```
python manage.py createsuperuser
```

* Step 6: Run server and enjoy!

```
python manage.py runserver
```

## Database setup

* You will need to be sure to setup skills for the platform. Be sure to go into the administrator with your superuser account and add whatever you would like. These skills are open to all users on the platform and is only able to be added by the administrator for a reason. We do not want the regular user to be able to add data that is shown across the board. 
```
127.0.0.1:8000/admin/accounts/skill/
```

## Help

Any advise for common problems or issues.
Please email `carson.alexander14@gmail.com`

## Authors

Contributors names and contact info

Carson Alexander - @carsonalexander14 (GH)

## Thank You Mentors

Keith Lewis - @Jacrys (GH)

Mark Ryan - @MarkRyan (GH)

Zen - @pythondebugger (GH)

Team Treehouse Staff & Others

## Version History

* 0.1
    * Initial Release
