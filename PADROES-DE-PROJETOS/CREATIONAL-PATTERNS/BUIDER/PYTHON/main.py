class Order:
    def __init__(self, products=None, address=None, total=0):
        self.products = products if products else []
        self.address = address
        self.total = total

    def __str__(self):
        product_list = "\n".join(
            [f"- {product['name']}: {product['quantity']}" for product in self.products])
        return f"Pedido:\nProdutos:\n{product_list}\nEndereço de entrega: {self.address}\nTotal: R${self.total:.2f}"


class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def add_product(self, name, quantity):
        self.order.products.append({'name': name, 'quantity': quantity})
        return self

    def set_address(self, address):
        self.order.address = address
        return self

    def calculate_total(self):
        # Lógica para calcular o total do pedido baseado nos produtos
        self.order.total = sum(
            product['quantity'] * 10 for product in self.order.products)
        return self

    def build(self):
        return self.order


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.add_product("Camisa", 2) \
                    .add_product("Calça", 1) \
                    .set_address("Rua Principal, 123") \
                    .calculate_total()
        return self.builder.build()


# Uso do Builder com Director
builder = OrderBuilder()
director = Director(builder)
order = director.construct()

print(order)
