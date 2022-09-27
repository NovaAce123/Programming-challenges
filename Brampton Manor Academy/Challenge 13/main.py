import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"


def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def pos():
    html = scrape(url)
    i = 0
    x = 0

    while x < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)

        newstring = html[open_tr:close_tr]
        lookingfor = '"position">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</', pos_start)
        print(newstring[pos_start + len(lookingfor):pos_end])

        i = close_tr
        x += 1

def artist():
    html = scrape(url)
    i = 0
    x = 0

    while x < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)

        newstring = html[open_tr:close_tr]
        lookingfor = 'class="artist">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</a', pos_start)
        updatedString = newstring[pos_start + len(lookingfor):pos_end]
        y = updatedString.find('/">')
        refinedstring = updatedString[y+3:]
        print(refinedstring)

        i = close_tr
        x += 1

def title():
    html = scrape(url)
    i = 0
    x = 0

    while x < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)

        newstring = html[open_tr:close_tr]
        lookingfor = 'class="title">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</a', pos_start)
        updatedString = newstring[pos_start + len(lookingfor):pos_end]
        y = updatedString.find('/">')
        refinedstring = updatedString[y+3:]
        print(refinedstring)

        i = close_tr
        x += 1


def format():
    scrape(url)
    a = pos()
    b = artist()
    c = title()

    print(f"{a}{b:<30}{c}")

if __name__ == "__main__":
    format()