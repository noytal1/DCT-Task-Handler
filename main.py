import argparse

from User import User
from UserDepartment import UserDepartment
from UserId import UserId
from UserName import UserName

parser = argparse.ArgumentParser(description="Execute a user's task")
parser.add_argument('--name', help="The user's name", nargs='+')
parser.add_argument('--dept', help="The user's department", nargs='+')
parser.add_argument('--id', help="The user's task id", nargs='+')
args = parser.parse_args()

if __name__ == '__main__':
    user = User(args.name, args.id, args.dept)
    user.create_user()
    # try:
    #     user_name = UserName(args.name)
    #     user_id = UserId(args.id)
    #     user_dept = UserDepartment(args.dept)
    #     if user_name.validate() and user_id.validate() and user_dept.validate():
    #         print("user name: {}, user id: {}, user dept: {}".format(user_id, user_name, user_dept))
    #     else:
    #         print('Too many wrong inputs. Program exits')
    # except Exception as e:
    #     print(f"{e} occurred")
