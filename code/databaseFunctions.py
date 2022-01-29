import psycopg2
import datetime as dt

# function for creating a connection with the database
def make_conn():
    conn = psycopg2.connect(
        host = "localhost",
        database = "web_scrape_project",
        user = "postgres",
        password = "password"
    )   

    return conn


# function for isnterting in the first table
def insert_search(conn, demand, wantDownl, count):

    # getting the time of the search
    current_date = str(dt.datetime.now())

    with conn:
        with conn.cursor() as cur:
            if wantDownl:
                cur.execute(
                    f"""INSERT INTO chrome_history (demand, is_downloaded, download_count, search_time)
                        VALUES ('{demand}', '{wantDownl}', '{count}', '{current_date[:19]}');
                    """
                )
            else:
                cur.execute(
                    f"""INSERT INTO chrome_history (demand, is_downloaded, download_count, search_time)
                        VALUES ('{demand}', '{wantDownl}', NULL, '{current_date[:19]}');
                    """
                )
