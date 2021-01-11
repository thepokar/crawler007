from bs4 import BeautifulSoup
import urllib.request

logo = """

███████╗██╗     ██████╗  ██████╗ ██╗  ██╗███████╗██████╗  
██╔════╝██║     ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗
█████╗  ██║     ██████╔╝██║   ██║█████╔╝ █████╗  ██████╔╝
██╔══╝  ██║     ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
███████╗███████╗██║     ╚██████╔╝██║  ██╗███████╗██║  ██║╚
╚══════╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
                                                                                   

"""
print(logo)
print("My Channel : https://www.youtube.com/channel/UCkmU73jmY7TFUEYF0OGMQFQ")
print("My Github : https://github.com/thepokar")
print("\n")
links = []
urlw = input("Enter Your Url ===> ")
parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed

links.append(urlw)
xx = 0
for url in links:
    try:

        resp = urllib.request.urlopen(url)
        response = resp.read().decode(encoding="iso-8859-1")
        soup = BeautifulSoup(
            response, parser)
        for link in soup.find_all('a', href=True):
            link = link['href']
            if link[0] == "/":
                link = link[1:]
            if "http" not in link and "#" not in link and ";" not in link:
                final = urlw+link
                if final not in links:
                    print(final)
                    links.append(final)
                    xx += 1
            if "http" in link and urlw in link and "#" not in link and ";" not in link:
                if link not in links:
                    print(link)
                    links.append(link)
                    xx += 1
    except KeyboardInterrupt:
        print("\n")
        print("Bye !")
    except:
        pass
# all found links will save in "links" list you can make for loop enjoy!
