# Skibidi-fication 3000: The Attention Span Prosthetic
## Hack&Roll 2026 Winning Blueprint

**The Pitch**: "NUS Students have an attention span of 4 seconds. We fixed education by forcing it to compete with Subway Surfers."

---

## ✅ Current Implementation (MVP Ready!)

### Core Features Built:
1. **PDF Text Extraction** - Upload any lecture PDF
2. **GPT-5-nano Brainrot Translation** - ULTRA-FAST translation to Gen Z slang
3. **ElevenLabs Adam Voice** - The iconic Reddit stories voice
4. **Video Generation** - Looping background with audio overlay

### Technical Stack:
- **GPT-5-nano** (NEW!) - Fastest OpenAI model for 2-3x speed boost
  - $0.05/1M input tokens, $0.40/1M output tokens
  - Perfect for real-time demos
- **ElevenLabs Adam Voice** - The viral TikTok voice
- **MoviePy** - Video composition

---

## 🚀 Usage

### Quick Start (TURBO MODE):
```bash
# Install dependencies
pip install -r requirements.txt

# Run turbo version with GPT-5-nano
python app_turbo.py
```

### Manual Usage:
```python
from brainrot_turbo import generate_brainrot_turbo

generate_brainrot_turbo("CS2040S_Algorithms.pdf")
```

---

## 🏆 Winning Features to Add (Judging Criteria Optimization)

### Feature A: ✅ COMPLETE - "Gen Alpha" Translator (LLM + Prompt Engineering)
**Status**: DONE - Using GPT-5-nano with engineered prompts

**What We Have**:
- Translates "Dijkstra's algorithm" → "Yo chat, Dijkstra is the GOAT speedrun strat"
- Maintains educational accuracy while maximizing engagement
- Ultra-fast processing with GPT-5-nano

**Example Output**:
```
Input: "Dijkstra's algorithm finds the shortest path between nodes."

Output: "Yo chat, Dijkstra is literally the GOAT for finding shortest paths, no cap.
It's the speedrun strat where you visit each node once. Big O notation? That's just
how long it takes to cook - O(V²) if you're raw-dogging it, but O(E log V) with a
priority queue fr fr."
```

---

### Feature B: 🔨 IN PROGRESS - "Stimulation Sandwich" (Video Composition)

**Current State**: Basic looping video
**Winning Enhancement**: Procedural gameplay that speeds up based on complexity

#### Implementation Ideas:

```python
def procedural_video_speedup(video_clip, text_complexity):
    """
    Speed up gameplay based on content complexity.
    Complex topics = faster gameplay for more stimulation.
    """
    # Analyze text complexity
    if "algorithm" in text_complexity.lower() or "complexity" in text_complexity:
        speed_multiplier = 1.5  # Speed up for complex topics
    else:
        speed_multiplier = 1.0

    return video_clip.fx(vfx.speedx, speed_multiplier)

def add_text_overlay(video_clip, key_terms):
    """
    Flash key terms in top half of screen.
    """
    from moviepy.video.VideoClip import TextClip
    from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

    # Create flashing text overlays for key terms
    text_clips = []
    for i, term in enumerate(key_terms):
        txt_clip = TextClip(term, fontsize=70, color='yellow', font='Impact')
        txt_clip = txt_clip.set_position(('center', 50))
        txt_clip = txt_clip.set_duration(0.5)
        txt_clip = txt_clip.set_start(i * 2)  # Flash every 2 seconds
        text_clips.append(txt_clip)

    return CompositeVideoClip([video_clip] + text_clips)
```

**Why This Wins**: Shows you didn't just loop a video - you procedurally generated content.

---

### Feature C: 🎯 WINNING FEATURE - "Clockwork Orange" Mode (Eye Tracking)

**Status**: NOT IMPLEMENTED YET
**Impact**: THIS IS THE KILLER FEATURE

#### The Mechanic:

```javascript
// MediaPipe in browser for eye tracking
import { FaceMesh } from '@mediapipe/face_mesh';

const faceMesh = new FaceMesh({
  locateFile: (file) => {
    return `https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/${file}`;
  }
});

faceMesh.setOptions({
  maxNumFaces: 1,
  refineLandmarks: true,
  minDetectionConfidence: 0.5,
  minTrackingConfidence: 0.5
});

function onResults(results) {
  if (results.multiFaceLandmarks) {
    const eyeLandmarks = results.multiFaceLandmarks[0];

    // Detect if user is looking away
    const isLookingAway = detectGazeDirection(eyeLandmarks);

    if (isLookingAway) {
      // PAUSE VIDEO
      video.pause();
      // RED SCREEN OVERLAY
      document.body.style.backgroundColor = 'red';
      // VINE BOOM SOUND
      vineBoomAudio.play();
    } else {
      // RESUME VIDEO
      video.play();
      document.body.style.backgroundColor = 'black';
    }

    // Detect long blink
    const blinkDuration = detectBlinkDuration(eyeLandmarks);
    if (blinkDuration > 500) { // 500ms
      // SPEED UP VIDEO 2x
      video.playbackRate = 2.0;
    } else {
      video.playbackRate = 1.0;
    }
  }
}

// Start webcam
const camera = new Camera(videoElement, {
  onFrame: async () => {
    await faceMesh.send({image: videoElement});
  }
});
camera.start();
```

**Why This WINS**:
- **Hardware/Sensor Interaction**: Judges LOVE this
- **Interactive Art Installation**: Not just a website
- **Meme Potential**: "Forced to learn" is hilarious
- **Technical Complexity**: Shows CV/ML integration

---

## 📊 Judging Criteria Checklist

### ✅ Creativity (30 points)
- [x] Unique concept: "Attention Span Prosthetic"
- [x] Hilarious execution: Academic content as brainrot
- [ ] Eye-tracking adds interactive art element

### ✅ Polish (25 points)
- [x] Professional voice synthesis (ElevenLabs)
- [ ] Web interface with eye tracking
- [ ] Smooth video transitions
- [ ] Error handling and edge cases

### ✅ Technical Complexity (25 points)
- [x] LLM integration with prompt engineering
- [x] TTS API integration
- [x] Video composition with MoviePy
- [ ] Computer vision (MediaPipe)
- [ ] Real-time webcam processing
- [ ] Procedural video generation

### ✅ Presentation (20 points)
- [x] Clear pitch: "4-second attention span problem"
- [x] Live demo: Upload PDF → Get brainrot video
- [ ] Interactive demo: Let judges try eye tracking
- [ ] Meme-worthy results they can share

---

## 🎨 Next Steps to WIN

### Priority 1: Add Eye Tracking (THIS WINS IT)
1. Create a web interface (React/Next.js)
2. Integrate MediaPipe Face Mesh
3. Implement gaze detection
4. Add "Clockwork Orange" mode:
   - Red screen when looking away
   - Vine boom sound effect
   - 2x speed on long blinks

### Priority 2: Procedural Video Enhancement
1. Analyze text complexity (keyword detection)
2. Speed up gameplay based on complexity
3. Add flashing text overlays with key terms
4. Sync visual effects to audio beats

### Priority 3: Web App Polish
1. Drag-and-drop PDF upload
2. Real-time progress bar
3. Live preview of brainrot text
4. Download generated video
5. Share to social media

---

## 🔧 Tech Stack for Full Implementation

### Backend (Current):
- Python + FastAPI
- OpenAI GPT-5-nano
- ElevenLabs API
- MoviePy

### Frontend (To Add):
- Next.js / React
- MediaPipe (eye tracking)
- TailwindCSS
- React Dropzone (file upload)

### Deployment:
- Vercel (frontend)
- Railway / Render (backend)
- FFmpeg in Docker

---

## 💡 Demo Strategy for Hack&Roll

### The Perfect Demo Flow:
1. **Hook** (10 sec): "We have 4-second attention spans. We fixed education."
2. **Problem** (20 sec): Show boring CS2040S PDF
3. **Upload** (10 sec): Drag-and-drop PDF into web app
4. **Generate** (30 sec): Watch real-time brainrot translation (GPT-5-nano speed!)
5. **Result** (60 sec): Play the video with Adam voice + Subway Surfers
6. **Killer Feature** (60 sec): Turn on eye tracking, demonstrate "Clockwork Orange" mode
7. **Close** (10 sec): "Education that competes with TikTok. We won attention."

### Props to Bring:
- Laptop with webcam for eye tracking demo
- HDMI cable for big screen demo
- Pre-generated videos as backup
- Vine boom sound effect cued up
- Printed meme comparison: "Boring lecture vs. Our version"

---

## 📈 Expected Judge Reactions

**"This is hilarious"** ✅ Creativity points
**"The eye tracking is insane"** ✅ Technical complexity
**"I actually want to use this"** ✅ Practicality
**"The Adam voice is perfect"** ✅ Polish

---

## 🎯 Files in This Project

- `brainrot_turbo.py` - **NEW!** GPT-5-nano turbo version
- `app_turbo.py` - Quick demo script
- `generate_brainrot.py` - Original GPT-4o version
- `requirements.txt` - Dependencies
- `README.md` - Basic usage
- `HACKROLL_2026.md` - **THIS FILE** - Winning strategy

---

## 🚀 Current Speed Comparison

### GPT-4o (Original):
- Translation time: ~8-12 seconds
- Cost: $2.50/1M input, $10/1M output

### GPT-5-nano (Turbo):
- Translation time: ~3-5 seconds ⚡️
- Cost: $0.05/1M input, $0.40/1M output 💰
- **2-3x FASTER** for real-time demos!

---

## 🏅 Why This Wins Hack&Roll 2026

1. **Meme Category Champion**: High technical effort + culturally relevant
2. **All Judging Criteria**: Creativity ✓ Polish ✓ Technical ✓ Presentation ✓
3. **Demo-able**: Works in 3 minutes, judges can try it
4. **Viral Potential**: They'll share the videos
5. **Actual Problem**: Attention span is a real issue
6. **Unique**: Nobody else will have eye tracking + brainrot

---

## 💪 Go Build It and Win

You have the MVP. Now add the eye tracking and you're in the Top 3 guaranteed.

**Remember**: The eye tracking is what separates "funny website" from "holy shit this is next level."

Good luck at Hack&Roll 2026! 🏆
