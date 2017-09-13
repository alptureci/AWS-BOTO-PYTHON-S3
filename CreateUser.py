# -*- coding: utf-8 -*-
import sys
import boto
import random
import string

s3=boto.connect_s3()
region = 'us-west-1'

def createUser(username, password, email):
    print 'email: ' + username + '\npassword: ' + password + '\nemail: ' + email
    key = username
    value = [password, email]
    isNewUser(key, password, email)


def isNewUser(userkey, userpass, email):
    #s3=boto.connect_s3()
    #bucketlist=s3.get_all_buckets()
    #for o in bucketlist:
        #print o
    userbucket = 'alptureci-users-bucket'
    bucket = s3.get_bucket(userbucket)
    k = boto.s3.key.Key(bucket)
    k.key = userkey
    if k.exists():
        update_user(bucket, userkey, userpass, email)
    else:
        create_new_user(bucket, userkey, userpass, email)

def create_new_user(bucket, userkey, userpass, email):
    print 'createNewUser()'
    print 'create a new bucket for the user'
    newkey = bucket.new_key(userkey)
    newkey.set_contents_from_string(userpass+','+email)
    newkey.set_acl('public-read')
    create_bucket(userkey)

def update_user(bucket, userkey, userpass, email):
    print userkey + ' updated with password ' + userpass + ' and email: ' + email
    updatekey = bucket.get_key(userkey)
    updatekey.set_contents_from_string(userpass + ',' + email)

def create_bucket(bucketname):
    s3.create_bucket(bucketname+'-ucscext-alptureciaws', location=region)
    print bucketname+'-ucscext-alptureciaws bucket created successfully'


def random_generator(size=4,chars=string.ascii_uppercase+string.digits):
    return "".join(random.choice(chars) for x in range(size))



if __name__ == "__main__":
    if sys.argv.__len__() != 4:
        print 'error in supplied paramters please provide 3 in the order of (username pass email)'
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        email = sys.argv[3]
        createUser(username, password, email)