import argparse
from operator import attrgetter


class CustomArgParse:
    """
    Use this class if you want to set a bool value for an argument to True just specified the argument after the script in the command-line.
    Default value for arguments is False.


    Example of an input dictionary
    args_dict1 = {'arg1': ['a1', ' Argument 1 Description'],
                    'arg2': ['a2', 'Argument 2 Description'],
                     'arg3': ['a3', 'Argument 3 Description']}
    Command Line Example
    python test1.py --arg1
    python test1.py -a1
    Output from get_args method
    {'arg1': True, 'arg2': False, 'arg3': False}

    """

    def __init__(self, args_dict):
        self.args_dict = args_dict
        self._parser = argparse.ArgumentParser(description='----------------> Execution Instructions <----------------',
                                              epilog='-------------> End of the Execution Instructions <-------------')
        for full_arg, (abbr_arg, info_arg) in args_dict.items():
            self._parser.add_argument('-{abbr_arg}'.format(abbr_arg=abbr_arg), '--{full_arg}'.format(full_arg=full_arg),
                                     help='{info_arg}'.format(info_arg=info_arg), action='store_true', default=False)
        self._args = self._parser.parse_args()

    def get_args(self):
        """
        Return a dictionary where the key is the name of an argument and dict value is the value provided.
        The dictionary has elements of type string
        """
        d1 = {}
        for arg in self.args_dict.keys():
            prop_arg = attrgetter(arg)
            d1[arg] = prop_arg(self._args)
        return d1


class CustomArgParseValue:
    """
    Use this class if you want to insert arguments from the command-line.
    Default value for arguments is False.

    Example of an input dictionary
    args_dict1 = {'arg1': ['a1', ' Argument 1 Description'],
                    'arg2': ['a2', 'Argument 2 Description'],
                     'arg3': ['a3', 'Argument 3 Description']}

    Command Line Example
    python test2.py --arg1 "test"
    python test2.py -a1 "test"
    Output from get_args method
    {'arg1': "test", 'arg2': False, 'arg3': False}
    """

    def __init__(self, args_dict):
        self.args_dict = args_dict
        self._parser = argparse.ArgumentParser(description='----------------> Execution Instructions <----------------',
                                              epilog='-------------> End of the Execution Instructions <-------------')
        for full_arg, (abbr_arg, info_arg) in args_dict.items():
            self._parser.add_argument('-{abbr_arg}'.format(abbr_arg=abbr_arg), '--{full_arg}'.format(full_arg=full_arg),
                                      help='{info_arg}'.format(info_arg=info_arg), default=False)
        self._args = self._parser.parse_args()

    def get_args(self):
        """
        Return a dictionary where the key is the name of the argument and dict value is the value provided.
        The dictionary has elements of type string
        """
        d1 = {}
        for arg in self.args_dict.keys():
            prop_arg = attrgetter(arg)
            d1[arg] = prop_arg(self._args)
        return d1



if __name__ == "__main__":
    raise SyntaxError("This is a module and must be imported!")

