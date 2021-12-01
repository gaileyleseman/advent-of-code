import argparse
import requests
import os
import cookie_jar


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', '-y', help="enter the event year", type=str, default='2021')
    parser.add_argument('--day', '-d', help="enter the event day", type=str)
    parser.add_argument('--redo', '-r', help="set to True to download the input again", type=bool, default=False)
    parser.add_argument('-language', '-l', help="set the boilerplate language", type=str, default='python')
    args = parser.parse_args()

    session = requests.Session()
    cookies = {'session': cookie_jar.aoc}

    path = "./{0}/day{1}/".format(args.year, args.day.zfill(2))
    if not os.path.exists(path):  # create folder for the day
        os.makedirs(path)

    input_path = path + "input.txt"
    if not os.path.isfile(input_path) or args.redo:  # request input and create txt file
        url = "https://adventofcode.com/{0}/day/{1}/input".format(args.year, args.day)
        try:
            page = session.get(url, allow_redirects=True, cookies=cookies)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        with open(input_path, 'w') as f:
            f.write(page.text.rstrip())

    solution_path = path + "day{0}.py".format(args.day.zfill(2))
    boilerplate_path = "boilerplate/{0}_boilerplate.py".format(args.language)

    if not os.path.isfile(solution_path):  # create a boilerplate
        with open(boilerplate_path, 'r') as boilerplate, open(solution_path, 'a') as solution:
            for line in boilerplate:
                solution.write(line)

    with open(path + "test.txt", 'a'):  # create empty txt file for test input
        pass

    print("Ready for 'Advent of Code | {0} | Day {1}'!".format(args.year, args.day))


if __name__ == '__main__':
    main()
