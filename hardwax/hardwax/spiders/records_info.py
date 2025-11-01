import scrapy
import json

class RecordsInfoSpider(scrapy.Spider):
    name = "records_info"
    allowed_domains = ["hardwax.com"]
    start_urls = ["https://hardwax.com"]

    def start_requests(self):
        # Step 1: load all product IDs from labels.json
        with open("slugs.json") as f:
            all_data = json.load(f)                             # load the whole JSON array
        all_ids = [item["product_id"] for item in all_data]

        # Step 2: loop through the IDs and create a request for each
        for pid in all_ids:
            url = f"https://hardwax.com/records.json?slugs={pid}"
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # Step 3: parse the JSON response for each product
        data = response.json()

        for item in data.get("results", []):
            result = item["result"]
            yield {
                "slug": result.get("slug"),
                "title": result.get("title"),
                "html": result.get("html"),
                "availability": result.get("availability", "")
            }
