import argparse

parser = argparse.ArgumentParser(description="Example Python CLI")

parser.add_argument("hacker_name", help="Enter Hacker Name", type=str)
parser.add_argument("hacker_power", help="Enter Hacker Power", type=str)

parser.add_argument("-bh", "--blackhat", default=False, action="store_true")
parser.add_argument("-wh", "--whitehat", default=True, action="store_false")

parser.add_argument("-ht", "--hackertype", choices=["white","black","gray"])

args = parser.parse_args()

print(args)

print(args.hacker_name)

