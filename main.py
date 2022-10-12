import psycopg2

try:
    connect = psycopg2.connect(
        database="content", user="postgres", password="12345", host="127.0.0.1", port = "5433"
    )

except:
    print("error")


def add(data):
    global connect
    cur = connect.cursor()

    fields = [
         

    ]

    for apidata in data:
        my_data = [apidata[field] for field in fields]
        insert_query = "INSERT INTO apidata VALUES (?, ?, ?)"
        cur.execute(insert_query, tuple(my_data))
        connect.commit()

    
    cur.close()

   
    connect.close()

