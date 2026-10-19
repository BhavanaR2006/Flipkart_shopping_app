from flask import Flask, request, redirect, render_template_string, session, url_for

app = Flask(__name__)
app.secret_key = "flipkart-demo-secret"

products = [
    {"id": 1, "name": "Laptop", "price": 55000, "category": "Electronics", "description": "Laptop for work and study"},
    {"id": 2, "name": "Smartphone", "price": 25000, "category": "Mobiles", "description": "Smartphone with modern features"},
    {"id": 3, "name": "Headphones", "price": 2000, "category": "Accessories", "description": "Headphones for music and calls"},
    {"id": 4, "name": "Smart Watch", "price": 3500, "category": "Watches", "description": "Smart watch with useful features"},
    {"id": 5, "name": "Keyboard", "price": 1200, "category": "Accessories", "description": "Keyboard for everyday use"},
]

PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ShopKart Shopping Demo</title>
<style>
*{box-sizing:border-box}
body{margin:0;font-family:Arial,sans-serif;background:#f1f3f6;color:#222}
header{background:#2874f0;color:white;padding:16px 5%;display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.logo{font-size:25px;font-weight:bold}
.search{flex:1;min-width:180px}
.search input{width:100%;padding:12px;border:0;border-radius:4px}
nav{display:flex;gap:18px;flex-wrap:wrap}
nav a{color:white;text-decoration:none;font-weight:bold}
.categories{background:white;padding:15px;display:flex;justify-content:center;gap:30px;flex-wrap:wrap;box-shadow:0 2px 4px #ddd}
.categories a{color:#333;text-decoration:none}
main{max-width:1200px;margin:25px auto;padding:0 16px}
h2{margin-top:10px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:18px}
.card,.panel{background:white;padding:20px;border-radius:7px;box-shadow:0 2px 6px #ddd}
.icon{font-size:55px;text-align:center;padding:12px}
.price{font-size:21px;font-weight:bold}
button,.btn{display:inline-block;border:0;border-radius:4px;padding:11px 14px;color:white;background:#fb641b;cursor:pointer;text-decoration:none;margin:4px 3px 4px 0}
.blue{background:#2874f0}
input,select{padding:10px;margin:5px 0}
.track{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0}
.step{flex:1;min-width:100px;text-align:center;padding:12px 5px;background:#e5e7eb;border-radius:5px;font-size:13px}
.done{background:#bdebd0}
.active{background:#ffe0b2;font-weight:bold}
.muted{color:#666}
footer{text-align:center;padding:25px;color:#666}
@media(max-width:600px){header{gap:12px}.logo{width:100%}.categories{gap:12px}}
</style>
</head>
<body>
<header>
<div class="logo">ShopKart</div>
<form class="search" action="/" method="get">
<input name="q" placeholder="Search for products..." value="{{ q }}">
</form>
<nav>
<a href="/">Home</a>
<a href="/orders">My Orders</a>
<a href="/cart">Cart ({{ cart_count }})</a>
<a href="/logout">Logout</a>
</nav>
</header>
<div class="categories">
<a href="/">All Products</a><a href="/?category=Electronics">Electronics</a>
<a href="/?category=Mobiles">Mobiles</a><a href="/?category=Accessories">Accessories</a>
<a href="/?category=Watches">Watches</a>
</div>
<main>
{% if page == 'login' %}
<div class="panel" style="max-width:420px;margin:45px auto;text-align:center">
<h2>Customer Login</h2><p class="muted">Login to start shopping</p>
<form method="post" action="/login">
<input type="email" name="email" placeholder="Email address" required style="width:95%"><br>
<input type="password" name="password" placeholder="Password" required style="width:95%"><br>
<button type="submit">Login</button>
</form>
<p class="muted">Demo project: enter any email and password.</p>
</div>
{% elif page == 'home' %}
<h2>Welcome to ShopKart</h2>
<p>Discover products for your everyday needs.</p>
{% if message %}<div class="panel">{{ message }}</div>{% endif %}
<div class="grid">
{% for p in products %}
<div class="card">
<div class="icon">{{ p.icon }}</div>
<h3>{{ p.name }}</h3><p class="muted">{{ p.category }}</p>
<p class="price">₹{{ "{:,}".format(p.price) }}</p>
<p>{{ p.description }}</p>
<a class="btn blue" href="/product/{{ p.id }}">View Details</a>
<form method="post" action="/cart/add" style="display:inline">
<input type="hidden" name="id" value="{{ p.id }}"><button>Add to Cart</button>
</form>
</div>
{% else %}<p>No products found.</p>{% endfor %}
</div>
{% elif page == 'product' %}
<div class="panel">
<div class="icon">{{ product.icon }}</div><h2>{{ product.name }}</h2>
<p>{{ product.description }}</p><p>Category: {{ product.category }}</p>
<p class="price">₹{{ "{:,}".format(product.price) }}</p>
<form method="post" action="/cart/add"><input type="hidden" name="id" value="{{ product.id }}"><button>Add to Cart</button></form>
<a class="btn blue" href="/">Continue Shopping</a>
</div>
{% elif page == 'cart' %}
<h2>Shopping Cart</h2><div class="panel">
{% for item in cart %}
<p><b>{{ item.name }}</b> — ₹{{ "{:,}".format(item.price) }}</p>
{% else %}<p>Your cart is empty.</p>{% endfor %}
<hr><h3>Total: ₹{{ "{:,}".format(total) }}</h3>
{% if cart %}<form method="post" action="/checkout"><button>Place Order / Checkout</button></form>{% endif %}
<a class="btn blue" href="/">Continue Shopping</a>
</div>
{% elif page == 'orders' %}
<h2>My Orders & Tracking</h2>
{% for order in orders %}
<div class="panel" style="margin-bottom:18px">
<h3>Order #{{ order.id }}</h3><p>{{ order.items }}</p>
<p><b>Total: ₹{{ "{:,}".format(order.total) }}</b></p>
<p>Order Status: <b>{{ order.status }}</b></p>
<div class="track">
{% for s in statuses %}
<div class="step {% if loop.index0 < order.stage %}done{% elif loop.index0 == order.stage %}active{% endif %}">{{ s }}</div>
{% endfor %}
</div>
<form method="post" action="/demo-status/{{ order.id }}">
<label>Demo tracking status:</label>
<select name="status">
{% for s in statuses %}<option {% if s == order.status %}selected{% endif %}>{{ s }}</option>{% endfor %}
</select><button class="blue">Update Demo Status</button>
</form>
</div>
{% else %}
<div class="panel"><p>You have no orders yet. Add products to cart and checkout first.</p><a class="btn" href="/">Browse Products</a></div>
{% endfor %}
{% endif %}
</main>
<footer>ShopKart — Shopping Website Demo · Demo order statuses are not real courier updates.</footer>
</body>
</html>
"""

statuses = ["Order Placed", "Confirmed", "Shipped", "Out for Delivery", "Delivered"]
icons = {1: "💻", 2: "📱", 3: "🎧", 4: "⌚", 5: "⌨️"}
orders = []
next_order_id = 1001

def render_page(page, **kwargs):
    cart = session.get("cart", [])
    cart_count = len(cart)
    return render_template_string(
        PAGE, page=page, products=kwargs.get("products", []),
        product=kwargs.get("product"), cart=cart,
        total=sum(x["price"] for x in cart), cart_count=cart_count,
        q=kwargs.get("q", ""), category=kwargs.get("category", ""),
        message=kwargs.get("message", ""), orders=kwargs.get("orders", []),
        statuses=statuses
    )

@app.route("/")
def home():
    if not session.get("logged_in"):
        return render_page("login")
    q = request.args.get("q", "").strip().lower()
    category = request.args.get("category", "")
    filtered = []
    for p in products:
        if q and q not in (p["name"] + " " + p["description"] + " " + p["category"]).lower():
            continue
        if category and p["category"] != category:
            continue
        filtered.append({**p, "icon": icons[p["id"]]})
    return render_page("home", products=filtered, q=q, category=category)

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    if email and password:
        session["logged_in"] = True
        session["email"] = email
        session["cart"] = []
        return redirect(url_for("home"))
    return render_page("login", message="Please enter your email and password.")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    if not session.get("logged_in"):
        return redirect(url_for("home"))
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_page("product", product={**product, "icon": icons[product["id"]]})

@app.route("/cart")
def cart_page():
    if not session.get("logged_in"):
        return redirect(url_for("home"))
    return render_page("cart")

@app.route("/cart/add", methods=["POST"])
def add_to_cart():
    if not session.get("logged_in"):
        return redirect(url_for("home"))
    product_id = request.form.get("id", type=int)
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart = session.get("cart", [])
        cart.append({"id": product["id"], "name": product["name"], "price": product["price"]})
        session["cart"] = cart
    return redirect(url_for("cart_page"))

@app.route("/checkout", methods=["POST"])
def checkout():
    global next_order_id
    if not session.get("logged_in"):
        return redirect(url_for("home"))
    cart = session.get("cart", [])
    if not cart:
        return redirect(url_for("cart_page"))
    orders.append({
        "id": next_order_id,
        "items": ", ".join(x["name"] for x in cart),
        "total": sum(x["price"] for x in cart),
        "status": "Order Placed",
        "stage": 0,
        "email": session.get("email", "")
    })
    next_order_id += 1
    session["cart"] = []
    return redirect(url_for("orders_page"))

@app.route("/orders")
def orders_page():
    if not session.get("logged_in"):
        return redirect(url_for("home"))
    customer_orders = [o for o in orders if o["email"] == session.get("email", "")]
    return render_page("orders", orders=customer_orders)

@app.route("/demo-status/<int:order_id>", methods=["POST"])
def demo_status(order_id):
    if not session.get("logged_in"):
        return redirect(url_for("home"))
    status = request.form.get("status")
    if status not in statuses:
        return redirect(url_for("orders_page"))
    for order in orders:
        if order["id"] == order_id and order["email"] == session.get("email", ""):
            order["status"] = status
            order["stage"] = statuses.index(status)
    return redirect(url_for("orders_page"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6080)