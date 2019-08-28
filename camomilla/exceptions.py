class NeedARedirect(Exception):
    def __init__(self, redirect_url):
        self.redirect_url = redirect_url
