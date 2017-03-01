from urllib import urlretrieve

url = "https://somelink.com/somefile"
fileName = "file.zip"

def dlProgress(count, blockSize, totalSize):
    print "Percent %d " % int(count * blockSize * 100 / totalSize) 

urlretrieve(url, fileName, reporthook=dlProgress)

