from User import User
import ArgsHandler
from Logger import logger

if __name__ == '__main__':
    """ Main function to execute a DCT task """
    try:
        logger.info("Receiving flags from user")
        args = ArgsHandler.parse_args()  # define all flags needed
        user = User(args.name, args.id, args.dept)  # create a user to execute a task
        user.create_user()
    except Exception as e:
        print(e)
        logger.info("got Exception {}".format(e))
