# Configuración del módulo de compras
def orderling_list(self):
    # 購入者の購入Contenidoに基づいて、購入者ごYの注文リストを表示する
    total = 0
    print(f"=====　Listas de pedidos por cliente({self.name}, {self.shop})　=====")
    for order in self.orders:
        print(f"Nombre del cliente: {order[0]}, cantidad de dinero: {order[1]}, fecha y hora：{order[2]}")
        total += order[1]
    print("--------------importe total：{}".format(total))
    print("====================================")

def _grocery_list(self, groceries):
    print("------Lista de la compra------")
    for i, grocery in enumerate(groceries):
        print(f"{i}: {grocery.name}, {grocery.price}")

def _shopping_list(self, basket):
    print(f"=====　lista de la compra({self.name}/{self.address})　=====")
    for grocery in basket:
        name = grocery[0].name
        price = grocery[0].price
        quantity = grocery[1]
        money = price * quantity
        print(f"nombre comercial (marca): {name}, volumen: {quantity}, cantidad de dinero：{money}")
        self.total += money
    print(f"----------importe total：{self.total}-------------")
    print("====================================")