import subprocess, schedule


def start_scrapy():
    subprocess.call(['scrapy', 'crawl', 'openweather_spider'])


if __name__ == '__main__':
    schedule.every(1).minutes.do(start_scrapy)
    while True:
        schedule.run_pending()