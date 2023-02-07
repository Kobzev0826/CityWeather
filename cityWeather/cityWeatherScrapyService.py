import subprocess, schedule
from dotenv import load_dotenv

def start_scrapy():
    subprocess.call(['scrapy', 'crawl', 'openweather_spider'])


if __name__ == '__main__':
    load_dotenv()
    subprocess.call(['scrapy', 'crawl', 'openweather_spider'])
    # schedule.every(1).minutes.do(start_scrapy)
    # while True:
    #     schedule.run_pending()