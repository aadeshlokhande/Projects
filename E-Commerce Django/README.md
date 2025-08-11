# 🛒 Django E-Commerce Website

A simple **E-Commerce** web application built with **Django** that allows managing products and categories with full **CRUD (Create, Read, Update, Delete)** functionality.  

This project is a basic yet scalable starting point for building more advanced online stores.

---

## ✨ Features
- 📂 **Category Management** – Add, view, edit, and delete product categories.
- 🛍 **Product Management** – Add, view, edit, and delete products.
- 🔍 View products filtered by category.
- 📦 Product details page.
- 🛠 Built using Django's powerful **Model-View-Template** (MVT) architecture.

---

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default, easily replaceable with PostgreSQL/MySQL)
- **Others:** Django ORM for database operations

---

## 📂 Models
### Category Model
- `name` – Category name
- `description` – Category description

### Product Model
- `name` – Product name
- `description` – Product details
- `price` – Product price
- `category` – Foreign key to Category
- `image` – Product image (optional)

---
