# -*- coding: utf-8 -*-
import scrapy


class AmazonproductSpider(scrapy.Spider):
    name = 'AmazonProduct'
    allowed_domains = ['amazon.co.jp']

    # ドラッグストアカテゴリの「ホエイプロテイン」のキーワードで設定
    start_urls = ['https://www.amazon.co.jp/s?k=%E3%83%9B%E3%82%A8%E3%82%A4%E3%83%97%E3%83%AD%E3%83%86%E3%82%A4%E3%83%B3&i=hpc&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss']

    def parse(self, response):
        for sel in response.xpath('//div[@class="s-item-container"]'):

            #タイトルに含まれている文字列を指定
            title_str = sel.xpath('div[@class="a-row a-spacing-none"]/div[@class="a-row a-spacing-mini"]/a[@class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/@title').extract_first()

            if 'iPhone' in title_str:

                #データ取得時間を設定
                now = dt.now(timezone('Asia/Tokyo'))
                date = now.strftime('%Y-%m-%d')
                jst_time = now.strftime('%Y-%m-%dT%H-%M-%S')

                product = MyproductsItem()

                #タイトル
                product['title'] = sel.xpath('div[@class="a-row a-spacing-none"]/div[@class="a-row a-spacing-mini"]/a[@class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/@title').extract_first()
                #サームネイル
                product['thumbnail'] = sel.xpath('div[@class="a-row a-spacing-base"]/div/a/img/@src').extract_first()
                #キーワード
                product['keyword'] = response.xpath('//input[@id="twotabsearchtextbox"]/@value').extract_first()
                #リンク
                product['detail_link'] = sel.xpath('div[@class="a-row a-spacing-none"]/div[@class="a-row a-spacing-mini"]/div[position()=1]/a/@href').extract_first()
                #ページカウント
                product['page_count'] = response.xpath('//div[@id="bottomBar"]/div/span[@class="pagnCur"]/text()').extract_first()
                #ページURL
                product['url'] = response.url
                #データ取得時刻
                product['timestamp'] = jst_time

                yield product

        #次のリンクをチェックし、Requestを発行します。
        next_page = response.xpath('//a[@id="pagnNextLink"]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, callback=self.parse)
        # pass
