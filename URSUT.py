import requests
import pyshorteners
import sys


class name_ban:
    
    def banner(self)
         pass
    
    def help(self):
       
       
    
       print('URSIT V1.0')
       about = '''Have you ever wondered: Where does this link go? 
       The uslit it allows you to see the complete path a redirected URL goes through. 
       It will show you the full redirection path of URLs, shortened links, or tiny URLs.
       or URL Shortner is used to shorten a URL'''
       print(about)
       print('\nRequirements: Python 3, requests and colorama libraries')
       print('To install the requirements run these commands')
       print('\tUpdate: apt-get update')
       print('\tPython 3: apt-get install python3')
       print('\tRequests: pip install requests')
       print('\tcolorama: pip install colorama')
       print('\nRun the tool: uslit.py --track')
       print('Commands')
       print("--track or -t  -> Track the given URL's redirection path & find its end URL.")
       print("--shortner or -s -> To give the shorten for a link")
       print('--help or -h  -> To display helpline how to use this tool & about tool. ')
       print(Fore.GREEN + "developed by SURYA")
       print(Fore.YELLOW + "contact me through insta @ i_am_surya28")

    def cmdusage(self):
        print('Invalid command-line arguments!')
        print('Commands')
        print("--track or -t  -> Track the given URL's redirection path & find its end URL.")
        print("-shortner or - s -> To give shorten form of a link")
        print('--help or -h  -> To display helpline how to use this tool & about tool. ')

class ursut:
    def __init__(self, url):
        self.url = url

    def shortner(self):
        try:
            surl = pyshorteners.Shortener().tinyurl.short(self.url) 
            print(f"shorted url: {surl}")
        except Exception as q:
            print('Tracking Failed! Check URL')
            print("Invalid url ")
            print(q)
            exit()

    def track_url(self):
        try:
            resp = requests.get(self.url)
            if resp.history: 
                print(Fore.RED + ' \nYes URL is Redirected or Shorten!' )
                print(Fore.RED + ' Here the following redirected chain...\n ' )
                for r in resp.history:
                    print(Fore.RED + ' | ', r.status_code, '|', r.url, '|', r.reason)
                print(Fore.WHITE + '\nEND URL :', resp.url)
                print(Fore.WHITE +  'Status Code :', resp.status_code, resp.reason)
            else:
                print(Fore.WHITE + ' \nURL is Not Redirected or Shorten!')
                print(Fore.WHITE + ' END URL :', resp.url)
                print(Fore.WHITE + ' Status Code :' , resp.status_code, resp.reason)

        except BaseException as be:
            print(Fore.RED + 'Tracking Failed! Check URL')
            print(be)
            exit()
       

if __name__=='__main__':
    intro = name_ban()
    intro.banner()
    if len(sys.argv) == 2:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            intro.help()
        elif sys.argv[1] == '--track' or sys.argv[1] == '-t':
            url = input('Enter URL to Track:')
            print('Tracking Redirection Of URL...')
            track = ursut(url)
            track.track_url()
        elif sys.argv[1]== "--shortner" or sys.argv[1]=="-s":
            url = input('Enter URL to short:')
            short = ursut(url)
            short.shortner()
        else:
            intro.cmdusage()
    else:
        intro.cmdusage()
