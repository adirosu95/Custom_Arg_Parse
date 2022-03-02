import sys
import os
from CustomArgParse import CustomArgParse


def main():
    args_dict1 = {'arg1': ['a1', ' Argument 1 Description'],
                  'arg2': ['a2', 'Argument 2 Description'],
                  'arg3': ['a3', 'Argument 3 Description']}
    custom_arg_parse = CustomArgParse(args_dict1)
    print( custom_arg_parse.get_args())


if __name__ == "__main__":
    sys.exit(main())
