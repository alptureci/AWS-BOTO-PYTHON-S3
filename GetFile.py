# -*- coding: utf-8 -*-
import sys
import boto

user_bucket_extension = '-ucscext-alptureciaws'

def is_user_exists(username, password):
    s3 = boto.connect_s3()
    # first check is users exists
    users_bucket = 'alptureci-users-bucket'
    bucket = s3.get_bucket(users_bucket)
    k = boto.s3.key.Key(bucket)
    k.key = username
    if k.exists():
        # second check is password true
        obj = k.get_contents_as_string()
        value_list = obj.split(',')
        if password == value_list[0]:
            print 'password is true! go on'
            return True
        else:
            print 'wrong password'
            return False
    else:
        print 'User does not exit!'
        return False

# this need modification is fo the last parameter (pathtoSave-file) now I should emphasize it like: .\yosemite.jpg 
def get_file():
    s3 = boto.connect_s3()
    bucket = s3.get_bucket(username + user_bucket_extension)
    bucket_location = bucket.get_location()
    # this was necessary because otherwise for big data size i was taking
    # Connection reset by peer ERROR
    # solution from: https://github.com/boto/boto/issues/2207
    if bucket_location:
        conn = boto.s3.connect_to_region(bucket_location)
        bucket = conn.get_bucket(username + user_bucket_extension)
        key = bucket.get_key(fileKey)
        key.get_contents_to_filename(pathToSaveFile)


if __name__ == "__main__":
    if sys.argv.__len__() != 5:
        print 'error in supplied paramters please provide 4 in the order of (username pass file-key path-to-file-to-upload)'
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        fileKey = sys.argv[3]
        pathToSaveFile = sys.argv[4]

        if is_user_exists(username, password):
            get_file()
