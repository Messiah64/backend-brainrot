"""
Brainrot Video Generator
========================
Converts PDF documents into Gen Z slang "brainrot" videos with AI narration.

Uses:
- OpenAI API: To rewrite text into Gen Z slang
- ElevenLabs API: To generate audio with the iconic "Adam" voice (used in viral Reddit stories)
- MoviePy: To overlay audio on looping background video

Setup:
1. Install dependencies: pip install PyPDF2 openai elevenlabs moviepy
2. Set environment variables:
   - OPENAI_API_KEY=your_openai_key
   - ELEVENLABS_API_KEY=your_elevenlabs_key
3. Place a background video named 'subway.mp4' in the same directory

The Adam voice (pNInz6obpgDQGcFmaJgB) is the most popular ElevenLabs voice for:
- AI Reddit story narrations on TikTok
- Brainrot memes and content
- Viral scary/creepy story videos
"""

import os
from PyPDF2 import PdfReader
try:
    from moviepy.editor import VideoFileClip, AudioFileClip
except ImportError:
    # For moviepy v2.x
    from moviepy import VideoFileClip, AudioFileClip
from openai import OpenAI
from elevenlabs import ElevenLabs

def extract_text_from_pdf(pdf_path):
    """Extract all text content from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text.strip()

def rewrite_to_brainrot(text, api_key=None):
    """
    Use OpenAI to rewrite text into Gen Z slang/brainrot style.
    Set OPENAI_API_KEY environment variable or pass api_key parameter.
    """
    # Initialize OpenAI client
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        client = OpenAI()  # Uses OPENAI_API_KEY environment variable

    instructions = """You are a Gen Z translator that converts formal text into brainrot slang.
Rewrite text into Gen Z slang and brainrot style using terms like 'rizz', 'no cap',
'bussin', 'slay', 'fr fr', 'lowkey', 'highkey', 'main character energy',
'understood the assignment', etc. Make it engaging and over-the-top with Gen Z
internet culture references."""

    response = client.responses.create(
        model="gpt-4o",  # Use gpt-4o or gpt-3.5-turbo
        reasoning={"effort": "medium"},
        instructions=instructions,
        input=text
    )

    return response.output_text

def generate_tts_audio(text, output_audio_path="brainrot_audio.mp3", elevenlabs_api_key=None):
    """
    Generate audio from text using ElevenLabs API with the Adam voice.
    Adam is the iconic voice used in viral Reddit stories and brainrot content.

    Set ELEVENLABS_API_KEY environment variable or pass elevenlabs_api_key parameter.
    """
    # Initialize ElevenLabs client with explicit API key
    api_key = elevenlabs_api_key or os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise ValueError("ElevenLabs API key not found. Set ELEVENLABS_API_KEY environment variable or pass elevenlabs_api_key parameter.")

    client = ElevenLabs(api_key=api_key)

    # Adam voice ID - the most popular voice for Reddit stories and brainrot content
    ADAM_VOICE_ID = "pNInz6obpgDQGcFmaJgB"

    print(f"  > Using ElevenLabs 'Adam' voice (the iconic Reddit stories voice)")

    # Generate audio
    audio = client.text_to_speech.convert(
        text=text,
        voice_id=ADAM_VOICE_ID,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128"
    )

    # Save audio to file
    with open(output_audio_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    return output_audio_path

def create_video_with_audio(background_video_path, audio_path, output_path="output.mp4"):
    """
    Overlay audio onto a looping background video.
    The video will loop to match the audio duration.
    """
    try:
        from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
    except ImportError:
        from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips

    # Load the audio to get its duration
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration

    # Load the background video
    video_clip = VideoFileClip(background_video_path)
    video_duration = video_clip.duration

    # Calculate how many times we need to loop the video
    num_loops = int(audio_duration / video_duration) + 1

    # Create looped video by concatenating clips (MoviePy v2.x compatible)
    clips = [video_clip] * num_loops
    looped_video = concatenate_videoclips(clips)

    # Trim to match audio duration (MoviePy v2.x uses subclipped)
    try:
        final_video = looped_video.subclip(0, audio_duration)
    except AttributeError:
        final_video = looped_video.subclipped(0, audio_duration)

    # Set the audio
    final_video = final_video.with_audio(audio_clip) if hasattr(final_video, 'with_audio') else final_video.set_audio(audio_clip)

    # Write the output file
    final_video.write_videofile(
        output_path,
        codec='libx264',
        audio_codec='aac',
        fps=video_clip.fps
    )

    # Clean up
    video_clip.close()
    audio_clip.close()
    final_video.close()
    looped_video.close()

    return output_path

def generate_brainrot(pdf_path, background_video="subway.mp4", output_video="output.mp4",
                     openai_api_key=None, elevenlabs_api_key=None):
    """
    Main function to generate brainrot video from PDF.

    Args:
        pdf_path: Path to the input PDF file
        background_video: Path to background video (default: subway.mp4)
        output_video: Path for output video (default: output.mp4)
        openai_api_key: OpenAI API key (optional, can use OPENAI_API_KEY env var)
        elevenlabs_api_key: ElevenLabs API key (optional, can use ELEVENLABS_API_KEY env var)

    Returns:
        Path to the generated video file
    """
    print("Step 1: Extracting text from PDF...")
    pdf_text = extract_text_from_pdf(pdf_path)
    print(f"Extracted {len(pdf_text)} characters from PDF")

    print("\nStep 2: Rewriting text into Gen Z slang/brainrot...")
    brainrot_text = rewrite_to_brainrot(pdf_text, openai_api_key)
    print(f"Generated brainrot text ({len(brainrot_text)} characters)")
    print(f"\nPreview: {brainrot_text[:200]}...")

    print("\nStep 3: Generating audio using ElevenLabs Adam voice...")
    audio_path = "brainrot_audio.mp3"
    generate_tts_audio(brainrot_text, audio_path, elevenlabs_api_key)
    print(f"Audio saved to {audio_path}")

    print("\nStep 4: Creating video with looping background...")
    output_path = create_video_with_audio(background_video, audio_path, output_video)
    print(f"\n✅ Brainrot video generated successfully: {output_path}")

    # Optional: Clean up temporary audio file
    # os.remove(audio_path)

    return output_path

# Alternative function for Google Generative AI (Gemini)
def rewrite_to_brainrot_gemini(text, api_key=None):
    """
    Alternative implementation using Google's Gemini API.
    Uncomment and use this if you prefer Google over OpenAI.
    """
    import google.generativeai as genai

    if api_key:
        genai.configure(api_key=api_key)
    else:
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    model = genai.GenerativeModel('gemini-pro')

    prompt = f"""Rewrite the following text into Gen Z slang and brainrot style.
Use terms like 'rizz', 'no cap', 'bussin', 'slay', 'fr fr', 'lowkey', 'highkey',
'main character energy', 'understood the assignment', etc. Make it engaging and
over-the-top with Gen Z internet culture references.

Original text:
{text}

Rewritten version:"""

    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    # Example usage
    pdf_file = "example.pdf"  # Replace with your PDF path

    # Make sure subway.mp4 exists in the same directory
    if not os.path.exists("subway.mp4"):
        print("⚠️ Warning: subway.mp4 not found in current directory!")
        print("Please add a background video file named 'subway.mp4'")
    elif not os.path.exists(pdf_file):
        print(f"⚠️ Warning: {pdf_file} not found!")
        print("Please provide a valid PDF file path")
    else:
        # Generate the brainrot video
        generate_brainrot(pdf_file)
