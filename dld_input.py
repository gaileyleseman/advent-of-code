import requests
import aoc_config as cfg

def download_input(year, day):
    session = requests.Session()
    session.get('https://adventofcode.com/')
    headers = {'session': cfg.aoc["session-cookie"]}
    url = "https://adventofcode.com/{0}/day/{1}/input".format(year, day)
    filename = "./input/day{0}_input.txt".format(day)
    page = requests.get(url, allow_redirects=True, cookies=headers)
    open(filename, 'w').write(page.text)

download_input(2020,8)



