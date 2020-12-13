import requests
import aoc_config as cfg

def download_input(year, day):
    session = requests.Session()
    session.get('https://adventofcode.com/')
    headers = {'session': cfg.aoc["session-cookie"]}

    # TODO: fix trailing zeros in filenames but not in url
    url = "https://adventofcode.com/{0}/day/{1}/input".format(year, day)
    filename = "./input/day{0}_input.txt".format(day)
    page = requests.get(url, allow_redirects=True, cookies=headers)
    open(filename, 'w').write(page.text)

    # Create empty test input
    testfilename = "./input/day{0}_test.txt".format(day)
    open(testfilename, 'w')

    # Create starter Python File
    pyfilename = "day{0}.py".format(day)
    input = "# input = open('{0}', 'r').read().splitlines()".format(filename)
    testinput = "input = open('{0}', 'r').read().splitlines()".format(testfilename)
    pts = "# Part {0} ----------------------------------------------------------#"
    open(pyfilename, "w").write(input + "\n" + testinput + "\n\n" + pts.format(1) + "\n\n" + pts.format(2))

download_input(2020, 13)



