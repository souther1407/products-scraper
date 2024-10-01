from playwright.sync_api import sync_playwright


class SeleniumRequest:
    def request(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            content = page.content()
            browser.close()
            return content
