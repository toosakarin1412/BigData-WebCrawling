import scrapy


class OlxSpiderSpider(scrapy.Spider):
    name = "olx-spider"
    allowed_domains = ["www.olx.co.id"]
    start_urls = ["https://www.olx.co.id/mobil-bekas_c198"]

    def parse(self, response):
        items = response.xpath('//*[@id="main_content"]/div/div/section/div/div/div[5]/div[2]/div/div[2]/ul/li[*]')
        for item in items:
            harga = item.xpath('a/div[1]/div[2]/span/text()').get()
            tahun = item.xpath('a/div[1]/div[2]/div[1]/text()').get()
            nama = item.xpath('a/div[1]/div[2]/div[2]/text()').get()

            yield({
                'nama': nama,
                'harga': harga,
                'tahun': tahun
            })
        
