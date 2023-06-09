import streamlit as st

# Variables
filmmakers = ["Stanley Kubrick", "Alfred Hitchcock", "David Lynch", "Quentin Tarantino", "Wes Anderson",
              "Guillermo del Toro", "Akira Kurosawa", "Tim Burton", "Martin Scorsese", "Christopher Nolan"]
location_time_of_day = ["Sunrise time", "Sunset time", "Daylight duration", "Evening hours", "Nighttime hours",
                        "Twilight time", "Dawn", "Dusk"]
shot = ["Wide shot/Long shot", "Medium shot", "Close-up shot", "Extreme close-up shot", "Over-the-shoulder shot",
        "Two-shot", "Point-of-view (POV) shot", "High angle shot", "Low angle shot", "Dutch angle shot"]
dash_dash = ["4:3", "16:9", "1.85:1", "1.37:1", "2.39:1", "2:1", "1.43:1", "2.76:1"]

# Custom CSS
st.markdown(
    """
    <style>
    body {
        color: #00FF41;  /* Neon green text color */
        background-color: #000;  /* Black background color */
    }

    h1 {
        color: #FF3864;  /* Neon pink header color */
        text-align: center;
        margin-bottom: 1em;
    }

    .st-expander .st-expander-open-btn::before {
        content: "\f103";
    }

    .st-expander .st-expander-close-btn::before {
        content: "\f102";
    }

    @media (max-width: 480px) {
        .st-expander .st-expander-open-btn::before {
            content: "\f104";
        }

        .st-expander .st-expander-close-btn::before {
            content: "\f105";
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    # Add image above the title
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        st.write("")  # Empty column to center the image
    with col2:
        st.image("https://cdn.midjourney.com/274c1856-34cc-47b5-a780-0a316a4c8245/0_3.png", use_column_width=True)
    with col3:
        st.write("")  # Empty column to center the image

    # Title and description
    st.title('Cinematic Midjourney Prompt Generator')
    st.markdown('Made by Shane Fozard, June 2023')

    # Get user input or random choice
    with st.expander("Click to Expand"):
        selected_filmmaker = st.selectbox("Select a filmmaker:", filmmakers)
        scene_subject_action = st.text_input("Enter the Scene/Subject/Action: ")
        set = st.text_input("Enter the Set: ")
        selected_location_time_of_day = st.selectbox("Select a location and time of day:", location_time_of_day)
        selected_shot = st.selectbox("Select a shot type:", shot)
        selected_dash_dash = st.selectbox("Select an aspect ratio:", dash_dash)

    # Generate prompt
    if st.button('Generate Prompt'):
        prompt = f"Cinematic Still, by {selected_filmmaker}, {scene_subject_action}, {set}, {selected_location_time_of_day}, {selected_shot}, --ar{selected_dash_dash}"
        st.write(prompt)


if __name__ == "__main__":
    main()
