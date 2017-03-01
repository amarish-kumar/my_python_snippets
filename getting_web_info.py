import urllib2, urllib

def download_progress(count, block_size, total_size):
    print "Percent downloaded: %d " % int(count * blockSize * 100 / totalSize)

try:
    params = urllib.urlencode({
        "user": "jonh",
        "password": "passW0rd!" 
    })
    # POST
    f = urllib2.urlopen("http://www.pyhton.org/", params)
    # GET
    f2 = urllib2.urlopen("http://www.pyhton.org/" + "?" + params)
    # DOWNLOAD
    f3 = urllib.urlretrieve("http://www.pyhton.org/file.zip","file.zip",reporthook=download_progress)

    # Using Request
    ua = "Mozilla/5.0 (compatible; Konqueror/3.5.8; Linux)"
    h = {"User-Agent": ua} 
    r = urllib2.Request("http://www.python.org", headers=h) 
    f4 = urllib2.urlopen(r) 

    print f.read()
    f.close()
    f2.close()
    f3.close()
    f4.close()
except HTTPError as e:
    print "ERROR: ", e.code
except URLError as e:
    print "ERROR: ", e.reason