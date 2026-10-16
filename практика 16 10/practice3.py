"""Онлайн-магазин

Товар, заказ, покупатель и корзина. Корзина при оформлении создаёт заказ
и записывает его покупателю
"""

TAX_RATE = 0.20  # налог 20%


class Product:
    """товар на складе"""

    def __init__(self, name, price, stock, category):
        """название, цена, остаток и категория"""
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        """строка с данными товара"""
        return f"{self.name} ({self.category}): {self.price} руб., на складе: {self.stock}"


class Order:
    """заказ, считает сумму со скидкой и налогом"""

    def __init__(self, customer, items, discount=0.0):
        """покупатель, товары и скидка (0.1 это 10%)"""
        # items: список кортежей (Product, количество)
        self.customer = customer
        self.items = items
        self.discount = discount

    def subtotal(self):
        """сумма без скидки и налога"""
        return sum(product.price * quantity for product, quantity in self.items)

    def total(self):
        """итог: сначала скидка, потом налог"""
        # Сначала скидка, затем налог
        discounted = self.subtotal() * (1 - self.discount)
        return round(discounted * (1 + TAX_RATE), 2)


class Customer:
    """покупатель, хранит свои заказы"""

    def __init__(self, name, email):
        """имя, почта, список заказов пустой"""
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        """добавляет заказ в историю"""
        self.orders.append(order)

    def __str__(self):
        """строка с именем и количеством заказов"""
        return f"{self.name} <{self.email}>, заказов: {len(self.orders)}"


class ShoppingCart:
    """корзина, здесь выбираем товары"""

    def __init__(self, customer):
        """пустая корзина для покупателя"""
        self.customer = customer
        self.items = []  # список кортежей (Product, количество)

    def add_product(self, product, quantity=1):
        """кладёт товар в корзину, если на складе хватает"""
        if quantity > product.stock:
            raise ValueError(f"Недостаточно товара «{product.name}» на складе")
        self.items.append((product, quantity))

    def remove_product(self, product):
        """убирает товар из корзины"""
        self.items = [(p, q) for p, q in self.items if p is not product]

    def update_quantity(self, product, quantity):
        """меняет количество товара в корзине"""
        if quantity > product.stock:
            raise ValueError(f"Недостаточно товара «{product.name}» на складе")
        self.items = [(p, quantity if p is product else q) for p, q in self.items]

    def checkout(self, discount=0.0):
        """создаёт заказ, списывает товар со склада и очищает корзину"""
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
