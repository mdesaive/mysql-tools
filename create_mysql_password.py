#!/usr/bin/python3

""" Compare two sets of mysql variables. """

# import sys
import pprint
import argparse
# import re
import hashlib
import textwrap


def prepare_arguments():
    """ Parse commandline arguments."""

    parser = argparse.ArgumentParser(
        prog='list_systemvms.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        Compare two lists of MySQL variable settings and printout differences.

        Autor: Melanie Desaive <m.desaive@mailbox.org>
        '''),
        epilog=textwrap.dedent('''\
        Examples:

        Compare two files
            ./create_mysql_password.py \
                --password plaintext password\
                --plugin MySQL authentication plugin \
        Additional Infos:
          Print a MySQL authentication string for the provided password and
          authentication plugin.

        Todo:

        '''))
    parser.add_argument(
        '--password',
        dest='password',
        help='Password to be hashed',
        required=True)

    parser.add_argument(
        '--plugin',
        dest='plugin',
        help='Authentication plugin to provide password hash for.',
        required=True)

    args = parser.parse_args()
    return args


def hash_for_mysql_native_password(password):
    """Creatae hash for plugin mysql_native_password."""

    # stage1 = hashlib.sha1(password)
    # stage2 = stage1.digest()
    # stage3 = hashlib.sha1(stage2)
    # stage4 = stage3.hexdigest()
    # stage5 = stage4.upper()
    # stage6 = "*" + stage5
    # python -c 'from hashlib import sha1; print "*" + sha1(sha1("right").digest()).hexdigest().upper()'

    stage1 = hashlib.sha1(password.encode('utf-8')).digest()
    password_hash = hashlib.sha1(stage1).hexdigest().upper()

    return "*" + password_hash


def main():
    """ main :) """
    args = prepare_arguments()

    if args.plugin == 'mysql_native_password':
        password_hash = hash_for_mysql_native_password(args.password)
    else:
        print('Allowed plugins: ["mysql_native_password", ]')

    print(password_hash)


if __name__ == "__main__":
    main()
