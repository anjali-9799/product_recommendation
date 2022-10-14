import random
from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from products.models import Product

PRODUCTS = ["chair", "stool", "table", "mug", "cup", "desk lamp", "floor lamp", " desk", "shelf", "sofa", "tea cup", "tea pot", "cutlery", "chess set", "lounge", " alarm clock", "phone dock", "keyboard", "side table", "wallet", "vase", "dog bed", "bird house", "wine holder", "skateboard", "calculator", "coathanger", "salt & pepper shaker",  "piggy bank", "headphones", "sculpture", "telephone", "flashlight", "mail sorter", "playing cards", "fan", "jewelry box", "mouse", "lantern", "walking cane", "sword", "wall clock", "mirror", "bed", "crib", "hammock", "plate", "bowl",
            "coffee mug", "espresso cup", "glasses", "fork", "spoon", "knife", "serving tray", "toy train", "action figure", "lamp shade", "cutting board", "dresser", "shoe rack", "rocking chair", "usb key", "8 ball", "frying pan", "drawer handle", "doorknob", "cable organizer", "planter pot", "coat hanger", "bottle opener", "can opener", "coasters", "pocket knife", "surfboard", "shoes", "book", "calendar", "house numbers", "spice rack", "suitcase", "button", "ring", "baking tray", "tape dispenser", "flower pot", "canoe", "basket", "pillow", "rug", "wall tile", "road bike", "bike seat", "handlebars"]
CATEGORIES = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]


class Provider(faker.providers.BaseProvider):
    def product_category(self):
        return self.random_element(CATEGORIES)

    def product_names(self):
        return self.random_element(PRODUCTS)


class Command(BaseCommand):
    help = 'Command information'

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(Provider)

        for _ in range(1000):
            pname = fake.product_names()
            pcat = fake.product_category()
            Product.objects.create(
                product_name=pname,
                categories=pcat.upper(),
                description=fake.text(max_nb_chars=250),
                unit_price=(round(random.uniform(0.01, 999999.99), 2)),
                quatity=random.randint(1, 250),
                for_sale=fake.boolean(),
                in_stock=fake.boolean(),
                review=fake.text(max_nb_chars=100),
                rating=random.randint(0, 5),
            )
