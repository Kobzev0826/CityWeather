FROM python:3.10-slim
ADD CityWeatherAPI.py ResponseModels.py openweathermap.py models.py  requirements.txt repository.py .
ENV MYSQL_DATABASE=cityWeather
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=123456
RUN pip install -r requirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "CityWeatherAPI:app"]