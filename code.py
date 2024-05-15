
import streamlit as st

# Page layout
st.set_page_config(layout="wide")

# Placeholder data
products = [
    {"name": "Full BCA Simulation Test", "price": "$9.99",
     "description": "A full BCA Simulation Test where students recieve an english essay and math exam, as well as a deatailed answer key, full english walkthrough, and admitted student practice essay.",
     "image": "https://www.google.com/imgres?q=testing%20image&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1273058761%2Fvector%2Ftiny-people-testing-quality-assurance-in-software.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DDsNlOqfMpPkHlVEavkrz8atzgOxVSRgZPkGHYH-e1-8%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Ftiny-people-testing-quality-assurance-in-software-gm1273058761-375129817&docid=sq7JjeJRPgimeM&tbnid=8F9ehayUEJET3M&vet=12ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA..i&w=612&h=430&hcb=2&ved=2ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA"},
    {"name": "5 Full BCA Simulation Test", "price": "$39.99",
     "description": "A full BCA Simulation Test where students recieve an english essay and math exam, as well as a deatailed answer key, full english walkthrough, and admitted student practice essay.",
     "image": "https://www.google.com/imgres?q=testing%20image&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1273058761%2Fvector%2Ftiny-people-testing-quality-assurance-in-software.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DDsNlOqfMpPkHlVEavkrz8atzgOxVSRgZPkGHYH-e1-8%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Ftiny-people-testing-quality-assurance-in-software-gm1273058761-375129817&docid=sq7JjeJRPgimeM&tbnid=8F9ehayUEJET3M&vet=12ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA..i&w=612&h=430&hcb=2&ved=2ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA"},
    {"name": "10 Full BCA Simulation Test", "price": "$69.99",
     "description": "A full BCA Simulation Test where students recieve an english essay and math exam, as well as a deatailed answer key, full english walkthrough, and admitted student practice essay.",
     "image": "https://www.google.com/imgres?q=testing%20image&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1273058761%2Fvector%2Ftiny-people-testing-quality-assurance-in-software.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DDsNlOqfMpPkHlVEavkrz8atzgOxVSRgZPkGHYH-e1-8%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Ftiny-people-testing-quality-assurance-in-software-gm1273058761-375129817&docid=sq7JjeJRPgimeM&tbnid=8F9ehayUEJET3M&vet=12ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA..i&w=612&h=430&hcb=2&ved=2ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA"},
    {"name": "Math Practice Workbook", "price": "$49.99", "description": "Comprehensive math workbook covering all topics tested in the BCA admission test. Includes practice questions with solutions.", "image": "https://www.google.com/imgres?q=testing%20image&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1273058761%2Fvector%2Ftiny-people-testing-quality-assurance-in-software.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DDsNlOqfMpPkHlVEavkrz8atzgOxVSRgZPkGHYH-e1-8%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Ftiny-people-testing-quality-assurance-in-software-gm1273058761-375129817&docid=sq7JjeJRPgimeM&tbnid=8F9ehayUEJET3M&vet=12ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA..i&w=612&h=430&hcb=2&ved=2ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA"},
    {"name": "Live Guidance Session with Current BCA Student", "price": "$99.99", "description": "Join a call with a recently admitted BCA student who will review you essay for up to 3 iterations and join you on a 1 hour long call.", "image": "https://www.google.com/imgres?q=testing%20image&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1273058761%2Fvector%2Ftiny-people-testing-quality-assurance-in-software.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DDsNlOqfMpPkHlVEavkrz8atzgOxVSRgZPkGHYH-e1-8%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Ftiny-people-testing-quality-assurance-in-software-gm1273058761-375129817&docid=sq7JjeJRPgimeM&tbnid=8F9ehayUEJET3M&vet=12ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA..i&w=612&h=430&hcb=2&ved=2ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA"},
    {"name": "1 Math Simulation Test", "price": "$6.99", "description": "A full BCA Math Simulation Test with answer key.", "image": "https://www.google.com/imgres?q=testing%20image&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1273058761%2Fvector%2Ftiny-people-testing-quality-assurance-in-software.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DDsNlOqfMpPkHlVEavkrz8atzgOxVSRgZPkGHYH-e1-8%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Ftiny-people-testing-quality-assurance-in-software-gm1273058761-375129817&docid=sq7JjeJRPgimeM&tbnid=8F9ehayUEJET3M&vet=12ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA..i&w=612&h=430&hcb=2&ved=2ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA"},
    {"name": "5 Math Simulation Test", "price": "$29.99", "description": "5 full BCA Math Simulation Test with answer key.", "image": "https://www.google.com/imgres?q=testing%20image&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1273058761%2Fvector%2Ftiny-people-testing-quality-assurance-in-software.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DDsNlOqfMpPkHlVEavkrz8atzgOxVSRgZPkGHYH-e1-8%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Ftiny-people-testing-quality-assurance-in-software-gm1273058761-375129817&docid=sq7JjeJRPgimeM&tbnid=8F9ehayUEJET3M&vet=12ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA..i&w=612&h=430&hcb=2&ved=2ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA"},
    {"name": "1 English Simulation Essay", "price": "$6.99", "description": "A full BCA English Simulation Essay with full walkthrough.", "image": "https://www.google.com/imgres?q=testing%20image&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1273058761%2Fvector%2Ftiny-people-testing-quality-assurance-in-software.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DDsNlOqfMpPkHlVEavkrz8atzgOxVSRgZPkGHYH-e1-8%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Ftiny-people-testing-quality-assurance-in-software-gm1273058761-375129817&docid=sq7JjeJRPgimeM&tbnid=8F9ehayUEJET3M&vet=12ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA..i&w=612&h=430&hcb=2&ved=2ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA"},
    {"name": "5 English Simulation Essay", "price": "$6.99",
     "description": "5 full BCA English Simulation Essay with full walkthrough.",
     "image": "https://www.google.com/imgres?q=testing%20image&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1273058761%2Fvector%2Ftiny-people-testing-quality-assurance-in-software.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DDsNlOqfMpPkHlVEavkrz8atzgOxVSRgZPkGHYH-e1-8%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Ftiny-people-testing-quality-assurance-in-software-gm1273058761-375129817&docid=sq7JjeJRPgimeM&tbnid=8F9ehayUEJET3M&vet=12ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA..i&w=612&h=430&hcb=2&ved=2ahUKEwjm4bPwiomGAxVgFVkFHc3yAsQQM3oECBYQAA"},

]

# Shopping cart
def add_to_cart(product):
    if 'cart' not in st.session_state:
        st.session_state.cart = []
    st.session_state.cart.append(product['name'])
    st.success(f"{product['name']} added to cart!")

def show_cart():
    if 'cart' not in st.session_state or len(st.session_state.cart) == 0:
        st.write("Your cart is empty.")
    else:
        st.write("## Your Cart")
        for item in st.session_state.cart:
            st.write(f"- {item}")

# Login/Signup
def login():
    st.write("Login Page")

def signup():
    st.write("Signup Page")

# Navigation
nav_option = st.sidebar.radio("Navigation", ["Home", "About", "Products", "Cart"])

# Main content
if nav_option == "Home":
    st.title("Welcome to ACE BCA Prep")
    st.write("ACE BCA is an online educational platform helping students achieve their dream of attending Bergen County Academies by providing them practice resources, and simulation tests. We also provide live guidance from students who are currently attending BCA.")
    st.write("Browse our products and add them to your cart!")

elif nav_option == "About":
    st.title("About ACE BCA Prep")
    st.write("ACE BCA is an online educational platform dedicated to helping students prepare for the Bergen County Academies admission test. Our mission is to provide comprehensive study materials, practice resources, and live guidance to support students in achieving their goal of attending BCA.")

elif nav_option == "Products":
    st.title("Products")
    for product in products:
        st.write(f"## {product['name']}")
        st.image(product['image'], use_column_width=True)
        st.write(f"Price: {product['price']}")
        st.write(product['description'])
        add_to_cart_button = st.button("Add to Cart", key=product['name'])
        if add_to_cart_button:
            add_to_cart(product)
        st.write("---")

elif nav_option == "Cart":
    show_cart()
