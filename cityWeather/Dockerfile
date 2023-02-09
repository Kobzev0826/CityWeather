FROM python:3.10
ADD cityWeatherScrapyService.py  /cityWeather requirements.txt scrapy.cfg .
RUN pip install -r requirements.txt
CMD ["python", "./cityWeatherScrapyService.py"]
# Or enter the name of your unique directory and parameter set.