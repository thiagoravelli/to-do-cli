import m2s4_codigo as db
import argparse

conexao = db.conectar_ao_banco("m2s4.db")
db.criar_tabelas(conexao)

parser = argparse.ArgumentParser(
    description="Editar banco de dados",
    epilog="tarefa ou categoria",
    add_help=True
)

parser.add_argument(
    '--adicionar_tarefa',
    help='Adiciona tarefa',
    action='store_true'
)

parser.add_argument(
    '--adicionar_categoria',
    help='Adiciona categoria',
    action='store_true'
)

parser.add_argument(
    '--atualizar_tarefa',
    help='Atualizar tarefa',
    action='store_true'
)

parser.add_argument(
    '--atualizar_categoria',
    help='Atualizar categoria',
    action='store_true'
)

parser.add_argument(
    '--deletar_tarefa',
    help='deletar tarefa',
    action='store_true'
)

parser.add_argument(
    '--deletar_categoria',
    help='deletar categoria',
    action='store_true'
)

parser.add_argument(
    '--listar_tarefa',
    help='listar tarefa',
    action='store_true'
)

parser.add_argument(
    '--listar_tarefa_data',
    help='listar tarefa de uma data',
    action='store_true'
)

parser.add_argument(
    '--listar_categoria',
    help='listar categoria',
    action='store_true'
)

parser.add_argument(
    '--finalizar_tarefa',
    help='Finalizar tarefa',
    action='store_true'
)

args = parser.parse_args()

if args.adicionar_tarefa:
    db.editar_categoria(conexao, "listar")
    db.editar_TODO(conexao, "inserir")

if args.adicionar_categoria:
    db.editar_categoria(conexao, "inserir")

if args.atualizar_tarefa:
    db.editar_TODO(conexao, "listar")
    db.editar_TODO(conexao, "atualizar")

if args.atualizar_categoria:
    db.editar_categoria(conexao, "listar")
    db.editar_categoria(conexao, "atualizar")

if args.deletar_tarefa:
    db.editar_TODO(conexao, "listar")
    db.editar_TODO(conexao, "deletar")

if args.deletar_categoria:
    db.editar_categoria(conexao, "listar")
    db.editar_categoria(conexao, "deletar")

if args.listar_tarefa:
    db.editar_TODO(conexao, "listar")

if args.listar_tarefa_data:
    db.editar_TODO(conexao, "listar_data")

if args.listar_categoria:
    db.editar_categoria(conexao, "listar")

if args.finalizar_tarefa:
    db.editar_TODO(conexao, "finalizar")