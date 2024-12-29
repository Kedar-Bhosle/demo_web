import streamlit as st
import pandas as pd
import os

st.title("Data View App")
st.header("Certain 100 People's Data")
st.subheader("Read the data and fill out the form")

# Define the file name
data_file = "customers-100.csv"

# Load or create the dataset
if os.path.exists(data_file):
    dataset = pd.read_csv(data_file)
else:
    # If file does not exist, create a new DataFrame with columns
    dataset = pd.DataFrame(columns=["Index", "Customer Id", "First Name", "Last Name","Company","City", "Phone 1", "Phone 2","Email","Subscription Date","Website"])
    # Display the dataset
st.dataframe(dataset)

# Form for user input
with st.form("user_form"):

    index = st.text_input("Enter your index number")
    Customer_id = st.text_input("Enter your custermer id")
    First_Name = st.text_input("Enter your first name")
    Last_name = st.text_input("Enter your Last name:")
    Company = st.text_input("Enter your company")
    City = st.text_input("Enter your city name")
    Phone_1 = st.text_input("Enter your phone 1 number")
    Phone_2 = st.text_input("Enter your phone 2 number")
    Email = st.text_input("Enter your email address")
    Subscription_Date = st.text_input("Enter your subscription date")
    Website = st.text_input("Enter your website")

    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        if not index or not Customer_id or not First_Name or not Last_name or not Email or not Subscription_Date or not Website:
            st.warning("Please fill in all fields.")
        else:
            # Append new data to the dataset
            new_data = {"Index":index, "Customer Id":Customer_id,"First Name":First_Name,"Last Name": Last_name, "Email":Email,"Subscription Date":Subscription_Date,"Website": Website}
           
           
            dataset = pd.concat([dataset, new_data], ignore_index=True)

            # Save updated dataset to CSV
            dataset.to_csv(data_file, index=False)

            st.success("Your data has been saved successfully!")

            # Display the updated dataset
            st.dataframe(dataset)

                                                                        
