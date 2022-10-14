# Product Recommendation

This is product recommendations assignment where it recommends products with similar categories

# APIS working

1. To post and get product: localhost/product/api
2. To post and get orders: localhost/orders/api
3. To get similar product ids: localhost/product/recommend/<int:id>

# How to run this project

1. Clone the git repository.
2. Create a virtual environment.
3. Activate the virtual environment.
4. pip install -r "requirements.txt"
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver

# To populate Products Table run the following command

python manage.py createproduct

# To populate Orders Table run the following command

python manage.py createorder
