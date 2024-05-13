import streamlit as st
# image
st.image("Automation Edge.jpeg")

# title
st.title("Welcome to AutomationEdge")
#header
st.header("We created Hyperautomation solutions, so you don’t have to")

# Subheader
st.subheader("We’re accelerating our customer’s automation journey by providing access to industry-specific automation solutions")

# Info
st.info("AutomationEdge is a powerful RPA tool to automate IT and business processes with AI-powered automation tool. It helped us reduce TAT for multiple IT processes such as User ID creation , password reset for Active directory & email system with added IT security. At the same time, there are no SLA breach now…")


# warning message
st.warning("Dont just learn Earn also......join Automation")

# Error
st.error("RPA Error")

# Sucess Message
st.success("Congrats You have Visited Automation Edge")

# Markdown
st.markdown("## Don’t see what you need in our ready solutions? Build your own ")

# text
st.text("You can build your own solution with our low-code platforms: DocEdge for intelligent document processing,CogniBot for Conversational Al and RPA for automation of repetitive processes")

# st.caption
st.caption("Caption here for Automation")

# latex
st.latex(r'''a^2 + b^2+2ab''')

# Widget
# checkbox
st.checkbox("Login")

# button
st.button("click")

# Radio
st.radio("pick your gender",["Male","Female","Other"])

# selectbox
st.selectbox("Pick you Domain",["Banking","Health","IT"])

# Multiselect
st.multiselect("Choose the services",["RPA","Web Developement","HR & IT"])

# slidebar
st.select_slider("Rating",["Bad","Good","Best"])

# st.slider
st.slider("Enter your Number",0,10)

#  Number input
st.number_input("pick your number of Services")

# text_input
st.time_input("Enter Your Mail")

# date input
st.date_input("Enter your birthdate")

# time_input
st.time_input("Enter login time")

#text area
st.text_area("Trusted by companies large and small") 

# file upload
st.file_uploader("Enter your Project file")

# color_picker
st.color_picker("Pick your color")

# progress
st.progress(90)

# # spinner
# with st.spinner("Just wait for sec "):
#     t.sleep(5)

# ballon
# st.balloons()

# sidebar
st.sidebar.title("Admin Section")
st.sidebar.text_input("Enter Mail Address")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")
st.sidebar.radio("Professional Expert",["Developer","Data Scientist","Tester"])

# Data Visulization
import pandas as pd
import numpy as np
data=pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.title("bar chart")
st.bar_chart(data)
st.title("line chart")
st.line_chart(data)
st.title("Area chart")
st.area_chart(data)















