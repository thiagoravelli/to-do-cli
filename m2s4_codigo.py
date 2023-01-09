import sqlite3 as sq

def conectar_ao_banco(nome_db: str):
    conexao = sq.connect(nome_db)
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()
    sql_TODO = '''
    CREATE TABLE IF NOT EXISTS TODO (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        tarefa VARCHAR(100),
        data VARCHAR(10),
        categoria_id INT NOT NULL,
        finalizada VARCHAR (3),
        CONSTRAINT categoria_FK FOREIGN KEY (categoria_id) REFERENCES categoria(id)
    );
    '''
    sql_categoria = '''
    CREATE TABLE IF NOT EXISTS categoria (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100)
    );
    '''
    cursor.execute(sql_TODO)
    cursor.execute(sql_categoria)
    conexao.commit()

def editar_categoria(conexao, selecao: str):
    cursor = conexao.cursor()
    sql_inserir = '''
    INSERT INTO categoria (nome) VALUES (?)
    '''
    sql_atualizar = '''
    UPDATE categoria SET nome = ? WHERE id = ?
    '''
    sql_deletar = '''
    DELETE FROM categoria WHERE id = ?
    '''
    def inserir():
        categoria = input('Digite o nome da categoria: ')
        values = [categoria]
        cursor.execute(sql_inserir, values)
        conexao.commit()

    def atualizar():
        id = input('Digite o ID da categoria que deseja atualizar: ')
        categoria = input('Digite o nome da categoria: ')
        values = [categoria, id]
        cursor.execute(sql_atualizar, values)
        conexao.commit()

    def deletar():
        id = int(input('Digite o ID da categoria que deseja deletar: '))
        values = [id]
        cursor.execute(sql_deletar, values)
        conexao.commit()

    def listar():
        sql_mostrar = '''
        SELECT * FROM categoria
        '''
        consulta = cursor.execute(sql_mostrar)
        id = "id".center(15)
        nome = "nome".center(15)
        print(f'*---------------*---------------*\n|{id}|{nome}|\n*---------------*---------------*')
        for resultado in consulta:
            resultado_id = str(resultado[0]).center(15)
            resultado_categoria = resultado[1].center(15)
            print(f"|{resultado_id}|{resultado_categoria}|")
        print('*---------------*---------------*')
        conexao.commit()

    if selecao == "inserir":
        inserir()
    
    if selecao == "atualizar":
        listar()
        atualizar()
    
    if selecao == "deletar":
        listar()
        deletar()

    if selecao == "listar":
        listar()

def editar_TODO(conexao, selecao: str):
    cursor = conexao.cursor()

    sql_inserir = '''
    INSERT INTO TODO (tarefa, data, categoria_id, finalizada) VALUES (?, ?, ?, ?)
    '''
    sql_atualizar = '''
    UPDATE TODO SET tarefa = ?, data = ?, categoria_id = ? WHERE id = ?
    '''
    sql_deletar = '''
    DELETE FROM TODO WHERE id = ?
    '''
    sql_finalizar = '''
    UPDATE TODO SET finalizada = "Sim" WHERE id = ?
    '''

    def inserir():
        tarefa = input('Digite o nome da tarefa: ')
        data = input('Digite a data da tarefa: ')
        categoria_id = int(input('Digite o ID da categoria: '))
        finalizada = input('A tarefa ja foi concluida? ')
        values = [tarefa, data, categoria_id, finalizada]
        cursor.execute(sql_inserir, values)
        conexao.commit()

    def atualizar():
        id = input('Digite o ID da tarefa que deseja atualizar: ')
        tarefa = input('Digite o nome da tarefa: ')
        data = input('Digite a data da tarefa: ')
        categoria_id = int(input('Digite o ID da categoria: '))
        values = [tarefa, data, categoria_id, id]
        cursor.execute(sql_atualizar, values)
        conexao.commit()

    def deletar():
        id = int(input('Digite o ID da tarefa que deseja deletar: '))
        values = [id]
        cursor.execute(sql_deletar, values)
        conexao.commit()
    
    def listar(opcao: str):
        if opcao == 'data':
            sql_mostrar = '''
            SELECT t. id, t.tarefa, c.nome, t.finalizada FROM TODO AS t, categoria as c WHERE data = ? AND c.id = t.categoria_id
            '''
            data = input('Digite a data que voce quer consultar: ')
            id = "id".center(15)
            nome = "nome".center(30)
            categoria = "categoria".center(15)
            finalizada = "finalizada".center(15)
            print(f'*---------------*------------------------------*---------------*---------------*\n|{id}|{nome}|{categoria}|{finalizada}|\n*---------------*------------------------------*---------------*---------------*')
            values = [data]
            consulta = cursor.execute(sql_mostrar, values)
            for resultado in consulta:
                resultado_id = str(resultado[0]).center(15)
                resultado_nome = resultado[1].center(30)
                resultado_categoria = resultado[2].center(15)
                resultado_finalizada = resultado[3].center(15)
                print(f"|{resultado_id}|{resultado_nome}|{resultado_categoria}|{resultado_finalizada}|")
            print('*---------------*------------------------------*---------------*---------------*')
            conexao.commit()

        if opcao == 'todos':
            sql_mostrar = '''
            SELECT t.id, t.tarefa, c.nome, t.data, t.finalizada FROM TODO AS t, categoria as c WHERE c.id = t.categoria_id
            '''
            id = "id".center(15)
            nome = "nome".center(30)
            categoria = "categoria".center(15)
            finalizada = "finalizada".center(15)
            data = "data".center(15)
            print(f'*---------------*------------------------------*---------------*---------------*---------------*\n|{id}|{nome}|{categoria}|{data}|{finalizada}|\n*---------------*------------------------------*---------------*---------------*---------------*')
            values = [data]
            consulta = cursor.execute(sql_mostrar)
            for resultado in consulta:
                resultado_id = str(resultado[0]).center(15)
                resultado_nome = resultado[1].center(30)
                resultado_data = resultado[2].center(15)
                resultado_categoria = resultado[3].center(15)
                resultado_finalizada = resultado[4].center(15)
                print(f"|{resultado_id}|{resultado_nome}|{resultado_data}|{resultado_categoria}|{resultado_finalizada}|")
            print('*---------------*------------------------------*---------------*---------------*---------------*')
            conexao.commit()
    
    def finalizar():
        id = int(input('Digite o ID da tarefa que deseja marcar como finalizada: '))
        values = [id]
        cursor.execute(sql_finalizar, values)
        conexao.commit()
    
    if selecao == "inserir":
        inserir()
    
    if selecao == "atualizar":
        listar("todos")
        atualizar()
    
    if selecao == "deletar":
        deletar()

    if selecao == "listar":
        listar("todos")
    
    if selecao == "listar_data":
        listar("data")
    
    if selecao == "finalizar":
        listar("todos")
        finalizar()