import streamlit as st
# title
st.title("Welcome to BMI calculator")
#BMI formula
#weight input in kgs
weight : int = st.number_input("Enter weight in kgs")
#radion button to choose height format
#first one title, others are options

status = st.radio('Select your height fromat', ('cms', 'meters', 'feet'))
if status == 'cms':
    #takes height input in cms
    height = st.number_input("Centimeters")
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text('Enter your height')

     # takes height in meters
elif(status == 'meters'):
    height = st.number_input("Meters")
    try:
        bmi = weight / (height ** 2)
    except:
        st.text('enter your value of height')
else:
    # takes height in feet
    height = st.number_input('feet')
    # 1 meter = 3.28 feet
    try:
        bmi = weight / (((height /3.28)) ** 2)
    except:
        ('Enter your value of height')
    # check if the button is pressed or not
    # Calculate BMI when button is pressed
if st.button('Calculate BMI'):
    if height <= 0 or weight <= 0:
        st.error('Please enter valid values for weight and height.')
    else:
        if status == 'cms':
            height_m = height / 100
        elif status == 'meters':
            height_m = height
        else: # 'feet'
            height_m = height / 3.28 


        # give the interpretation of bmi index
        if bmi < 16:
            st.error('Your are extremely underweight')
        elif (bmi >= 16 and bmi < 18.5):
            st.warning("Your are underweight")
        elif (bmi >= 18.5 and bmi < 25):
            st.success('healthy')
        elif (bmi >= 25 and bmi < 30):
            st.warning("Overweight")
        elif (bmi >= 30):
            st.error("Extremely overweight")
    


       


    