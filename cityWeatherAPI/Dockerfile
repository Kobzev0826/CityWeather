FROM python:3.10-slim
ADD CityWeatherAPI.py RepositoryModels.py .
ADD models.py  requirements.txt repository.py .
RUN pip install -r requirements.txt
CMD ["python", "-m", "uvicorn", "CityWeatherAPI:app"]