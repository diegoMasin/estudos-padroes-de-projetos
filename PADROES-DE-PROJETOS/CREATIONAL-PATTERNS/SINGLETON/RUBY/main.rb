
class Logger
  @instance = nil

  def self.instance
    @instance ||= new
  end

  private_class_method :new

  def log(message)
    puts message
  end
end

# Uso do Singleton
logger1 = Logger.instance
logger2 = Logger.instance

puts logger1.equal?(logger2) # true, ambas as variáveis referem-se à mesma instância

logger1.log("Log de teste") # Saída: Log de teste
