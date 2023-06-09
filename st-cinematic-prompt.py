import streamlit as st
import random

# Variables
filmmakers = ["Stanley Kubrick", "Alfred Hitchcock", "David Lynch", "Quentin Tarantino", "Wes Anderson", "Guillermo del Toro", "Akira Kurosawa", "Tim Burton", "Martin Scorsese", "Christopher Nolan"]
location_time_of_day = ["Sunrise time", "Sunset time", "Daylight duration", "Evening hours", "Nighttime hours", "Twilight time", "Dawn", "Dusk"]
shot = ["Wide shot/Long shot", "Medium shot", "Close-up shot", "Extreme close-up shot", "Over-the-shoulder shot", "Two-shot", "Point-of-view (POV) shot", "High angle shot", "Low angle shot", "Dutch angle shot"]
dash_dash = ["4:3", "16:9", "1.85:1", "1.37:1", "2.39:1", "2:1", "1.43:1", "2.76:1"]

def main():
    st.title('Cinematic Midjourney Prompt Generator')

    # Get user input or random choice
    selected_filmmaker = st.selectbox("Select a filmmaker:", filmmakers)
    scene_subject_action = st.text_input("Enter the Scene/Subject/Action: ")
    set = st.text_input("Enter the Set: ")
    selected_location_time_of_day = st.selectbox("Select a location and time of day:", location_time_of_day)
    selected_shot = st.selectbox("Select a shot type:", shot)
    selected_dash_dash = st.selectbox("Select an aspect ratio:", dash_dash)

    # Generate prompt
    if st.button('Generate Prompt'):
        prompt = f"Cinematic Still, by {selected_filmmaker}, {scene_subject_action}, {set}, {selected_location_time_of_day}, {selected_shot}, --ar {selected_dash_dash}"
        st.write(prompt)

if __name__ == "__main__":
    main()
