def parse(self, response):
        # this helps to get all links from source code
        links = LxmlLinkExtractor(allow=()).extract_links(response)
 
        # Finallinks contains links url
        Finallinks = [str(link.url) for link in links]
 
        # links list for url that may have email ids
        links = []
 
        # filtering and storing only needed url in links list
        # pages that are about us and contact us are the ones that have email ids
        for link in Finallinks:
            if ('Contact' in link or 'contact' in link or 'About' in link or 'about' in link or 'CONTACT' in link or 'ABOUT' in link):
                links.append(link)
 
        # current page url also added because few sites have email ids on there main page
        links.append(str(response.url))
 
 
 
        # parse_link function is called for extracting email ids
        l = links[0]
        links.pop(0)
 
        # meta helps to transfer links list from parse to parse_link
        yield SeleniumRequest(
            url=l,
            wait_time=3,
            screenshot=True,
            callback=self.parse_link,
            dont_filter=True,
            meta={'links': links}
        )
