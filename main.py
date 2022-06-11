import argparse

from User import User

parser = argparse.ArgumentParser(description="Execute a user's task")
parser.add_argument('--name', help="The user's name", nargs='+')
parser.add_argument('--dept', help="The user's department", nargs='+')
parser.add_argument('--id', help="The user's task id", nargs='+')
args = parser.parse_args()

if __name__ == '__main__':
    try:
        user = User(args.name, args.id, args.dept)
        user.create_user()
    except Exception as e:
        print(e)
