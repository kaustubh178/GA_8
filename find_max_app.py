Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import streamlit as st
... 
... def find_largest(a, b, c):
...     return max(a, b, c)
... 
... def main():
...     st.title("Find the Largest Number")
... 
...     st.write("Enter three numbers:")
...     a = st.number_input("Enter the first number:")
...     b = st.number_input("Enter the second number:")
...     c = st.number_input("Enter the third number:")
... 
...     if st.button("Find Largest"):
...         largest = find_largest(a, b, c)
...         st.success(f"The largest number is: {largest}")
... 
... if __name__ == "__main__":
...     main()
