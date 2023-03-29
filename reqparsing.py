class reqparsing:
    def __init__(self ,reqstring):
        self.lines=str(reqstring).splitlines()
        self.reqmethod=self.lines[0].split(' ')[0]
        self.requrl=self.lines[0].split(" ")[1]
        self.reqhost=self.lines[1].split(" ")[1]
    def reqmethods(self):
        return self.reqmethods
    def requrls(self):
        return self.requrl
    def reqhosts(self):
        return self.reqhost


