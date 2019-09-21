from faker import Faker
from appTwo.models import User
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

django.setup()


fake = Faker()


def populate(n=5):
    """Create fake data with Faker generator."""

    for _ in range(n):
        # Generate fake name
        fake_name = fake.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]

        # Generate fake email
        fake_email = fake.email()

        # Create new entry with fakes
        user = User.objects.get_or_create(
            first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == "__main__":
    print("Population fake data...")
    populate()
    print("Population completed!")
