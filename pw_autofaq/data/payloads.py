from faker import Faker

fake = Faker()


payload = {
    "id": "9d284ecc-0c99-40be-82d2-1c08fd1233ed",
    "login": "default",
    "email": fake.email(),
    "fullName": fake.first_name(),
    "payload": {}
    }