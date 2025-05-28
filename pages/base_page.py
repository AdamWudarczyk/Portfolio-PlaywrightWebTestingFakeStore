class BasePage:
    def __init__(self, page):
        self.page = page

    def go_to(self, url: str):
        self.page.goto(url)