import streamlit as st


# Set the background color and additional styling using HTML
st.markdown(
    """
    <style>
        body {
            background-color: #3498db;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 50px;
        }
        .left-side {
            width: 50%;
            color: white;
        }
        .right-side {
            width: 50%;
            text-align: center;
            color: white;
        }
        h1 {
            font-size: 36px;
            margin-bottom: 20px;
        }
        h2 {
            font-size: 24px;
            margin-bottom: 10px;
        }
        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        li {
            margin-bottom: 5px;
        }
    </style>
    <div class="container">
    """,
    unsafe_allow_html=True
)

# Dictionary to store beauty services and their prices
service_prices = {
    "Facial": 50,
    "Haircut": 30,
    "Manicure": 20,
    "Pedicure": 25,
    "Waxing": 40,
    "Massage": 60
}

def main():
    # Right side: Welcome message
    st.markdown("<div class='right-side'>", unsafe_allow_html=True)
    st.title("Hi! Welcome to Naari Makeovers")
    st.write("We offer a wide range of beauty services to help you look and feel your best.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Left side: Beauty services and prices
    st.markdown("<div class='left-side'>", unsafe_allow_html=True)
    st.title("Naari Beauty Care")
    selected_service = st.selectbox("Select a Beauty Service:", [""] + list(service_prices.keys()))
    if selected_service:
        st.write(f"Price for {selected_service}: ${service_prices[selected_service]}")
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
