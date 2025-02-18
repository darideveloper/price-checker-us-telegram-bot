import os
from database.mysql import MySQL
from dotenv import load_dotenv

# Load env variables
load_dotenv()
DB_SERVER = os.getenv("DB_SERVER")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT"))


class DB (MySQL):

    def __init__(self):
        """ Connect with mysql paerent class
        """

        # Connect with mysql
        super().__init__(DB_SERVER, DB_DATABASE, DB_USERNAME, DB_PASSWORD, DB_PORT)

    def get_bots(self) -> list:
        """ Get all bot tokens

        Returns:
            list: list of dictionaries with bots data

            Structure:
            [
                {
                    "id": int,
                    "name": str,
                    "token": str
                }
            ]
        """

        # Get all bot tokens
        sql = """
            SELECT
                *
            FROM
                bots_tokens
        """
        tokens = self.run_sql(sql)

        # Return tokens
        return tokens
