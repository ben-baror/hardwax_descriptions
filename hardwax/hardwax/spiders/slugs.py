import scrapy

class SlugsSpider(scrapy.Spider):
    name = "slugs"
    allowed_domains = ["hardwax.com"]
    start_urls = ["https://hardwax.com/section/labels.json"]

    def parse(self, response):
        data = response.json()

        # yield each ID individually
        for product_id in data["results"]:
            yield {"product_id": product_id}

        # follow pagination if next exists
        next_page = data.get("next")
        if next_page:
            next_page_url = "https://hardwax.com" + next_page
            yield response.follow(next_page_url, callback=self.parse)