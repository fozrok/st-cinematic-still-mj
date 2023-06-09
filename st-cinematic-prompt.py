import streamlit as st

# Variables
image_types = [
    "Animation",
    "Architectural design",
    "Cartoon",
    "Ceramics",
    "Cinematic Still",
    "Comic art",
    "Digital Manipulation",
    "Epic Fantasy Art",
    "Film/Video",
    "Glass Art",
    "Hero Image",
    "Illustration",
    "Iconic Artwork",
    "Ink style",
    "Installation Art",
    "Landscape",
    "Mixed Media",
    "Neo-realism",
    "Photography",
    "Pixar",
    "Post-impressionism",
    "Poster style",
    "Realism",
    "Studio Ghibli",
    "Surrealism",
    "Textile Art",
    "Ukiyoe",
    "Visual impact",
    "Wasteland Punk",
    "Watercolor",
    "Watercolor painting",
    "Website Design",
    "Woodworking"
]

# Filmmakers
filmmakers = ["Stanley Kubrick", "Alfred Hitchcock", "David Lynch", "Quentin Tarantino", "Wes Anderson",
              "Guillermo del Toro", "Akira Kurosawa", "Tim Burton", "Martin Scorsese", "Christopher Nolan"]

# Illustrators
illustrators = [
    "Walt Disney",
    "Chuck Jones",
    "Matt Groening",
    "Hanna-Barbera",
    "Bill Watterson",
    "Tex Avery",
    "Jim Davis",
    "Charles Schulz",
    "Osamu Tezuka",
    "Hayao Miyazaki",
    "Glen Keane",
    "John Lasseter",
    "Max Fleischer",
    "Ralph Bakshi",
    "Winsor McCay",
    "Carl Barks",
    "Craig McCracken",
    "Genndy Tartakovsky",
    "Bill Hanna",
    "Joe Barbera",
    "Friz Freleng",
    "Jim Henson",
    "Shigeru Miyamoto",
    "René Goscinny",
    "Albert Uderzo"
]

comic_artists = [
    "Jack Kirby",
    "Stan Lee",
    "Will Eisner",
    "Frank Miller",
    "Alan Moore",
    "Neil Gaiman",
    "Jim Lee",
    "Todd McFarlane",
    "Frank Frazetta",
    "John Romita Sr.",
    "John Buscema",
    "Alex Ross",
    "Dave Gibbons",
    "Brian Bolland",
    "George Pérez",
    "Neal Adams",
    "Walt Simonson",
    "Mike Mignola",
    "J.H. Williams III",
    "Bernie Wrightson",
    "Joe Kubert",
    "Steve Ditko",
    "John Byrne",
    "Jim Steranko",
    "Dave McKean"
]

iconic_artists = [
    "Leonardo da Vinci",
    "Vincent van Gogh",
    "Pablo Picasso",
    "Michelangelo",
    "Rembrandt",
    "Claude Monet",
    "Salvador Dalí",
    "Frida Kahlo",
    "Georgia O'Keeffe",
    "Andy Warhol",
    "Henri Matisse",
    "Jackson Pollock",
    "Gustav Klimt",
    "Wassily Kandinsky",
    "Edgar Degas",
    "René Magritte",
    "Pierre-Auguste Renoir",
    "Marc Chagall",
    "Grant Wood",
    "Edvard Munch",
    "Diego Rivera",
    "Paul Cézanne",
    "Roy Lichtenstein",
    "Caravaggio",
    "Yayoi Kusama"
]
famous_animators = [
    "Hayao Miyazaki",
    "Walt Disney",
    "Isao Takahata",
    "Glen Keane",
    "Chuck Jones",
    "Tex Avery",
    "Satoshi Kon",
    "Nick Park",
    "John Lasseter",
    "Brad Bird",
    "Mamoru Hosoda",
    "Don Bluth",
    "Goro Miyazaki",
    "Genndy Tartakovsky",
    "Sylvain Chomet",
    "Masaaki Yuasa",
    "Laika Studios",
    "Studio Ghibli",
    "Pixar Animation Studios",
    "DreamWorks Animation",
    "Aardman Animations",
    "Blue Sky Studios",
    "Wes Anderson",
    "Makoto Shinkai",
    "Richard Williams"
]

famous_architectural_styles = [
    "Gothic Revival",
    "Art Deco",
    "Renaissance",
    "Baroque",
    "Neoclassical",
    "Bauhaus",
    "Modernism",
    "Victorian",
    "Greek Revival",
    "Romanesque",
    "Islamic Architecture",
    "Colonial Revival",
    "Palladianism",
    "International Style",
    "Futurism",
    "Postmodernism",
    "Deconstructivism",
    "Beaux-Arts",
    "Queen Anne",
    "Art Nouveau",
    "Brutalism",
    "Craftsman",
    "Tudor Revival",
    "Italianate",
    "Expressionism"
]

famous_fantasy_artists = [
    "J.R.R. Tolkien",
    "H.R. Giger",
    "Brom",
    "Frank Frazetta",
    "Brian Froud",
    "Alan Lee",
    "John Howe",
    "Frank Frazetta",
    "Chris Riddell",
    "Luis Royo",
    "Michael Whelan",
    "Boris Vallejo",
    "Stephan Martiniere",
    "Roger Dean",
    "Jasmine Becket-Griffith",
    "Kinuko Y. Craft",
    "Amy Brown",
    "Charles Vess",
    "Luis Royo",
    "Moebius",
    "Tony DiTerlizzi",
    "Jeff Easley",
    "Donato Giancola",
    "Greg Hildebrandt",
    "Jim FitzPatrick"
]

famous_installation_art_styles = [
    "Conceptual Art",
    "Land Art",
    "Environmental Art",
    "Interactive Art",
    "Site-Specific Art",
    "Light Art",
    "Street Art",
    "Sound Art",
    "Kinetic Art",
    "Sculptural Installation",
    "Performance Art",
    "Video Installation",
    "Digital Installation",
    "Mixed Media Installation",
    "Immersive Art",
    "Public Art",
    "Temporary Art",
    "Intervention Art",
    "Minimalism",
    "Abstract Expressionism",
    "Surrealism",
    "Dada",
    "Op Art",
    "Pop Art",
    "Neo-Conceptualism"
]

popular_landscape_styles = [
    "Realism",
    "Impressionism",
    "Expressionism",
    "Abstract",
    "Photorealism",
    "Romanticism",
    "Naturalism",
    "Minimalism",
    "Symbolism",
    "Post-Impressionism",
    "Fauvism",
    "Cubism",
    "Surrealism",
    "Modernism",
    "Contemporary",
    "Tonalism",
    "Luminism",
    "Hudson River School",
    "Chinese Ink Painting",
    "Japanese Ukiyo-e",
    "Plein Air",
    "Sublime",
    "Topographical",
    "Hyperrealism",
    "Constructivism"
]

famous_photography_styles = [
    "Street Photography",
    "Documentary Photography",
    "Portrait Photography",
    "Landscape Photography",
    "Fashion Photography",
    "Fine Art Photography",
    "Black and White Photography",
    "Still Life Photography",
    "Conceptual Photography",
    "Wildlife Photography",
    "Macro Photography",
    "Underwater Photography",
    "Night Photography",
    "Aerial Photography",
    "Travel Photography",
    "Sports Photography",
    "War Photography",
    "Experimental Photography",
    "Photojournalism",
    "Candid Photography",
    "Architecture Photography",
    "Astrophotography",
    "Long Exposure Photography",
    "HDR Photography",
    "Food Photography"
]

famous_watercolor_styles = [
    "Transparent Watercolor",
    "Dry Brush Watercolor",
    "Wet-on-Wet Watercolor",
    "Wet-on-Dry Watercolor",
    "Wash Watercolor",
    "Gouache Watercolor",
    "Ink and Wash Watercolor",
    "Stippling Watercolor",
    "Sgraffito Watercolor",
    "Pouring Watercolor",
    "Lifting Watercolor",
    "Splatter Watercolor",
    "Negative Painting Watercolor",
    "Granulation Watercolor",
    "Blended Watercolor",
    "Controlled Wet-in-Wet Watercolor",
    "Textured Watercolor",
    "Multimedia Watercolor",
    "Abstract Watercolor",
    "Landscape Watercolor",
    "Botanical Watercolor",
    "Portrait Watercolor",
    "Urban Sketching Watercolor",
    "Illustrative Watercolor",
    "Expressive Watercolor"
]

mood = [
    "happy",
    "excited",
    "angry",
    "sad",
    "disgusted",
    "surprised",
    "hopeful",
    "anxious",
    "elated",
    "fearful",
    "hateful",
    "moody",
    "dark",
    "brutal"
]

technical_effects = [
    "epic detail",
    "dramatic contrast",
    "octane render",
    "unreal engine 5",
    "vray",
    "dof",
    "4k",
    "8k",
    "16k",
    "32k",
    "HD"
]

shot = ["Wide shot/Long shot", "Medium shot", "Close-up shot", "Extreme close-up shot", "Over-the-shoulder shot",
        "Two-shot", "Point-of-view (POV) shot", "High angle shot", "Low angle shot", "Dutch angle shot", "Close up",
        "Full body", "Portrait", "Symmetrical", "Wide view", "Bird view", "Top view", "Up view", "Front view",
        "Headshot", "Ultrawide shot", "Extreme closeup", "Macro shot"]

lighting_styles = [
    "beautiful lighting",
    "moody lighting",
    "soft lights",
    "studio lighting",
    "dramatic lighting",
    "volumetric lighting",
    "rim light",
    "edge light",
    "back light",
    "hard light",
    "soft light",
    "morning light",
    "sun light",
    "golden hour light",
    "cold light",
    "neon light",
    "inner glow",
    "outer glow",
    "strobe light"
]

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
    st.title('Midjourney Prompt Generator')
    st.markdown('Made by Shane Fozard, June 2023')

    # Get user input or random choice in sidebar
    selected_image_type = st.sidebar.selectbox("Select a media type:", image_types)

    with st.expander("Click to Expand"):
        if selected_image_type == "Animation":
            selected_creator = st.selectbox("Select an Animator:", famous_animators)
        elif selected_image_type == "Architectural design":
            selected_creator = st.selectbox("Select an Architectural Style:", famous_architectural_styles)
        elif selected_image_type == "Epic Fantasy Art":
            selected_creator = st.selectbox("Select a Fantasy Artist:", famous_fantasy_artists)
        elif selected_image_type == "Installation Art":
            selected_creator = st.selectbox("Select an Installation Art Style:", famous_installation_art_styles)
        elif selected_image_type == "Landscape":
            selected_creator = st.selectbox("Select a Landscape Style:", popular_landscape_styles)
        elif selected_image_type == "Photography":
            selected_creator = st.selectbox("Select a Photography Style:", famous_photography_styles)
        elif selected_image_type == "Watercolor":
            selected_creator = st.selectbox("Select a Watercolor Style:", famous_watercolor_styles)
        elif selected_image_type == "Cartoon":
            selected_creator = st.selectbox("Select an illustrator:", illustrators)
        elif selected_image_type == "Comic art":
            selected_creator = st.selectbox("Select a comic artist:", comic_artists)
        elif selected_image_type == "Iconic Artwork":
            selected_creator = st.selectbox("Select an iconic artist:", iconic_artists)
        else:
            selected_creator = st.selectbox("Select a Film Director:", filmmakers)

        scene_subject_action = st.text_input("Enter the Scene/Subject/Action: ")
        set = st.text_input("Enter the Set: ")
        selected_mood = st.selectbox("Select a Mood:", mood)
        selected_technical_effect = st.selectbox("Select a Technical Effect:", technical_effects)
        selected_lighting_styles = st.selectbox("Select Lighting Style:", lighting_styles)
        selected_shot = st.selectbox("Select a shot/angle type:", shot)
        selected_dash_dash = st.selectbox("Select an aspect ratio:", dash_dash)

    # Generate prompt
    if st.button('Generate Prompt'):
        prompt = f"{selected_image_type}, by {selected_creator}, {scene_subject_action}, {set}, with a {selected_mood} mood, {selected_technical_effect}, {selected_lighting_styles}, {selected_shot}, --ar {selected_dash_dash}"
        st.write(prompt)


if __name__ == "__main__":
    main()
