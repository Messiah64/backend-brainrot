"""
Skibidi-fication 3000: The Attention Span Prosthetic
=====================================================
Hack&Roll 2026 Project - "NUS Students have a 4-second attention span. We fixed education."

Uses GPT-5-nano for ULTRA-FAST brainrot translation.
This is the turbo version optimized for speed using OpenAI's fastest model.

Technical Stack:
- GPT-5-nano: Ultra-fast Gen Z translation (0.05/1M tokens input, 0.40/1M output)
- ElevenLabs API: Adam voice (the iconic Reddit stories voice)
- MoviePy: Video composition with procedural gameplay sync
"""

import os
import re
import numpy as np
from PyPDF2 import PdfReader
from PIL import Image, ImageDraw, ImageFont
try:
    from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
except ImportError:
    from moviepy import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from openai import OpenAI
from elevenlabs import ElevenLabs


def extract_text_from_pdf(pdf_path):
    """Extract all text content from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text.strip()


def brainrot_translate_turbo(text, api_key=None):
    """
    ULTRA-FAST Gen Z brainrot translation using GPT-5-nano.

    Prompt Engineering for "Skibidi-fication 3000":
    - Translates academic concepts into "Rot Speak"
    - Optimized for viral TikTok/YouTube Shorts format
    - Maintains educational integrity while maximizing engagement

    Speed: GPT-5-nano is the fastest OpenAI model (~2-3x faster than GPT-4)
    Cost: $0.05/1M input, $0.40/1M output (cheapest in GPT-5 family)
    """
    # Initialize OpenAI client
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        client = OpenAI()  # Uses OPENAI_API_KEY environment variable

    # HACK&ROLL 2026 WINNING PROMPT
    # This prompt is engineered to create "educational brainrot" that judges will love
    instructions = """You are the "Skibidi-fication 3000" - an AI that translates boring academic content
into viral Gen Z "brainrot" while keeping it educational.

YOUR MISSION: Transform lecture notes into content that can compete with Subway Surfers for attention.

TRANSLATION RULES:
1. Start EVERY explanation with "Yo chat" or "No cap" or "Fr fr"
2. Replace technical terms with Gen Z slang BUT explain them:
   - "Algorithm" → "the speedrun strat"
   - "Optimization" → "min-maxing fr"
   - "Complexity" → "how long this takes to cook"
   - "Data structure" → "the storage setup"
   - "Function" → "the move/ability"

3. Use gaming/meme metaphors:
   - "This is OP (overpowered)"
   - "This hits different"
   - "Literally the GOAT move"
   - "We're about to pop off"
   - "This is bussin no cap"

4. Add narrative urgency:
   - "Chat is this real?"
   - "Wait this is actually insane"
   - "Bro understood the assignment"
   - "Main character energy"

5. CRITICAL: Keep the actual educational content. Don't lose accuracy.
   Example: "Yo chat, Dijkstra's algorithm is literally the GOAT for finding shortest paths.
   It's the speedrun strat where you visit each node once, no cap. Big O notation?
   That's just how long it takes to cook - in this case O(V²) if you're raw-dogging it,
   but O(E log V) with a priority queue fr fr."

6. Break complex concepts into hype moments:
   - "Okay so here's the tea..."
   - "Let me cook real quick..."
   - "This is where it gets spicy..."

7. End sections with engagement hooks:
   - "But wait, there's more..."
   - "This next part is gonna hit different..."
   - "Y'all aren't ready for this..."

TONE: Enthusiastic robot who just discovered Gen Z slang but is genuinely excited about CS/Math concepts.

OUTPUT: Pure translated text. No meta-commentary. Just the brainrot lecture. DURATION LIMIT: KEEP TO 3-5mins MAXIMUM"""

    print(f"  > Using GPT-5-nano (TURBO MODE - fastest OpenAI model)")

    # Use the Responses API for maximum speed
    response = client.responses.create(
        model="gpt-5-nano",
        reasoning={"effort": "low"},  # Fast reasoning for speed
        instructions=instructions,
        input=text
    )

    return response.output_text


def generate_tts_audio(text, output_audio_path="brainrot_audio.mp3", elevenlabs_api_key=None, openai_api_key=None):
    """
    Generate audio from text using OpenAI TTS API (faster and more reliable).
    Uses 'echo' voice which is energetic and perfect for brainrot content.
    Handles texts longer than 4096 characters by chunking and merging.
    """
    from openai import OpenAI
    from pydub import AudioSegment

    # Initialize OpenAI client with explicit API key
    api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY environment variable or pass openai_api_key parameter.")

    client = OpenAI(api_key=api_key)

    print(f"  > Using OpenAI TTS 'echo' voice (optimized for brainrot content)")

    # OpenAI TTS has a 4096 character limit, so we need to chunk if text is longer
    MAX_CHARS = 4000  # Leave some buffer

    if len(text) <= MAX_CHARS:
        # Text fits in one request
        response = client.audio.speech.create(
            model="tts-1",
            voice="echo",
            input=text,
            speed=1.1
        )
        response.stream_to_file(output_audio_path)
    else:
        # Split text into chunks at sentence boundaries
        print(f"  > Text is {len(text)} chars, splitting into chunks...")
        sentences = text.replace('!', '.').replace('?', '.').split('.')

        chunks = []
        current_chunk = ""

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            if len(current_chunk) + len(sentence) + 1 < MAX_CHARS:
                current_chunk += sentence + ". "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + ". "

        if current_chunk:
            chunks.append(current_chunk.strip())

        print(f"  > Generating {len(chunks)} audio chunks...")

        # Generate audio for each chunk
        audio_segments = []
        for i, chunk in enumerate(chunks):
            temp_file = f"temp_chunk_{i}.mp3"
            response = client.audio.speech.create(
                model="tts-1",
                voice="echo",
                input=chunk,
                speed=1.1
            )
            response.stream_to_file(temp_file)
            audio_segments.append(AudioSegment.from_mp3(temp_file))
            os.remove(temp_file)

        # Concatenate all audio segments
        print(f"  > Merging {len(audio_segments)} audio segments...")
        combined = audio_segments[0]
        for segment in audio_segments[1:]:
            combined += segment

        # Export the combined audio
        combined.export(output_audio_path, format="mp3")

    print(f"  > Audio saved to {output_audio_path}")

    return output_audio_path


def create_text_chunks(text, audio_duration, min_duration_per_chunk=0.8):
    """
    Split text into chunks for display with timing.
    OPTIMIZED: Updates text every 0.8-1.0 seconds instead of per-word for much faster rendering.

    Args:
        text: The brainrot text to display
        audio_duration: Total duration of audio in seconds
        min_duration_per_chunk: Minimum duration (in seconds) each text chunk should display

    Returns:
        List of tuples: [(text_chunk, start_time, end_time), ...]
    """
    # Split text into sentences for more natural chunking
    # Replace multiple punctuation with period for splitting
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return []

    # Calculate timing per sentence
    total_sentences = len(sentences)
    time_per_sentence = audio_duration / total_sentences if total_sentences > 0 else 0

    chunks = []
    current_time = 0.0

    # Group sentences to meet minimum duration requirement
    i = 0
    while i < len(sentences):
        chunk_sentences = [sentences[i]]
        chunk_duration = time_per_sentence
        i += 1

        # Keep adding sentences until we meet minimum duration
        while chunk_duration < min_duration_per_chunk and i < len(sentences):
            chunk_sentences.append(sentences[i])
            chunk_duration += time_per_sentence
            i += 1

        chunk_text = ". ".join(chunk_sentences) + "."
        start_time = current_time
        end_time = min(current_time + chunk_duration, audio_duration)

        chunks.append((chunk_text, start_time, end_time))
        current_time = end_time

    return chunks


def create_video_with_audio_ffmpeg(background_video_path, audio_path, brainrot_text="", output_path="output.mp4"):
    """
    ULTRA-FAST: Use FFmpeg directly for text overlays (10-100x faster than PIL per-frame rendering).
    Falls back to MoviePy if FFmpeg text rendering fails.
    """
    import subprocess
    import tempfile

    try:
        # Load the audio to get its duration
        audio_clip = AudioFileClip(audio_path)
        audio_duration = audio_clip.duration
        audio_clip.close()

        # Load video to get info
        video_clip = VideoFileClip(background_video_path)
        video_duration = video_clip.duration
        video_fps = video_clip.fps
        video_clip.close()

        # Calculate loops needed
        num_loops = int(audio_duration / video_duration) + 1

        if not brainrot_text:
            # No text - just loop video with audio
            filter_complex = f"[0:v]loop={num_loops}:size=999999:start=0,trim=duration={audio_duration}[v]"
            cmd = [
                'ffmpeg', '-i', background_video_path, '-i', audio_path,
                '-filter_complex', filter_complex,
                '-map', '[v]', '-map', '1:a',
                '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '23',
                '-c:a', 'aac', '-b:a', '192k',
                '-threads', '8', '-y', output_path
            ]
            print("  > Running FFmpeg for video loop + audio...")
            subprocess.run(cmd, check=True, capture_output=True)
            return output_path
        else:
            # FALLBACK: FFmpeg text escaping is too unreliable
            # Use MoviePy with optimized caching instead
            print(f"  > FFmpeg text rendering is unreliable - using optimized MoviePy with caching...")
            return create_video_with_audio(background_video_path, audio_path, brainrot_text, output_path)

    except Exception as e:
        print(f"  > FFmpeg failed ({e}), falling back to MoviePy...")
        return create_video_with_audio(background_video_path, audio_path, brainrot_text, output_path)


def create_video_with_audio(background_video_path, audio_path, brainrot_text="", output_path="output.mp4"):
    """
    Overlay audio and text captions onto a looping background video.
    The video will loop to match the audio duration.
    Text appears with white fill and black outline for readability.
    """
    try:
        from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
    except ImportError:
        from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

    # Load the audio to get its duration
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration

    # Load the background video
    video_clip = VideoFileClip(background_video_path)
    video_duration = video_clip.duration
    video_width, video_height = video_clip.size

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

    # Add text overlays if brainrot text is provided
    if brainrot_text:
        print("  > Adding OPTIMIZED text overlays (updates every ~1 second)...")
        text_chunks = create_text_chunks(brainrot_text, audio_duration, min_duration_per_chunk=0.8)

        # Pre-load font once (not per-frame)
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            try:
                font = ImageFont.truetype("Arial.ttf", 24)
            except:
                try:
                    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 24)
                except:
                    font = ImageFont.load_default()

        # Save reference to video with audio before creating text overlay
        base_video = final_video

        # CRITICAL OPTIMIZATION: Cache text rendering per chunk
        frame_cache = {}

        def get_text_for_time(t):
            """Find which text chunk should be displayed at this time."""
            for chunk_text, start_time, end_time in text_chunks:
                if start_time <= t < end_time:
                    return chunk_text
            return ""

        # Helper function to wrap text to fit within width
        def wrap_text(text, font, max_width, stroke_width=3):
            """Wrap text to fit within max_width, breaking at word boundaries.

            CRITICAL: Must include stroke_width in measurement to account for text outline.
            """
            words = text.split()
            lines = []
            current_line = []

            for word in words:
                test_line = ' '.join(current_line + [word])
                # Use a temporary draw object to measure WITH stroke_width
                test_draw = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
                bbox = test_draw.textbbox((0, 0), test_line, font=font, stroke_width=stroke_width)
                line_width = bbox[2] - bbox[0]

                if line_width <= max_width:
                    current_line.append(word)
                else:
                    if current_line:
                        lines.append(' '.join(current_line))
                        current_line = [word]
                    else:
                        # Single word is too long, force it
                        lines.append(word)

            if current_line:
                lines.append(' '.join(current_line))

            return lines

        # Create a function to overlay text on each frame with caching
        def make_frame(t):
            # Get the frame at time t from the base video
            frame = base_video.get_frame(t)
            current_text = get_text_for_time(t)

            if current_text:
                # Check cache first - if we've rendered this text before, reuse the overlay
                cache_key = current_text
                if cache_key not in frame_cache:
                    # Create text overlay image (only once per unique text)
                    overlay = Image.new('RGBA', (video_width, video_height), (0, 0, 0, 0))
                    draw = ImageDraw.Draw(overlay)

                    # Add horizontal padding (10% on each side = 80% usable width)
                    horizontal_padding = int(video_width * 0.1)
                    max_text_width = video_width - (2 * horizontal_padding)

                    # Wrap text to fit within bounds (with stroke width)
                    outline_width = 3
                    wrapped_lines = wrap_text(current_text, font, max_text_width, stroke_width=outline_width)

                    # Calculate total text block height
                    line_height = 30  # Approximate line height for 24pt font
                    total_text_height = len(wrapped_lines) * line_height

                    # Position text block at bottom center with vertical padding
                    y_start = video_height - total_text_height - 100

                    # Draw each line
                    for i, line in enumerate(wrapped_lines):
                        # Get line bounding box for centering (MUST include stroke_width)
                        bbox = draw.textbbox((0, 0), line, font=font, stroke_width=outline_width)
                        line_width = bbox[2] - bbox[0]

                        # Center the line horizontally
                        x = (video_width - line_width) // 2
                        y = y_start + (i * line_height)

                        # Draw black outline (stroke)
                        for adj_x in range(-outline_width, outline_width + 1):
                            for adj_y in range(-outline_width, outline_width + 1):
                                if adj_x != 0 or adj_y != 0:
                                    draw.text((x + adj_x, y + adj_y), line, font=font, fill='black')

                        # Draw white text on top
                        draw.text((x, y), line, font=font, fill='white')

                    # Cache the overlay as numpy array
                    frame_cache[cache_key] = np.array(overlay)

                # Composite cached text overlay onto frame
                overlay_array = frame_cache[cache_key]
                img = Image.fromarray(frame)
                overlay_img = Image.fromarray(overlay_array)
                img.paste(overlay_img, (0, 0), overlay_img)
                frame = np.array(img)

            return frame

        # Apply text overlay to video
        print(f"  > Applying {len(text_chunks)} text segments to video (with frame caching)...")
        from moviepy.video.VideoClip import VideoClip
        text_video = VideoClip(make_frame, duration=final_video.duration)
        text_video.fps = video_clip.fps
        text_video.audio = audio_clip
        final_video = text_video

    # Write the output file with ULTRA-FAST encoding settings
    print("  > Encoding video with ultrafast preset...")
    final_video.write_videofile(
        output_path,
        codec='libx264',
        audio_codec='aac',
        fps=video_clip.fps,
        preset='ultrafast',  # MUCH faster encoding
        threads=8,           # Use multiple CPU cores
        bitrate='3000k'      # Good quality for web
    )

    # Clean up
    video_clip.close()
    audio_clip.close()
    final_video.close()
    looped_video.close()

    return output_path


def generate_brainrot_turbo(pdf_path, background_video="subway.mp4", output_video="output.mp4",
                           openai_api_key=None, elevenlabs_api_key=None):
    """
    TURBO MODE: Generate brainrot video using GPT-5-nano for maximum speed.

    Perfect for Hack&Roll 2026 demo where you need to process PDFs in real-time.

    Args:
        pdf_path: Path to the input PDF file
        background_video: Path to background video (default: subway.mp4)
        output_video: Path for output video (default: output.mp4)
        openai_api_key: OpenAI API key (optional, can use OPENAI_API_KEY env var)
        elevenlabs_api_key: ElevenLabs API key (optional, can use ELEVENLABS_API_KEY env var)

    Returns:
        Path to the generated video file
    """
    print("SKIBIDI-FICATION 3000 - TURBO MODE ACTIVATED")
    print("=" * 60)

    print("\n[1/4] Extracting text from PDF...")
    pdf_text = extract_text_from_pdf(pdf_path)
    print(f"  > Extracted {len(pdf_text)} characters from PDF")

    print("\n[2/4] Translating to Gen Z brainrot (GPT-5-nano TURBO)...")
    brainrot_text = brainrot_translate_turbo(pdf_text, openai_api_key)
    print(f"  > Generated brainrot text ({len(brainrot_text)} characters)")
    print(f"\n  Preview:\n  {brainrot_text[:250]}...\n")

    print("\n[3/4] Generating voice narration...")
    audio_path = "brainrot_audio.mp3"
    generate_tts_audio(brainrot_text, audio_path, elevenlabs_api_key, openai_api_key)

    print("\n[4/4] Creating video with looping background and text overlays (FFmpeg ULTRA-FAST mode)...")
    output_path = create_video_with_audio_ffmpeg(background_video, audio_path, brainrot_text, output_video)

    print("\n" + "=" * 60)
    print(f"SUCCESS! BRAINROT VIDEO GENERATED: {output_path}")
    print(f"Ready for Hack&Roll 2026 demo!")
    print("=" * 60)

    return output_path


if __name__ == "__main__":
    # Example usage for Hack&Roll 2026
    import sys

    pdf_file = sys.argv[1] if len(sys.argv) > 1 else "document.pdf"

    if not os.path.exists(pdf_file):
        print(f"❌ Error: {pdf_file} not found!")
        print("Usage: python brainrot_turbo.py <pdf_file>")
        sys.exit(1)

    if not os.path.exists("subway.mp4"):
        print("⚠️  Warning: subway.mp4 not found!")
        print("Please add a background video file named 'subway.mp4'")
        sys.exit(1)

    # Generate the brainrot video using TURBO MODE
    generate_brainrot_turbo(pdf_file)
