"""Module for greeting a user."""

def greet(options):
    """Greet a user."""
    print("Hello, {}!".format(options.username))

def create_parser(subparsers):
    """Create an argument parser for the "greet" command."""
    parser = subparsers.add_parser("greet")
    parser.set_defaults(command=greet)
    # Add a required parameter to specify the user to greet
    parser.add_argument("-u", "--username", required=True, help="The user to greet")
