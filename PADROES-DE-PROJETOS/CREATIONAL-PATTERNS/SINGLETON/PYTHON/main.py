class Logger:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def log(self, message):
        print(message)

# Uso do Singleton
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # Retorna True, para mostrar que amabos são mesma instância

logger1.log("Log de teste")  # Saída: Log de teste