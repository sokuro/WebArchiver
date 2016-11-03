import spiders

if __name__ == '__main__':
    url = 'http://www.sme.sk/'  # url from to crawl
    logfile = 'errlog.log'  # path to logfile
    oformat = 'xml'  # output format
    outputfile = 'sitemap.xml'  # path to output file
    crawl = spiders.Crawler(url=url, logfile=logfile, oformat=oformat, outputfile=outputfile)
    crawl.crawl(pool_size=20)