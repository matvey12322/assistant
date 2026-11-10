import argparse
from app.client import call

parser = argparse.ArgumentParser()
parser.add_argument('input', help='Запрос')

args = parser.parse_args()

print(*call(args.input), sep="\n")

