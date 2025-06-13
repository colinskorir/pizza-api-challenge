# Seed data for the pizza API challenge
from .app import db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

def seed():
    db.drop_all()
    db.create_all()
    # Add restaurants
    r1 = Restaurant(name="Mario's Pizza", address="address1")
    r2 = Restaurant(name="Luigi's Pizza", address="address2")
    r3 = Restaurant(name="Kiki's Pizza", address="address3")
    db.session.add_all([r1, r2, r3])
    # Add pizzas
    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    db.session.add_all([p1, p2])
    db.session.commit()
    # Add restaurant pizzas
    rp1 = RestaurantPizza(price=5, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=10, pizza_id=p2.id, restaurant_id=r2.id)
    db.session.add_all([rp1, rp2])
    db.session.commit()

if __name__ == '__main__':
    from .app import app
    with app.app_context():
        seed()
        print('Database seeded!')
