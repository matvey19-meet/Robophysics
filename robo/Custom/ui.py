
import streamlit as st
import cv2
import matplotlib.pyplot as plt
import numpy as np
import opencv
import multiprocessing


st.title("ARDC calc")
uploaded_file= st.file_uploader("Choose track",["jpg","jpeg","png"])
st.write("Or")
user_default= st.checkbox('Use demo file')

opencv_image=None
algo_choice_lqr="None"



st.sidebar.subheader("Options")
algo_planning_choice=st.sidebar.selectbox("Choose planning algorythm",("RTT*","A*"))

algo_tracking_choice=st.sidebar.selectbox(
        "Choose tracking algorythm",
        ("LQR Speed & Steer", "LQR Steer")
    )   


if user_default:
    opencv_image=cv2.imread("path.jpeg")
    file_bytes="path.jpeg"
    st.image(opencv_image)
elif uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    st.image(opencv_image)


if st.sidebar.button("Calculate"):
    st.sidebar.markdown("You selected "+algo_planning_choice+" and "+algo_tracking_choice)
    
    opencv.main(file_bytes,opencv_image)
    st.image("track_finished.jpeg")



