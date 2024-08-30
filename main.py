import PyPDF2
from gtts import gTTS


# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)
        # Iterate through all the pages
        for page_num in range(len(reader.pages)):
            # Extract text from the page
            text += reader.pages[page_num].extract_text()
    return text


# Function to convert text to audio and save as an MP3 file
def text_to_speech(text, output_path):
    # Create a gTTS object
    tts = gTTS(text=text, lang='en', slow=False)
    # Save the audio to the specified output path
    tts.save(output_path)
    print(f"Audio saved to {output_path}")


# Main function
def pdf_to_audiobook(pdf_path, output_path):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    if text:
        # Convert text to speech and save as MP3
        text_to_speech(text, output_path)
    else:
        print("No text found in the PDF.")


# Example usage
pdf_path = "test.pdf"  # Replace with your PDF file path
output_path = "audiobook.mp3"  # Replace with your desired output path
pdf_to_audiobook(pdf_path, output_path)
