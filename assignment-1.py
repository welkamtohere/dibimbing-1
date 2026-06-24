class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self._order_id = order_id
        self._customer_name = customer_name
        self._order_date = order_date
        self._total_amount = total_amount

    def calculate_tax(self):
        tax_rate = 0.1
        return self._total_amount * tax_rate
    
    def get_total_amount(self):
        return self._total_amount

    def display_order(self):
        print(f"ID: {self._order_id} |  Name: {self._customer_name} | Total: {self._total_amount}")

class OrderProcessor:

    def __init__(self):
            self._orders = []

    def add_order(self, order):
        self._orders.append(order)

    def calculate_total_revenue(self):
        total = 0
        for order in self._orders:
            total += order.get_total_amount()

        return total

    def calculate_total_tax(self):
        total_tax = 0
        for order in self._orders:
            total_tax += order.calculate_tax()
        return total_tax

pesanan1 = Order("1", "John Doe", "2026-01-01", 10000)
pesanan2 = Order("2", "Jane Doe", "2026-01-02", 20000)
pesanan3 = Order("3", "Jim Doe", "2026-01-03", 30000)

processor = OrderProcessor()

processor.add_order(pesanan1)
processor.add_order(pesanan2)
processor.add_order(pesanan3)


pesanan1.display_order()
pesanan2.display_order()
pesanan3.display_order()


print(processor.calculate_total_revenue())
print(processor.calculate_total_tax())