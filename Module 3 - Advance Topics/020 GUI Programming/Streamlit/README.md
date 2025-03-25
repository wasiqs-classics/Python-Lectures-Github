# PYTHON GUI PROGRAMMING WITH "STREAMLIT"

Below is a step-by-step, hands-on tutorial that covers the fundamentals of Streamlit—from explaining what it is to building a mini BMI calculator app. Follow along as we explore the basics, learn about key components, and create a dynamic, interactive app.

---

## 1. What Is Streamlit?

Streamlit is an open-source Python library that lets you build interactive web applications quickly and easily. It’s especially popular for data science and machine learning projects because it allows you to turn data scripts into shareable web apps with minimal effort. In essence, if you can code in Python, you can build an interactive dashboard, prototype tools, or visualize your data in real time.

---

## 2. Installation and Your First App

### **Installing Streamlit**

Before you start, make sure that you have Python installed. Then, install Streamlit via pip:

```bash
pip install streamlit
```

### **Creating a “Hello World” App**

1. Create a new Python file (for example, `app.py`).
2. Open it in your favorite editor and type the following code:

   ```python
   import streamlit as st

   # Set the title of the app
   st.title("Hello, Streamlit!")

   # Write some text on the page
   st.write("This is your first Streamlit app. Enjoy the simplicity!")
   ```

3. Run your app in the command line:

   ```bash
   streamlit run app.py
   ```

This will launch your default browser and open your new web app.

---

## 3. Working with Text and Media

### **Text Features**

Streamlit offers different functions to display text in various styles:

- **Titles and Headers**:  
  ```python
  st.title("This is a Title")
  st.header("This is a Header")
  st.subheader("This is a Subheader")
  ```

- **Plain Text and Markdown**:  
  ```python
  st.text("This is plain text.")
  st.write("You can also use **Markdown** with st.write for formatting!")
  ```

### **Media Features**

Besides text, you can add images, audio, and video to enrich your app.

- **Images**:
  
  ```python
  st.image("https://via.placeholder.com/300", caption="Sample Image", use_column_width=True)
  ```

- **Videos**:
  
  ```python
  st.video("https://www.youtube.com/watch?v=your_video_id")
  ```

- **Audio**:
  
  ```python
  st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
  ```

In these examples, Streamlit automatically handles the media display to ensure everything looks neat and professional.

---

## 4. File Processing

Streamlit makes file processing very user-friendly with interactive widgets such as file uploaders.

- **Uploading Files**:  
  Use the file uploader widget to allow users to select a file from their computer.

  ```python
  uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
  if uploaded_file is not None:
      # If a file is uploaded, read it using pandas
      import pandas as pd
      df = pd.read_csv(uploaded_file)
      st.write("Data from the CSV file:", df)
  ```

This snippet lets a user upload a CSV file and then displays its content in a table.

---

## 5. Data Representations: DataFrames and Charts

### **Working with DataFrames**

You can easily display tabular data:

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)
st.dataframe(df)
```

### **Displaying Charts**

Streamlit integrates well with plotting libraries. For example, here’s how to create a simple line chart:

```python
import numpy as np

chart_data = np.random.randn(20, 3)
st.line_chart(chart_data)
```

Or, if you prefer using Matplotlib for a custom plot:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
st.pyplot(fig)
```

Both methods allow you to visualize data interactively.

---

## 6. State Management and Dynamic Data Handling

Interactive apps often need to handle user inputs and states dynamically. Streamlit provides state management through the `st.session_state` dictionary. For example, let’s create a simple counter:

```python
import streamlit as st

# Initialize a value in the session state if it doesn't exist
if "count" not in st.session_state:
    st.session_state.count = 0

def increment():
    st.session_state.count += 1

st.button("Increment", on_click=increment)
st.write(f"Counter: {st.session_state.count}")
```

This code remembers the count even as users interact with the app, making it dynamic and responsive.

---

## 7. Example: Building a BMI Calculator

Let’s bring everything together by building a simple BMI (Body Mass Index) calculator.

### **Step-by-Step BMI Calculator**

1. **User Inputs**: We need fields for weight (in kilograms) and height (in meters).  
2. **Calculation Logic**: BMI is calculated as weight divided by the square of height.  
3. **Display the Result**: Show the BMI and optionally add an interpretation of the result.

Here’s the complete code:

```python
import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Description
st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")

# User inputs for weight and height
weight = st.number_input("Enter your weight in kg:", min_value=1.0, step=0.1)
height = st.number_input("Enter your height in meters:", min_value=0.1, step=0.01)

# Adding a button that performs the calculation
if st.button("Calculate BMI"):
    # Ensure height is not zero to avoid division errors
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
        
        # Providing a simple categorization
        if bmi < 18.5:
            st.write("You are considered underweight.")
        elif 18.5 <= bmi < 25:
            st.write("You have a normal body weight.")
        elif 25 <= bmi < 30:
            st.write("You are considered overweight.")
        else:
            st.write("You are considered obese.")
    else:
        st.error("Please enter a valid height greater than 0.")
```

### **Explanation of the Code:**

- **Title and Description**:  
  `st.title()` and `st.write()` introduce and explain the app.
  
- **User Inputs**:  
  `st.number_input()` creates number fields where users enter their weight and height. Minimum values are set to avoid non-sensible input.

- **Button and Logic**:  
  The BMI calculation occurs only when the user clicks the "Calculate BMI" button. This ensures the app remains interactive.

- **Result Display and Categorization**:  
  Once calculated, the BMI value is displayed, and simple conditions provide feedback on the user’s BMI category.

To run this app, save it as `bmi_calculator.py` and run:

```bash
streamlit run bmi_calculator.py
```

---

## Wrapping Up

In this tutorial, you learned:

- **What Streamlit is and its purpose:** Building interactive, data-driven apps with minimal code.
- **How to install and set up your first app:** Using a “Hello World” example.
- **Text and media features:** Displaying text, images, videos, and audio.
- **File processing:** Uploading and reading files such as CSVs.
- **Displaying data:** Working with DataFrames and charts to visualize information.
- **State management:** Handling dynamic behavior within your app.
- **Building a complete BMI calculator:** Bringing all these elements together to create a functional application.

I encourage you to experiment further—try adding more interactivity (maybe integrate a Plotly chart to visualize BMI ranges, or add more input validations). Every new feature builds your understanding and creativity with Streamlit.

Happy coding, and enjoy exploring its endless possibilities!