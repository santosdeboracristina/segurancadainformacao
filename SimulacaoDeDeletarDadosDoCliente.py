import sqlite3, time
from datetime import datetime, timedelta

path = r'C:\sqlite3\Banco'# pasta onde se encontra o arquivo de BD
conn = sqlite3.connect(path+r'\test.db') # conexao com o BD
cur = conn.cursor() # cursor para dar comando no sqlite

dtime = 0
diad = 198

while dtime < 14: # Simulando injecao de dados de clientes no BD
    now = datetime.now() + timedelta(days = diad)

    year = now.strftime("%Y")

    month = now.strftime("%m")

    day = now.strftime("%d")

    DataExcusao = year+"-"+month+"-"+day
    print(DataExcusao)
    diad += 1
    dtime += 1

    inserir = "INSERT INTO cliente(Nome,CPF,Idade,DataDeEntrada,DataDeExcusão) VALUES('Daniel',45678949445,54,'2020-10-01','" + DataExcusao + "')"
    
    cur.execute(inserir)
    cur.execute("SELECT * FROM cliente")
    cliente = cur.fetchall()
    print(cliente)
    conn.commit()

dtime = 0
diad = 198

while dtime < 14: # Simulando o apagamento de dados e simulando a passagem de dias para apagar dados cliente no BD
    now = datetime.now() + timedelta(days = diad)

    year = now.strftime("%Y")

    month = now.strftime("%m")

    day = now.strftime("%d")

    DataExcusao = year+"-"+month+"-"+day
    print(DataExcusao)
    diad += 1
    dtime += 1

    delete = "DELETE FROM cliente WHERE DataDeExcusão = '" + DataExcusao + "'"
    cur.execute(delete)
    cur.execute("SELECT * FROM cliente")
    cliente = cur.fetchall()
    print(cliente)
    conn.commit()
    print ("--------------------------")
    time.sleep(2) 


cur.execute("SELECT * FROM cliente")
cliente = cur.fetchall()
print(cliente)
conn.close()
