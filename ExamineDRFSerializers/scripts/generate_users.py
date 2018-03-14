#!/usr/bin/python

__author__ = 'lawrencealan+github@gmail.com'

"""

Generates random users, profiles and game entries for testing.

"""

import string
import datetime
import os
import sys
import random

# django environment initialization - replace MYAPP w/ your application identifier

if __name__ == "__main__":
    sys.path.append('../ExamineDRFSerializers/')
    print(sys.path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()
from django.contrib.auth.models import User


def get_random_string(length, stringset=string.ascii_letters):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def generate_users(n):
    print("Generating %s user(s)..." % n)

    for user_index in range(n+1):
        # create user
        new_user = User.objects.create(
            username=get_random_string(16),
            email=get_random_string(16) + '@' + get_random_string(16) + '.com',
        )
        new_user.save()

def main(argv):
    if argv.__len__() < 2:
        print("Usage: %s <count>" % argv[0])
        sys.exit(1)
    if not argv[1].isdigit():
        print("Invalid argument: ""%s"" " % argv[1])
        print("Usage: %s <count>" % argv[0])
        sys.exit(1)
    generate_users(int(argv[1]))


if __name__ == "__main__":
    main(sys.argv[0:])
