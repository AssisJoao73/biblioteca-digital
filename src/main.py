from gerenciador_arquivos import listar_documentos_por_tipo_e_ano, imprimir_documentos

if __name__ == "__main__":
    docs = listar_documentos_por_tipo_e_ano()
    imprimir_documentos(docs)
