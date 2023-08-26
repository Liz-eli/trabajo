from grocery import Grocery
from customer import Customer
from seller import Seller

# Instanciación de vendedor (Ichiro Takahashi, Una tienda).
ichiro = Seller("Ichiro Takahashi", "Una tienda.")

# Creación de listas de productos（objeto）
groceries = []
groceries = Grocery("plátano", 300),\
            Grocery("pan", 150),\
            Grocery("leche (de vaca)", 230),\
            Grocery("huevo", 280),\
            Grocery("carne", 800),\
            Grocery("pescado", 500)

# Taro Yamadaをインスタンス化
taro = Customer("Taro Yamada", "Tokyo")
# Instanciación de Hanako Suzuki.
hanako = Customer("Hanako Suzuki", "Nagoya")
# Instanciación de Tommy Sasaki.
tommy = Customer("Tommy Sasaki", "Osaka")

# Taro Yamadaの買い物＆lista de la compra作成
order = taro.shopping(groceries)
ichiro.ordered(order)
# Hanako Suzuki shopping & creating lista de la compra
order = hanako.shopping(groceries)
ichiro.ordered(order)
# Sasaki Tommy shopping & creating lista de la compra
order = tommy.shopping(groceries)
ichiro.ordered(order)

# Visualización de listas de pedidos por cliente individual.
ichiro.orderling_list()