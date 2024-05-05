class Order
  attr_accessor :products, :address, :total

  def initialize(products = [], address = "", total = 0)
    @products = products
    @address = address
    @total = total
  end

  def to_s
    product_list = @products.map { |product| "- #{product[:name]}: #{product[:quantity]}" }.join("\n")
    "Pedido:\nProdutos:\n#{product_list}\nEndereço de entrega: #{@address}\nTotal: R$#{@total.round(2)}"
  end
end

class OrderBuilder
  def initialize
    @order = Order.new
  end

  def add_product(name, quantity)
    @order.products << { name: name, quantity: quantity }
    self
  end

  def set_address(address)
    @order.address = address
    self
  end

  def calculate_total
    @order.total = @order.products.sum { |product| product[:quantity] * 10 }
    self
  end

  def build
    @order
  end
end

class Director
  def initialize(builder)
    @builder = builder
  end

  def construct
    @builder.add_product("Camisa", 2)
            .add_product("Calça", 1)
            .set_address("Rua Principal, 123")
            .calculate_total
            .build
  end
end

# Uso do Builder com Director
builder = OrderBuilder.new
director = Director.new(builder)
order = director.construct

puts order
