from faker import Faker
import uuid

faker = Faker('pt_BR')

def GeraPedidos():
    return{
            "Latitude": int(faker.latitude()),
            "Longitude": int(faker.longitude()),
            "PedidoID": str(uuid.uuid4()),
            "ProdutoID": faker.random_int(min=1, max=30),
            "Status": "Pendente",
            "Cliente": faker.name(),
            "Data": faker.date(),
            "Quantidade": faker.random_int(min=1, max=50),
            "PrecoUnitario": faker.random_int(min=5, max=999),
        }
     
