from google.cloud import bigquery
from google.cloud.bigquery import SchemaField
import pandas as pd

conditions_dict = {
    "Partially cloudy": 1,
    "Clear": 2,
    "Overcast": 3,
    "Rain, Partially cloudy": 4,
    "Snow, Partially cloudy": 5,
    "Rain, Overcast": 6,
    "Snow, Overcast": 7,
    "Rain": 8,
    "Snow, Rain, Partially cloudy": 9,
    "Snow": 10,
    "Snow, Rain, Overcast": 11,
    "Snow, Rain, Freezing Drizzle/Freezing Rain, Overcast": 12,
    "Snow, Rain, Ice, Overcast": 13,
    "Snow, Rain, Freezing Drizzle/Freezing Rain, Ice, Partially cloudy": 14,
    "Snow, Rain": 15,
    "Rain, Ice, Overcast": 16,
    "Snow, Rain, Ice, Partially cloudy": 17,
    "Snow, Ice, Overcast": 18
}

def csv_to_dataframe(csv_file_path):
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        return df
    except Exception as e:
        print("Error:", e)
        return None


def write_input_to_bq(df, schema, table_name):
    client = bigquery.Client(project='weather-prediction-419019')
    job_config = bigquery.LoadJobConfig(write_disposition='WRITE_TRUNCATE', schema=schema)

    table_name = f"weather-prediction-419019.weather_prediction.{table_name}"

    job = client.load_table_from_dataframe(df, table_name, job_config=job_config)
    job.result()

full_dataset = csv_to_dataframe('Toronto 1975-01-01 to 2023-12-31.csv')

full_dataset['datetime'] = pd.to_datetime(full_dataset['datetime'])
full_dataset['year'] = full_dataset['datetime'].dt.year
full_dataset['month'] = full_dataset['datetime'].dt.month
full_dataset['day'] = full_dataset['datetime'].dt.day

# Drop the original datetime column if not needed anymore
full_dataset.drop(["name", "stations", "sunrise", "sunset", "description", "icon", "datetime", "preciptype"], axis=1, inplace=True)

full_dataset['conditions'] = full_dataset['conditions'].replace(conditions_dict)

schema = [
    SchemaField("year", "INTEGER", mode="REQUIRED"),
    SchemaField("month", "INTEGER", mode="REQUIRED"),
    SchemaField("day", "INTEGER", mode="REQUIRED"),
    SchemaField("tempmax", "FLOAT", mode="REQUIRED"),
    SchemaField("tempmin", "FLOAT", mode="REQUIRED"),
    SchemaField("temp", "FLOAT", mode="REQUIRED"),
    SchemaField("feelslikemax", "FLOAT", mode="REQUIRED"),
    SchemaField("feelslikemin", "FLOAT", mode="REQUIRED"),
    SchemaField("feelslike", "FLOAT", mode="REQUIRED"),
    SchemaField("dew", "FLOAT"),
    SchemaField("humidity", "FLOAT"),
    SchemaField("precip", "FLOAT"),
    SchemaField("precipprob", "FLOAT"),
    SchemaField("precipcover", "FLOAT"),
    SchemaField("snow", "FLOAT"),
    SchemaField("snowdepth", "FLOAT"),
    SchemaField("windgust", "FLOAT"),
    SchemaField("windspeed", "FLOAT"),
    SchemaField("winddir", "FLOAT", mode="REQUIRED"),
    SchemaField("sealevelpressure", "FLOAT"),
    SchemaField("cloudcover", "FLOAT"),
    SchemaField("visibility", "FLOAT"),
    SchemaField("solarradiation", "FLOAT"),
    SchemaField("solarenergy", "FLOAT"),
    SchemaField("uvindex", "FLOAT"),
    SchemaField("severerisk", "FLOAT"),
    SchemaField("moonphase", "FLOAT", mode="REQUIRED"),
    SchemaField("conditions", "INTEGER", mode="REQUIRED"),
]
print(full_dataset)
write_input_to_bq(full_dataset, schema, 'full_weather_historical_dataset')