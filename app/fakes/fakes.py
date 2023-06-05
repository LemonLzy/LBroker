from faker import Faker
from faker.providers import internet

fake = Faker(locale='zh_CN')
fake.add_provider(internet)
