from newspaper import Article

def getNews(url):
    """
    Get paragrah form news
    :param url : url of news online
    :return : sentence of news online
    """
    article = Article(url)
    article.download()
    article.html
    article.parse()
    news = article.text
    return(news)

# url = 'https://www.cnnindonesia.com/nasional/20200220212302-20-476621/aksi-212-besok-polisi-alihkan-arus-di-tujuh-ruas-jalan'
# url = 'https://bola.kompas.com/read/2020/02/20/22300008/pemain-timnas-indonesia-tengah-berjuang-untuk-pulih-pasca-operasi'
url = 'https://www.cnnindonesia.com/gaya-hidup/20200224123114-255-477472/vaksin-remdesivir-cikal-bakal-antivirus-corona'
# print(getNews(url))

# print('get_url')
# article = Article(url)
# article.download()
# print('downloded')
# print(article.html)
# html = article.html
# print(article.parse())
# print(article.authors)
# print(article.text)
