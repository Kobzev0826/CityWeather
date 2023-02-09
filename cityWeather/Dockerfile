FROM python:3.10-slim
RUN mkdir cityWeather
ADD /cityWeather /cityWeather
ADD cityWeatherScrapyService.py  requirements.txt scrapy.cfg .
RUN pip install -r requirements.txt
CMD ["python", "./cityWeatherScrapyService.py"]
# Or enter the name of your unique directory and parameter set.