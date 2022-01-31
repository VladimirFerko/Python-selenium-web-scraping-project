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

# function for inserting product prices

def insert_product(conn, handled_data, product, product_name):

    # last print
    expensive_idx = len(handled_data) - 1

    print(f'The product you have searched for is : {product} \nI have found this product : {product_name.text}\nThis is the best offer..\n')
    print(f'Product price       {handled_data[0][0]} €')
    print(f'Shipping            {handled_data[0][1]} €')
    print(f'Total               {handled_data[0][0] + handled_data[0][1]} €')
    print(f'Eshop               {handled_data[0][2]}')

    print('\nThis is the worst offer..\n')
    print(f'Product price       {handled_data[expensive_idx][0]} €')
    print(f'Shipping            {handled_data[expensive_idx][1]} €')
    print(f'Total               {handled_data[expensive_idx][0] + handled_data[expensive_idx][1]} €')
    print(f'Eshop               {handled_data[expensive_idx][2]}')

    
    # writing into a database
    conn = make_conn()

    
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                f"""INSERT INTO price_comparison (product_name, high_product_price, high_shipping, low_product_price, low_shipping, high_eshop, low_eshop)
                    VALUES (N'{product_name.text}', {handled_data[expensive_idx][0]}, {handled_data[expensive_idx][1]}, {handled_data[0][0]}, {handled_data[0][1]}, '{handled_data[expensive_idx][2]}', '{handled_data[0][2]}');
                """
            )

    conn.close()
            

