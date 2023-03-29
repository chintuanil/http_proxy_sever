import fileinput
class acessingfiles:
    def __init__(self):
        self.filename=""
    def acessfiles(self):
        f=open("blocked ip.html","r")
        req=f.read()
        return req
    def acessfile2(self):
        f=open("blocked websites.html" , "r")
        str1=f.read()
        return str1
    def acessfile3(self):
        f=open("blocked keywords.html","r")
        str3=f.read()
        return str3

