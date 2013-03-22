import urllib, re, pycolors

class hnx:
    def __init__(self):
        self.url = 'http://news.ycombinator.org/rss'
        self.color = pycolors.linux()
    def main(self):
        src = urllib.urlopen(self.url).read()
        items = re.findall(r"<item>(.*?)</item>", src)
        for x in items:
            title = ' '.join(re.findall(r"<title>(.*?)</title>", x))
            url = ' '.join(re.findall(r"<link>(.*?)</link>", x))
            print self.color.color(text=title, color='red', other='bold'), self.color.color(text='-', other='bold'), self.color.color(text=url, color='blue', other='bold')

        


hnx().main()
