from User import User
import ArgsHandler
import logging
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y, %H-%M-%S")
print("date and time =", dt_string)

logging.basicConfig(level=logging.INFO, filename='destination/logs/{}.log'.format(dt_string), filemode='w',
                    format='%(asctime)s :: %(levelname)s :: %(message)s')

if __name__ == '__main__':
    """ Main function to execute a DCT task """
    try:
        logging.info("creating a user")
        args = ArgsHandler.parse_args()  # define all flags needed
        user = User(args.name, args.id, args.dept)  # create a user to execute a task
        user.create_user()
    except Exception as e:
        print(e)
