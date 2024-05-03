
class Logger:
    _instance = None  # Variável estática para armazenar a instância única

    # Note que não temos o construtor padrão __init__ e sim criamos o método new para ser o construtor singleton
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def log(self, message):
        print(message)


# Uso do Singleton
logger1 = Logger()
logger2 = Logger()

# Retorna True, para mostrar que amabos são mesma instância
print(logger1 is logger2)

logger1.log("Log de teste")  # Saída: Log de teste
