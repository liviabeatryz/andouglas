#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome, matricula,turmas, email):
    db.cur.execute("""
                   INSERT into public.teachers (nome, matricula, turmas, email )
                   VALUES ('%s','%s','%s', '%s')
    
                   """ % (nome, matricula, turmas, email))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM teachers
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def deletar(matricula):
    db.cur.execute("""
                   delete from teachers where matricula = '%s'
    
                   """ % (matricula))
    db.con.commit()