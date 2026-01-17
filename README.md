# 🧠 SKIBIDI-FICATION 3000

**Hack&Roll 2026 Project** - *"NUS Students have a 4-second attention span. We fixed education."*

Upload your boring PDFs. We translate them into brainrot speak and **force you to watch** with eye-tracking. No cap, you will learn.

---

## 🎯 The Problem

Modern students have attention spans shorter than a TikTok video. Traditional lecture materials can't compete with Subway Surfers and brainrot content.

## 💡 The Solution

**Skibidi-fication 3000** transforms academic PDFs into engaging "educational brainrot" videos with:

1. **GPT-5-nano AI Translation** - Converts boring text into Gen Z slang while maintaining educational value
2. **ElevenLabs Voice Synthesis** - Uses the iconic "Adam" voice (from viral Reddit stories)
3. **Eye-Tracking Enforcement** - Uses face-api.js to detect when you're looking away
4. **Attention Lock System** - Video pauses + Vine Boom sound + Red overlay if you're not locked in

---

## 🚀 Quick Start

### Windows
```bash
start.bat
```

### Mac/Linux
```bash
chmod +x start.sh
./start.sh
```

### Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Start backend server
python backend_api.py

# Open http://localhost:8000/frontend/app.html in your browser
```

---

## 🏗️ Architecture

### Tech Stack
- **Frontend**: React (vanilla, no build step), face-api.js, HTML5 Video
- **Backend**: FastAPI (Python), MoviePy
- **AI Services**:
  - OpenAI GPT-5-nano (ultra-fast translation)
  - ElevenLabs API (text-to-speech)
- **Eye Tracking**: face-api.js with TinyFaceDetector

### System Flow
```
1. User uploads PDF → Backend API
2. Extract text from PDF (PyPDF2)
3. Translate to brainrot (GPT-5-nano)
4. Generate audio narration (ElevenLabs Adam voice)
5. Create video (MoviePy: audio + looping subway surfers)
6. Frontend eye-tracking forces engagement
```

---

## 📁 Project Structure

```
backend-brainrot/
├── backend_api.py              # FastAPI server
├── brainrot_turbo.py           # Core GPT-5-nano implementation
├── generate_brainrot.py        # Alternative GPT-4o version
├── app_turbo.py                # Standalone script runner
├── document.pdf                # Sample input PDF
├── subway.mp4                  # Background video
├── requirements.txt            # Python dependencies
├── start.bat / start.sh        # Startup scripts
├── frontend/
│   ├── app.html                # Main React application
│   ├── index.html              # Basic eye-tracker demo
│   └── models/                 # face-api.js models
├── uploads/                    # Uploaded PDFs (created at runtime)
└── outputs/                    # Generated videos (created at runtime)
```

---

## 🎨 Features

### Landing Page
- Modern gradient design
- Animated hero section
- Clear value proposition

### Upload Interface
- Drag-and-drop PDF upload
- File validation
- Progress indicators

### Processing View
- Real-time progress tracking
- Animated brain icon
- Status updates

### Video Player with Eye Tracking
- **Primary Video**: Your brainrot content
- **Webcam Feed**: Live face detection
- **Lock-In Status**: Green (locked in) / Red (not locked in)
- **Auto-Pause**: Video stops when you look away
- **Vine Boom**: Sound effect punishment for distraction
- **Red Overlay**: "LOCKED IN??" warning message
- **Statistics**: Track your look-away count

---

## 🎓 Educational Philosophy

This project satirizes while solving a real problem: **attention span erosion**. By gamifying focus and using culturally relevant "brainrot" language, we make learning competitive and engaging.

### The Translation System

Our GPT-5-nano prompt engineering creates "educational brainrot" that:
- Uses Gen Z slang ("no cap", "fr fr", "bussin")
- Maintains technical accuracy
- Adds gaming metaphors ("speedrun strat", "GOAT move")
- Creates narrative urgency ("chat is this real?")

**Example:**
```
Input:  "Dijkstra's algorithm finds the shortest path between nodes."
Output: "Yo chat, Dijkstra is literally the GOAT for finding shortest paths.
         It's the speedrun strat where you visit each node once, no cap."
```

---

## 🔧 API Endpoints

### `POST /api/upload`
Upload a PDF file for processing.

**Request:** `multipart/form-data` with PDF file
**Response:** `{ job_id, message, filename }`

### `POST /api/process/{job_id}`
Start processing an uploaded PDF.

**Response:** `{ job_id, status, video_url, message }`

### `GET /api/status/{job_id}`
Check processing status.

**Response:** `{ status, progress, video_url? }`

### `GET /api/video/{job_id}`
Download the generated brainrot video.

**Response:** Video file (mp4)

---

## 📊 Cost Analysis (Per Video)

| Service | Usage | Cost |
|---------|-------|------|
| GPT-5-nano | ~10k tokens | $0.01 |
| ElevenLabs | ~5 mins audio | $0.15 |
| **Total** | | **$0.16** |

*Ultra-affordable at scale!*

---

## 🏆 Demo Script (3 Minutes)

**[0:00-0:30] The Hook**
> "NUS students have a 4-second attention span. We can't pay attention to lectures, but we can watch 3-hour Subway Surfers compilations. So we fixed education."

**[0:30-1:00] The Demo**
1. Show landing page
2. Upload a real lecture PDF (e.g., "Algorithms Week 13")
3. Show processing animation

**[1:00-2:00] The Magic**
1. Video starts playing with brainrot narration
2. Look away → Video pauses + VINE BOOM + Red overlay "LOCKED IN??"
3. Look back → Video resumes
4. Show eye-tracking sidebar with statistics

**[2:00-2:30] The Technology**
> "We combined GPT-5-nano for ultra-fast translation, ElevenLabs for viral-quality voice, face-api.js for real-time eye tracking, and MoviePy for video composition."

**[2:30-3:00] The Impact**
> "This isn't just a meme. It's a proof of concept: education must compete with entertainment. We can't fight the attention economy—we have to join it."

---

## 🐛 Troubleshooting

### Camera not working
- Grant browser camera permissions
- Ensure no other app is using the camera
- Try a different browser (Chrome recommended)

### Face detection failing
- Ensure good lighting
- Face the camera directly
- Wait for models to load (check console)

### Video not playing
- Check that backend is running (`http://localhost:8000`)
- Verify `subway.mp4` exists in project root
- Check browser console for errors

### Processing takes too long
- GPT-5-nano should be very fast
- Check API key validity
- Monitor backend logs for errors

---

**Remember: Stay locked in. No cap.** 🔒✨
