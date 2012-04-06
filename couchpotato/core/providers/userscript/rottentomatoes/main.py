from BeautifulSoup import BeautifulSoup
from couchpotato.core.event import fireEvent
from couchpotato.core.providers.userscript.base import UserscriptBase

class RottenTomatoes(UserscriptBase):

    includes = ['http*://www.rottentomatoes.com/m/*']

    def getMovie(self, url):

        try:
            data = self.urlopen(url)
        except:
            return

        html = BeautifulSoup(data)
        title = html.find('span', {'itemprop':'name'}).text
        info = fireEvent('scanner.name_year', title, single = True)
        return self.search(info['name'], info['year'])