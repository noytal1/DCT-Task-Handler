
import argparse

def parse_args():
    """
    function to define all flags needed and parse them
    """
    parser = argparse.ArgumentParser(description="Execute a user's task")
    parser.add_argument('--name', help="The user's name", nargs='+')
    parser.add_argument('--dept', help="The user's department", nargs='+')
    parser.add_argument('--id', help="The user's task id", nargs='+')
    return parser.parse_args()


