import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

st.title("🔗 MongoDB Atlas Connection")

# Input fields for URI components
username = st.text_input("Username", value="sangita")
password = st.text_input("Password", type="password", value="1234")
cluster_url = st.text_input("Cluster URL", value="cluster0.625ka1m.mongodb.net")

if st.button("Connect to MongoDB"):
    uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"

    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        st.success("✅ Pinged your deployment. Successfully connected to MongoDB!")
        
        # Optional: list databases
        st.subheader("Available Databases")
        dbs = client.list_database_names()
        st.write(dbs)

    except Exception as e:
        st.error(f"❌ Connection failed: {e}")
