    import requests
    import pandas
    import psycopg2
    import json
    class DataLoader:
        @staticmethod
        def load_data_from_api(api_url, params=None):
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Failed to fetch data from API: {response.status_code}")
            
        @staticmethod
        def load_data_from_csv(file_path):
            if os.path.exists(file_path):
                return pandas.read_csv(file_path)
            else:
                raise Exception(f"File not found: {file_path}") 
            
        @staticmethod
        def load_data_from_postgres(query, db_config):
            conn = psycopg2.connect(**db_config)
            df = pandas.read_sql_query(query, conn)
            conn.close()
            return df

        @staticmethod
        def load_data_from_json(file_path):
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    return json.load(file)
            else:
                raise Exception(f"File not found: {file_path}") 


        @staticmethod
        def load_data_from_excel(file_path, sheet_name=0):
            if os.path.exists(file_path):
                return pandas.read_excel(file_path, sheet_name=sheet_name)
            else:
                raise Exception(f"File not found: {file_path}")