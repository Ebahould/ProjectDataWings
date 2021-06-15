import psycopg2

try:
    conn = psycopg2.connect(
          user = "postgres",
         password = "96130055",
          host = "localhost",
          port = "5432",
          database = "Test"
    )
    cur = conn.cursor()

    # Afficher la version de PostgreSQL 
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("Version : ", version,"\n")
  
    #fermeture de la connexion à la base de données
    cur.close()
    conn.close()
    print("La connexion PostgreSQL est fermée")

except (Exception, psycopg2.Error) as error :
    print ("Erreur lors de la connexion à PostgreSQL", error)