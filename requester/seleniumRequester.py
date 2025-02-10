from playwright.sync_api import sync_playwright


class SeleniumRequest:
    def request(self, url):
        with sync_playwright() as p:
            browser = p.firefox.launch()
            page = browser.new_page()
            page.set_default_navigation_timeout(200000000)
            page.goto(url, wait_until="networkidle")
            content = page.content()
            return content
