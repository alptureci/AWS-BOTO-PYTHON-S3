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

def list_files():
    print 'printing file for ' + username
    s3 = boto.connect_s3()
    bucket = s3.get_bucket(username + user_bucket_extension)
    keys = bucket.get_all_keys()
    print '/*******'
    for k in keys:
        print k.key
    print '/*******'


if __name__ == "__main__":
    if sys.argv.__len__() != 3:
        print 'error in supplied paramters please provide 2 in the order of (username pass)'
    else:
        username = sys.argv[1]
        password = sys.argv[2]

        if is_user_exists(username, password):
            list_files()
