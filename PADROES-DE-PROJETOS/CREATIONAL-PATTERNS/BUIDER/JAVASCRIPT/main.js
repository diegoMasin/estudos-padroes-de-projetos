class Order {
    constructor(products = [], address = "", total = 0) {
      this.products = products;
      this.address = address;
      this.total = total;
    }
  
    toString() {
      const productList = this.products.map(product => `- ${product.name}: ${product.quantity}`).join("\n");
      return `Pedido:\nProdutos:\n${productList}\nEndereço de entrega: ${this.address}\nTotal: R$${this.total.toFixed(2)}`;
    }
  }
  
  class OrderBuilder {
    constructor() {
      this.order = new Order();
    }
  
    addProduct(name, quantity) {
      this.order.products.push({ name, quantity });
      return this;
    }
  
    setAddress(address) {
      this.order.address = address;
      return this;
    }
  
    calculateTotal() {
      this.order.total = this.order.products.reduce((total, product) => total + product.quantity * 10, 0);
      return this;
    }
  
    build() {
      return this.order;
    }
  }
  
  class Director {
    constructor(builder) {
      this.builder = builder;
    }
  
    construct() {
      this.builder.addProduct("Camisa", 2)
                  .addProduct("Calça", 1)
                  .setAddress("Rua Principal, 123")
                  .calculateTotal();
      return this.builder.build();
    }
  }
  
  // Uso do Builder com Director
  const builder = new OrderBuilder();
  const director = new Director(builder);
  const order = director.construct();
  
  console.log(order.toString());
  