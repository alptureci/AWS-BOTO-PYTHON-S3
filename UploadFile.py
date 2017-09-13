# -*- coding: utf-8 -*-
import sys
import boto

user_bucket_extension = '-ucscext-alptureciaws'

def isUserExists(username, password):
    s3 = boto.connect_s3()
    #first check is users exists
    usersbucket = 'alptureci-users-bucket'
    bucket = s3.get_bucket(usersbucket)
    k = boto.s3.key.Key(bucket)
    k.key = username
    if k.exists():
    #second check is password true
        obj = k.get_contents_as_string()
        valueList = obj.split(',')
        if password == valueList[0]:
            print 'password is true! go on'
            return True
        else:
            print 'wrong password'
            return False
    else:
        print 'User does not exit!'
        return False

def uploadFile():
    s3 = boto.connect_s3()
    bucket = s3.get_bucket(username + user_bucket_extension)
    bucket_location = bucket.get_location()
    # this was necessary because otherwise for big data size i was taking
    # Connection reset by peer ERROR
    # solution from: https://github.com/boto/boto/issues/2207
    if bucket_location:
        conn = boto.s3.connect_to_region(bucket_location)
        bucket = conn.get_bucket(username+'-ucscext-alptureciaws')
        newkey = bucket.new_key(fileKey)
        newkey.set_contents_from_filename(pathToFileToUpload, cb=percent_cb, num_cb=10)


def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

if __name__ == "__main__":
    if sys.argv.__len__() != 5:
        print 'error in supplied paramters please provide 4 in the order of (username pass file-key path-to-file-to-upload)'
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        fileKey = sys.argv[3]
        pathToFileToUpload = sys.argv[4]
        if isUserExists(username, password):
            uploadFile()


