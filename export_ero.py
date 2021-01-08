

def _getText(div, xpath) :
    return div.find_element_by_xpath(xpath).text

def _getAttrText(div, xpath, attrName) :
    return div.find_element_by_xpath(xpath).get_attribute(attrName)

class Item :
    def __init__(self, div) :
        self.type   = _getText(div, './/span[@class="default3EHgn"]')
        self.url    = _getAttrText(div, './a', 'href')
        self.circle = _getText(div, './/p[@class="circleName209pI"]')
        self.title  = _getText(div, './/div[@class="productTitle3sdi8"]/p')
    
    def __repr__(self) :
        return "<Item type={}, url={}, circle={}, title={}>".format(self.type, self.url, self.circle, self.title)


class Date :
    def __init__(self, tup) :
        i, li = tup
        self.date = li.find_element_by_xpath('./p').text 
      
        divs = li.find_elements_by_xpath('./div[@class="localListProduct1pSCw"]')
        self.divs = [ Item(div) for div in divs ]

    def __repr__(self) :
        return "<Date {} / {}>".format(self.date, self.divs)

    def __str__(self) :
        return "{} / {}".format(self.date, self.divs)

def _isDateElement(tup) :
    i, li = tup
    try :
        li.find_element_by_xpath('./p')
        return True
    except :
        return False

def _toJson(dateList) :
    import json
    s = json.dumps(dateList, default=lambda o:o.__dict__, ensure_ascii=False)
    return s

def export(webDriver) :
    liList = webDriver.find_elements_by_xpath('//*[@class="purchasedListArea1Znew"]/ul/li')
    conv = [ Date(tup) for tup in enumerate(liList) if _isDateElement(tup) ]
    return _toJson(conv)


def toDict(j) :
    import json
    import collections
    obj = json.loads(j)
    ret = collections.defaultdict(list)

    for dateObj in obj :
        date = dateObj.get("date")
        for itemObj in dateObj.get('divs') :
            circle = itemObj.get("circle")
            url    = itemObj.get("url")
            title  = itemObj.get("title")
            type   = itemObj.get("type")
            ret[circle].append((date, title, type))

    return ret
