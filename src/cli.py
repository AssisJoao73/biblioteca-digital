import argparse
import os
import shutil

DOCUMENTOS_DIR = "documentos"

def adicionar_documento(caminho_arquivo, ano):
    if not os.path.isfile(caminho_arquivo):
        print(" Arquivo não encontrado.")
        return

    ext = os.path.splitext(caminho_arquivo)[1].lower()
    nome = os.path.basename(caminho_arquivo)
    destino_dir = os.path.join(DOCUMENTOS_DIR, str(ano))

    os.makedirs(destino_dir, exist_ok=True)
    destino = os.path.join(destino_dir, nome)
    shutil.copy2(caminho_arquivo, destino)
    print(f" Documento '{nome}' adicionado em '{destino_dir}'.")

def renomear_documento(ano, nome_antigo, nome_novo):
    origem = os.path.join(DOCUMENTOS_DIR, str(ano), nome_antigo)
    destino = os.path.join(DOCUMENTOS_DIR, str(ano), nome_novo)

    if not os.path.isfile(origem):
        print(" Documento original não encontrado.")
        return

    os.rename(origem, destino)
    print(f" Documento renomeado para '{nome_novo}'.")

def remover_documento(ano, nome_arquivo):
    caminho = os.path.join(DOCUMENTOS_DIR, str(ano), nome_arquivo)

    if not os.path.isfile(caminho):
        print(" Documento não encontrado.")
        return

    os.remove(caminho)
    print(f" Documento '{nome_arquivo}' removido.")

def main():
    parser = argparse.ArgumentParser(description="Sistema de Gerenciamento de Biblioteca Digital")
    subparsers = parser.add_subparsers(dest="comando")

    # Adicionar
    parser_add = subparsers.add_parser("adicionar", help="Adicionar um novo documento")
    parser_add.add_argument("caminho", help="Caminho do arquivo")
    parser_add.add_argument("ano", help="Ano de publicação")

    # Renomear
    parser_rename = subparsers.add_parser("renomear", help="Renomear um documento")
    parser_rename.add_argument("ano", help="Ano de publicação")
    parser_rename.add_argument("nome_antigo", help="Nome atual do arquivo")
    parser_rename.add_argument("nome_novo", help="Novo nome do arquivo")

    # Remover
    parser_remove = subparsers.add_parser("remover", help="Remover um documento")
    parser_remove.add_argument("ano", help="Ano de publicação")
    parser_remove.add_argument("nome", help="Nome do arquivo a ser removido")

    args = parser.parse_args()

    if args.comando == "adicionar":
        adicionar_documento(args.caminho, args.ano)
    elif args.comando == "renomear":
        renomear_documento(args.ano, args.nome_antigo, args.nome_novo)
    elif args.comando == "remover":
        remover_documento(args.ano, args.nome)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
