from dotenv import load_dotenv
load_dotenv() #import all the env variable

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Func to load google gemini model

def get_gemini_response(question,prompt):    #this will give response as sql query for the text question
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

# Func to retrieve data from sqlite

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Defining a prompt

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME,CLASS,
    SECTION \n\nFor example, \nExample 1- How many enteries of records are present?,
    the SQL comman will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2- How many students studying in AI class?,
    the SQL comman will be something like this SELECT * FROM STUDENT WHERE CLASS='AI';
    also the sql code should not have ``` in the beginning or end and sql word in output
    """
]    

## Streamlit App

st.set_page_config(page_title="Convert Text to SQL query")
st.header("Gemini App to Retriev SQL Data")

question=st.text_input("Input : ",key="input")

submit=st.button("Provide your question")

#if submit is clicked

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Sql response as")
    for row in response:
        print(row)
        st.header(row)