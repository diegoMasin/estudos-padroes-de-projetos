
class Logger {
    constructor() {
      if (!Logger.instance) {
        this._instance = this;
        // Inicialização aqui, se necessário
        Logger.instance = this;
      }
      return Logger.instance;
    }
  
    log(message) {
      console.log(message);
    }
  }
  
  // Uso do Singleton
  const logger1 = new Logger();
  const logger2 = new Logger();
  
  console.log(logger1 === logger2); // true, ambas as variáveis referem-se à mesma instância
  
  logger1.log("Log de teste"); // Saída: Log de teste
