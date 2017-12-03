import scrapy
from scrapy.http import FormRequest
from unidecode import unidecode

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.goodreads.com/user/sign_in',
    ]
    quotes_url = 'https://www.goodreads.com/author/quotes/1244.Mark_Twain'

    def __init__(self, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)

    def parse(self,response):
        return [FormRequest.from_response(response,
                formdata={'user[email]': 'balavnth@gmail.com', 'user[password]': 'Expedia@GoodReads'},
                callback=self.after_login)]

    def after_login(self, response):
        yield response.follow(self.quotes_url, callback=self.parse_quotes)

    def parse_quotes(self, response):
        for index, quoteDetail in enumerate(response.css('div.quoteDetails')):
            if(index < 10):
                yield{
                    'text' : unidecode(quoteDetail.css('div.quoteText::text').extract_first().strip()).strip('"'),
                    'author': quoteDetail.css('div.quoteText>a::text').extract_first(),
                    'likes': quoteDetail.css('div.quoteFooter>div.right>a::text').extract_first()
                }
