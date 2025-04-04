import platform

def main():
    sistema = platform.system()
    versao = platform.version()
    processador = platform.processor()
    print(f"Sistema Operacional: {sistema}")
    print(f"Versão do Sistema: {versao}")
    print(f"Arquitetura do Processador: {processador}")

if __name__ == "__main__":
    main()
