AWS #4 Boto, S3
Due No Due Date  Points 3
Using Python and Boto this assignment will ask you to create a set of Python scripts to manage a simple S3 storage repository that stores and manages files on a per-user basis.

Remember: bucket names must be unique.

You will have one bucket to store user information: user-name, [password, email] that holds all users.

For each user you will have a bucket that the user can store files in.

NOTE: this assignment must use different buckets than are used in assignment 5.

00) To avoid possible character encoding issues place this line at the top of each Python file:

# -*- coding: utf-8 -*-



01) CreateUser.py will have these command line arguments:

user-name password email

for example, in a console/terminal:

python CreateUser.py MrCat NiceCat cats@cats.com

On first use , create the bucket you need to hold users in.

Create an object in the users bucket that stores an object as follows:
key=user-name
values=[password, user-email] (a list)

You must be able to handle the case where the user already exists. For example, if CreateUser/py is called for an existing user, update the password and email address in the S3 object that hold that user's information.


02) UploadFile.py will have these command line arguments:

user-name password file-key path-to-file-to-upload

user-name = the user-name from CreateUser.py
password = the user's password from CreateUser
file-key = is a tag/string that the user can associate with an uploaded file
path-to-file-to-upload = the path to a file on your machine to save in S3

The file-key and path-to-file-to-upload may have spaces

For example:

python UploadFile.py MrCat NiceCat My-Favorite-Dog-Picture .\dog1.jpg


You must handle typical errors like: user does not exist, bad password, cannot find file

03) ListFiles.py will have these command line arguments:

user-name password

For example: python ListFiles.py MtCat NiceCat

For each user file stored, this Python script prints one line to the console:

file-key

example:

a) So if you ran the CreateUser, followed by running the UploadFile.py script twice:

python CreateUser.py MyUserName MyPassword

python UploadFile.py MyUserName MyPassword CatPicture .\cat.png

python UploadFile.py MyUserName MyPassword DogPicture .\dog.png

b) Followed by a call to ListFiles:

python ListFiles.py MyUserName MyPassword

you will see this output:

CatPicture

DogPicture


NOTE: do not worry about formatting the console output. The columns for each file do NOT have to line up.

04) GetFile.py will have these command line arguments:

user-name password file-key path-to-save-file-to

For example:

python GetFile MrCat NiceCat 'Picture of my favorite dog' .\MyFavoriteDog

where MrCat is a user-name and NiceCat is the password from a previous running of the CreateUser.py script

05) DeleteFile.py will have there command line parameters:

user-name password file-key

For example:

python DeleteFile.py MrCat NiceCat Bird01

where MrCat is a user-name and NiceCat is the password from a previous running of the CreateUser.py script

