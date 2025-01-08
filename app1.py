import streamlit as st

# Simplification function (you can enhance this with more complex rules)
def simplify_text(text):
    word_replacements = {
        "difficult": "hard",
        "utilize": "use",
        "comprehend": "understand",
        "nevertheless": "but",
        "assistance": "help"
    }
    
    words = text.split(" ")
    simplified_words = [word_replacements.get(word.lower(), word) for word in words]
    return " ".join(simplified_words)

# Main function to create the Streamlit interface
def main():
    st.title("Text Simplifier")
    
    # Input text area
    input_text = st.text_area("Enter text to simplify", "")
    
    # Simplify text button
    if st.button("Simplify Text"):
        if input_text:
            simplified = simplify_text(input_text)
            st.subheader("Simplified Text")
            st.write(simplified)
        else:
            st.error("Please enter some text.")

    # Text-to-speech functionality
    if st.button("Read Simplified Text"):
        if input_text:
            simplified = simplify_text(input_text)
            st.audio(f"data:audio/wav;base64,{text_to_speech(simplified)}")
        else:
            st.error("Please enter text to read.")
    
    # Instructions
    st.sidebar.header("How It Works")
    st.sidebar.write("""
        - *Text Input*: Type complex text _name_' is not defined
into the input box.
        - *Simplify*: Press the "Simplify Text" button to simplify the text into easier language.
        - *Text-to-Speech*: Press the "Read Simplified Text" button to hear the simplified text.
    """)

# Function to convert text to speech using a basic approach
def text_to_speech(text):
    import pyttsx3
    import tempfile
    import base64

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Save speech to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        engine.save_to_file(text, temp_file.name)
        engine.runAndWait()
        
        # Convert the file to base64
        with open(temp_file.name, "rb") as f:
            audio_data = f.read()
            base64_audio = base64.b64encode(audio_data).decode("utf-8")
            
    return base64_audio

if __name__ == "__main__":
    main()
