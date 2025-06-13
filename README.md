# Pizza API Challenge

A RESTful API for managing restaurants, pizzas, and their relationships, built with Flask, SQLAlchemy, and Flask-Migrate using the MVC pattern.

---

## 🧰 Setup Instructions

1. **Clone the repository and navigate to the project folder.**
2. **Install dependencies and activate your environment:**
   ```bash
   pipenv install flask flask_sqlalchemy flask_migrate
   pipenv shell
   ```
3. **Set up the database:**
   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
4. **Seed the database:**
   ```bash
   python -m server.seed
   ```

---

## 🗂 Project Structure (MVC)

```
server/
  ├── app.py
  ├── config.py
  ├── models/
  │   ├── __init__.py
  │   ├── restaurant.py
  │   ├── pizza.py
  │   └── restaurant_pizza.py
  ├── controllers/
  │   ├── __init__.py
  │   ├── restaurant_controller.py
  │   ├── pizza_controller.py
  │   └── restaurant_pizza_controller.py
  └── seed.py
migrations/
instance/pizza.db
challenge-1-pizzas.postman_collection.json
README.md
```

---

## 🛠 API Routes

### GET `/restaurants`
Returns a list of all restaurants.

### GET `/restaurants/<int:id>`
Returns details of a single restaurant and its pizzas.
- If not found:  
  `{ "error": "Restaurant not found" }` (404)

### DELETE `/restaurants/<int:id>`
Deletes a restaurant and all related RestaurantPizzas.
- If successful: 204 No Content
- If not found:  
  `{ "error": "Restaurant not found" }` (404)

### GET `/pizzas`
Returns a list of pizzas.

### POST `/restaurant_pizzas`
Creates a new RestaurantPizza.
- **Request:**
  ```json
  { "price": 5, "pizza_id": 1, "restaurant_id": 3 }
  ```
- **Success response:**
  ```json
  {
    "id": 4,
    "price": 5,
    "pizza_id": 1,
    "restaurant_id": 3,
    "pizza": { "id": 1, "name": "Emma", "ingredients": "Dough, Tomato Sauce, Cheese" },
    "restaurant": { "id": 3, "name": "Kiki's Pizza", "address": "address3" }
  }
  ```
- **Error response:**
  ```json
  { "errors": ["Price must be between 1 and 30"] }
  ```
  (400 Bad Request)

---

## ✅ Validation Rules

- `RestaurantPizza.price` must be between 1 and 30 (inclusive).
- `pizza_id` and `restaurant_id` must reference existing records.

---

## 🔎 Testing with Postman

- Import `challenge-1-pizzas.postman_collection.json` into Postman.
- Test each route as described above.

---

## 📝 Notes

- Deleting a restaurant will also delete all related RestaurantPizzas (cascading delete).
- All models and controllers follow the MVC pattern.
- The root endpoint `/` returns a simple status message.

---

## Example Usage

### Get all restaurants
```
GET http://localhost:5000/restaurants
```

### Get a single restaurant
```
GET http://localhost:5000/restaurants/1
```

### Delete a restaurant
```
DELETE http://localhost:5000/restaurants/1
```

### Get all pizzas
```
GET http://localhost:5000/pizzas
```

### Create a restaurant pizza
```
POST http://localhost:5000/restaurant_pizzas
Content-Type: application/json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

---

For any issues or questions, please contact the project maintainer(Collins).
