# ELEGANCE - Premium Clothing Store

A modern Django-based e-commerce application for selling premium clothing and accessories online.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)

## ✨ Features

- **User Authentication**: Register and login functionality
- **Product Catalog**: Browse Men's, Women's, and Accessories collections
- **Shopping Cart**: Add items to cart with quantity management
- **Cart Management**: View cart, update quantities, and calculate totals
- **Responsive Design**: Mobile-friendly interface with Bootstrap
- **User Dashboard**: Personalized greeting and user navigation

## 🛠️ Tech Stack

- **Backend**: Django 5.1.7
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Authentication**: Django's built-in authentication system
- **Python Version**: 3.13+

## 📦 Installation

### Prerequisites
- Python 3.13 or higher
- pip (Python package installer)
- Git

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/ramuuzz/project1.git
cd project1
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

3. **Install dependencies**
```bash
pip install django pillow
```

4. **Apply migrations**
```bash
cd project1
python manage.py migrate
```

5. **Create a superuser (admin)**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## ⚙️ Configuration

### Settings
Edit `project1/settings.py` to configure:
- `ALLOWED_HOSTS`: Add your domain
- `DEBUG`: Set to `False` in production
- `DATABASES`: Configure database connection
- `STATIC_URL`: Static files location
- `MEDIA_URL`: Media files location

### Media Files
Ensure the following directories exist:
```
project1/
├── mens/              # Men's product images
├── womens/            # Women's product images
├── accessories/       # Accessories images
└── static/            # Static CSS/JS files
```

## 🚀 Usage

### Admin Panel
Access the Django admin at `/admin` with your superuser credentials to:
- Add/edit products
- Manage users
- View cart items

### User Flow

1. **Register**: Create a new account at `/register`
2. **Login**: Sign in at `/login`
3. **Browse**: View products on the home page
4. **Add to Cart**: Click "Add to Cart" on any product
5. **View Cart**: Click the 🛒 icon in the navigation
6. **Checkout**: Proceed with payment (feature coming soon)
7. **Logout**: Sign out at any time

## 📁 Project Structure

```
project1/
├── project1/                 # Main project folder
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI config
│   ├── asgi.py              # ASGI config
│   └── __pycache__/
│
├── store/                    # Django app for e-commerce
│   ├── migrations/          # Database migrations
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL routing
│   ├── admin.py             # Admin configuration
│   ├── apps.py              # App configuration
│   └── tests.py             # Unit tests
│
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── home.html           # Homepage
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   └── cart.html           # Shopping cart
│
├── static/                 # Static files (CSS, JS, images)
├── mens/                   # Men's product images
├── womens/                 # Women's product images
├── accessories/            # Accessories images
├── manage.py               # Django CLI
├── db.sqlite3              # SQLite database
└── README.md               # This file
```

## 🔌 API Endpoints

### Authentication
- `GET /login` - Login page
- `POST /login` - Handle login
- `GET /register` - Registration page
- `POST /register` - Create new user
- `GET /logout` - Logout user

### Store
- `GET /` - Home page with all products
- `GET /cart/` - View shopping cart
- `GET /add-to-cart/<item_id>/<item_type>/` - Add item to cart

### Admin
- `GET /admin/` - Django admin panel

## 💾 Database Models

### User (Django Built-in)
```python
- username (CharField)
- password (CharField)
- email (EmailField)
```

### Mens
```python
- id (AutoField, Primary Key)
- name (CharField)
- price (DecimalField)
- description (TextField)
- image (ImageField)
```

### Womens
```python
- id (AutoField, Primary Key)
- name (CharField)
- price (DecimalField)
- description (TextField)
- image (ImageField)
```

### Accessoriess
```python
- id (AutoField, Primary Key)
- name (CharField)
- price (DecimalField)
- description (TextField)
- image (ImageField)
```

### Cart
```python
- id (AutoField, Primary Key)
- user (ForeignKey to User)
- item_id (IntegerField)
- item_type (CharField) - 'mens', 'womens', or 'accessories'
- item_name (CharField)
- item_price (DecimalField)
- quantity (IntegerField, default=1)
```

## 🔄 Recent Updates

### Cart Functionality
- ✅ Added `quantity` field to cart model
- ✅ Implemented `add_to_cart` view with quantity increment
- ✅ Created cart display template with total calculation
- ✅ Updated home page with functional Add to Cart buttons
- ✅ Fixed authentication checks on cart operations

### Template Fixes
- ✅ Updated `base.html` with proper e-commerce styling
- ✅ Fixed navigation with cart icon and user menu
- ✅ Created responsive product grid on home page

## 📝 Future Enhancements

- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] Order management system
- [ ] Product filtering and search
- [ ] User profile and order history
- [ ] Wishlist functionality
- [ ] Product reviews and ratings
- [ ] Inventory management
- [ ] Email notifications
- [ ] Admin dashboard
- [ ] API documentation

## 🐛 Troubleshooting

### Images not loading
- Ensure images are in the correct directory (mens/, womens/, accessories/)
- Check `MEDIA_URL` and `MEDIA_ROOT` in settings.py
- Run `python manage.py collectstatic` if needed

### Database errors
- Delete `db.sqlite3` and run migrations again: `python manage.py migrate`
- Clear `__pycache__` folders

### Port already in use
```bash
python manage.py runserver 8001  # Use different port
```

## 📧 Contact & Support

For issues or questions, please open an issue on GitHub or contact the project maintainer.

## 📄 License

This project is open source and available under the MIT License.

---

**Made with ❤️ by Ram**  
**GitHub**: [ramuuzz](https://github.com/ramuuzz)
