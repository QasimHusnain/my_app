import streamlit as st
#title
st.title("This is Title")
#Header
st.header("This is the Header")
#subheader
st.subheader("This is subheader")
#text
st.text("This is text")
# Markdown
st.markdown(" Hello! This is markdown")
# Success
st.success("Success")
# Information
st.info("Information")
# warning
st.warning("Warning")
#Error
st.error("Error")
# Exception - This has been added later
exp = ZeroDivisionError("Trying to dvide by zero")
st.exception(exp)
# Write function.Using write function, we can also display code in coding format. This is not possible using st.text(”)
st.write(range(2,40))
st.write("Text with write")
# from PIL import Image
# img = Image.open("streamlit.png")
# st.image(img, width=200)   
# #  img.show(img)
# # Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("flow.webp")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=500)
 
# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide
if st.checkbox('See me - show/hide'):
    # display the text if the checkbox returns True value
    st.image(Image.open('file.png'), width=400)
# radio button
status : str = st.radio("Gender:",('Male','Female'))
if (status == "Male"):
    st.success("Male")
else:
    st.success("Female")

#10. Selection Box:
#You can select any one option from the select box.    

hobby : str = st.selectbox('Hobbies:',['Reading','Sports','Travelling'])
st.write('Your hobby is', hobby)

# multi select box 
# first argument takes the box title
# second argument takes the options to show
multi_select = st.multiselect('Hobbies:',
                              ['Reading','Travelling','Sports'])
count = len(multi_select)
st.write(f'You selected {count} {"hobby" if count == 1 else "hobbies"}')


