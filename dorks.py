from googlesearch import search
import argparse
import time

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

parser = argparse.ArgumentParser(description='scraping vuln reports and writeups using google dorks ')
parser.add_argument('-m','--m',action='store_true', dest='medium', help='get writeups from medium')
parser.add_argument('-hone','--hone',action='store_true', dest='hackerone', help='get reports from hackerone')
parser.add_argument('-v',dest='vuln',help='specify the vulnerability type',required=True)
rp = parser.parse_args()
reports = []
def g_search(query):
    for report in search(query, stop=100):
        reports.append(report)
        print(f'{GREEN}{report}{END}')

def save_reports():
    with open('reports.txt', 'w+') as f:
        for report in reports:
            f.write(report)
            f.write('\n')


if __name__ == '__main__':
    h1 = 'hackerone.com'
    mm = 'medium.com'
    vuln = rp.vuln
    if rp.medium:
        dorks_medium = 'site:\''+mm+'\''+' '+vuln+' '+'writeup'
        print('\n{}Please Wait While we\'re quering list of writeups for you{}'.format(BLUE,END))
        print('---------------')
        time.sleep(2)
        g_search(dorks_medium)
        save_r = input('\nSave reports results in a file [Y]es/[N]o: ')
        if save_r.lower() == 'yes' or save_r.lower() == 'y':
            save_reports()
    if rp.hackerone:
        dorks_h1     = 'site:\''+h1+'\''+' '+vuln
        print('\n{}Please Wait While we\'re quering list of reports for you{}'.format(BLUE,END))
        print('---------------')
        time.sleep(2)
        g_search(dorks_h1)
        save_r = input('\nSave reports results in a file [Y]es/[N]o: ')
        if save_r.lower() == 'yes' or save_r.lower() == 'y':
            save_reports()





