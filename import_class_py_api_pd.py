import pandas as pd
import psycopg2
import requests



class DataLoader:
    @staticmethod
    def load_from_csv(filepath:str):
        return pd.read_csv(filepath)
    
    
    @staticmethod
    def load_from_postgres(host:str, database:str, user:str, password:str, query:str):
        """Load data from PostgreSQL database using the provided connection parameters."""
        try:
            conn = psycopg2.connect(host=host, database=database, user=user, password=password)
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            raise Exception(f"Error loading data from PostgreSQL: {e}")
    
    
    @staticmethod
    def from_api(url: str):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return pd.DataFrame(response.json())
    