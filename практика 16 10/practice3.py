TAX_RATE = 0.20


class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}): {self.price} руб., на складе: {self.stock}"


class Order:
    def __init__(self, customer, items, discount=0.0):
        # items: список кортежей (Product, количество)
        self.customer = customer
        self.items = items
        self.discount = discount

    def subtotal(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def total(self):
        # Сначала скидка, затем налог
        discounted = self.subtotal() * (1 - self.discount)
        return round(discounted * (1 + TAX_RATE), 2)


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"{self.name} <{self.email}>, заказов: {len(self.orders)}"


class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []  # список кортежей (Product, количество)

    def add_product(self, product, quantity=1):
        if quantity > product.stock:
            raise ValueError(f"Недостаточно товара «{product.name}» на складе")
        self.items.append((product, quantity))

    def remove_product(self, product):
        self.items = [(p, q) for p, q in self.items if p is not product]

    def update_quantity(self, product, quantity):
        if quantity > product.stock:
            raise ValueError(f"Недостаточно товара «{product.name}» на складе")
        self.items = [(p, quantity if p is product else q) for p, q in self.items]

    def checkout(self, discount=0.0):
        order = Order(self.customer, list(self.items), discount)
        for product, quantity in self.items:
            product.stock -= quantity
        self.customer.add_order(order)
        self.items = []
        return order


if __name__ == "__main__":
    laptop = Product("Ноутбук", 80000, stock=5, category="Электроника")
    mouse = Product("Мышь", 1500, stock=20, category="Аксессуары")

    ivan = Customer("Иван", "ivan@example.com")
    cart = ShoppingCart(ivan)
    cart.add_product(laptop, 1)
    cart.add_product(mouse, 2)
    cart.update_quantity(mouse, 3)

    order = cart.checkout(discount=0.10)
    print(f"Сумма заказа с налогом и скидкой: {order.total()} руб.")
    print(ivan)
    print(laptop)
