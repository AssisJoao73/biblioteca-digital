import os
from collections import defaultdict

def listar_documentos_por_tipo_e_ano(base_dir="documentos"):
    documentos = defaultdict(lambda: defaultdict(list))  # {ano: {extensao: [nomes]}}

    for root, _, files in os.walk(base_dir):
        for file in files:
            if '.' in file:
                ano = os.path.basename(root)
                nome, extensao = os.path.splitext(file)
                documentos[ano][extensao.lower()].append(file)

    return documentos

def imprimir_documentos(documentos):
    for ano, tipos in sorted(documentos.items()):
        print(f"\n📅 Ano: {ano}")
        for tipo, arquivos in sorted(tipos.items()):
            print(f"  📄 Tipo {tipo}:")
            for arquivo in arquivos:
                print(f"    - {arquivo}")
