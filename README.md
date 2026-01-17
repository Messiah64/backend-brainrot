# 🧠💀 Skibidi-fication 3000

> **Turn boring PDFs into viral brainrot education. No cap.**

Upload your dusty textbooks → AI translates them to Gen-Z slang → Eye-tracking forces you to actually pay attention. If TikTok and Duolingo had a baby, this would be it.

---

## 🔥 What Even Is This?

**Backend Brainrot** is an AI-powered education platform that fixes the attention span crisis:
- 📄 Upload any PDF (textbooks, research papers, your tax returns)
- 🤖 AI translates it into proper Gen-Z brainrot language
- 🎬 Generates TTS videos with meme energy
- 👁️ **Eye-tracking enforcement** - look away and the video pauses
- 🐱 Random cat/dog memes mock you when you're caught lacking

Stop pretending you can focus on boring PDFs. We make education compete with Subway Surfers.

---

## ✨ Features That Hit Different

### 👁️ Eye-Tracking Enforcement
- face-api.js detects when you're actually locked in (every 300ms)
- Look away for even a second? **Video pauses instantly**
- Red "LOCK IN BRO" overlay + random meme GIF rotation
- Vine boom sound effect for maximum psychological damage
- Green/red webcam border shows your shame in real-time
- Look-away counter to humble you

### 🎥 PDF → Brainrot Pipeline
- AI translation preserves educational value while adding slang
- ElevenLabs TTS with viral-quality voice
- Real-time progress tracking with ETA countdown
- **Triple TikTok window launcher** - scroll 3 TikToks side-by-side while waiting
- Auto-closes TikTok windows when processing completes

### 📊 Stats That Actually Matter
- Total look-away count
- Focus status (locked in vs. caught lacking)
- Live face detection status
- Your disappointment level: **visible**

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
A webcam
The ability to handle being roasted by memes
```

### Installation

```bash
# Clone this beauty
git clone https://github.com/yourusername/backend-brainrot.git
cd backend-brainrot

# Install dependencies
pip install -r requirements.txt

# Set up API keys (create .env file)
OPENAI_API_KEY=your_key_here
ELEVENLABS_API_KEY=your_key_here

# Run it
python app.py
```

Open `http://localhost:8000` and start rotting.

---

## 🎮 How to Use

1. **Upload** - Drag your PDF into the upload zone
2. **Wait** - Watch progress bar (or scroll 3 TikToks simultaneously)
3. **Lock In** - Allow webcam access when prompted
4. **Learn** - Actually pay attention or get meme-shamed

---

## 🛠️ Tech Stack

**Backend:**
- FastAPI - Web framework (speed matters when attention spans are 4 seconds)
- OpenAI API - GPT-4 for authentic Gen-Z translation
- ElevenLabs - TTS that doesn't sound like a microwave
- MoviePy - Video editing magic
- PyPDF2 - PDF text extraction

**Frontend:**
- React 18 - Single-page app vibes (one HTML file, no build tools)
- face-api.js - The snitch that rats you out
- TinyFaceDetector + FaceLandmark68Net - AI models for eye tracking

---

## 📁 Project Structure

```
backend-brainrot/
├── app.py                # FastAPI backend server
├── frontend/
│   └── app.html          # Entire frontend (React SPA)
├── meme/                 # Your personal shame collection (12 GIFs)
│   ├── dog.gif, dog1.gif, side-eye-dog-suspicious-dog.gif
│   └── cat.gif, cat-kitty.gif, haidilao-cat.gif, etc.
├── models/               # face-api.js AI models
├── uploads/              # Uploaded PDFs
├── outputs/              # Generated brainrot videos
└── requirements.txt      # Python dependencies
```

---

## 🎨 Features in Detail

### The Eye-Tracking Algorithm
- Detects face landmarks every 300ms
- Calculates horizontal eye position relative to nose center
- **Threshold:** <15px = locked in ✅ | >15px = caught lacking ❌
- Instant video pause when threshold exceeded

### Triple TikTok Window Launcher
Because one distraction isn't enough while processing:
- Opens 3 TikTok windows side-by-side (400px × 800px each)
- Pre-loaded accounts: `@cryocor`, `@orange.cat.diary100`, `@anatoxich`
- Positioned center-screen using `window.screen.availWidth/Height`
- All 3 windows auto-close when processing completes

### Meme Overlay System
When you look away:
- Random rotation of 12 elite memes (dogs + cats)
- Meme changes every 3-6 seconds (maximum psychological impact)
- Vine boom sound effect on pause
- Red overlay with "LOCK IN BRO" message

### Translation Quality
Example transformation:
```
INPUT:  "Dijkstra's algorithm finds the shortest path between nodes."

OUTPUT: "Yo chat, Dijkstra is literally the GOAT for finding shortest paths.
         It's the speedrun strat where you visit each node once, no cap.
         This algorithm is bussin fr fr."
```

Educational value: **preserved** ✅
Engagement level: **maximum** 🔥

---

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/upload` | POST | Upload PDF, returns `job_id` |
| `/api/process/{job_id}` | POST | Start processing (non-blocking) |
| `/api/status/{job_id}` | GET | Poll for status, progress, ETA |
| `/api/video/{job_id}` | GET | Stream generated video |

**Status Response:**
```json
{
  "status": "processing",
  "progress": 67,
  "step": "Generating TTS audio...",
  "eta_seconds": 23,
  "video_url": "/api/video/{job_id}"
}
```

---

## 💰 Cost Per Video

| Service | Usage | Cost |
|---------|-------|------|
| OpenAI GPT-4 | ~10k tokens | $0.03 |
| ElevenLabs TTS | ~5 mins audio | $0.15 |
| **Total** | | **~$0.18** |

Ultra-affordable at scale.

---

## 🤝 Contributing

PRs welcome, especially if you:
- Have better memes for the overlay
- Know more authentic brainrot slang
- Can make the eye-tracking even more aggressive
- Want to add more TikTok accounts to the launcher
- Have ideas for mobile support

---

## ⚠️ Disclaimer

This app will:
- ✅ Make you actually learn things
- ✅ Expose your terrible attention span
- ✅ Make studying weirdly addictive
- ❌ NOT cure your actual brain rot
- ❌ NOT help you touch grass

---

## 🎓 Educational Philosophy

This project satirizes while solving a real problem: **attention span erosion in the TikTok era**.

By gamifying focus and using culturally relevant language, we make learning competitive and engaging. Education must compete with entertainment. We can't fight the attention economy—we have to join it.

---

## 🐛 Troubleshooting

**Camera not working?**
- Grant browser camera permissions
- Ensure no other app is using your webcam
- Try Chrome (recommended)

**Face detection failing?**
- Check lighting (face-api.js needs decent light)
- Face the camera directly
- Wait for models to load (~2-3 seconds)

**Video won't play?**
- Verify backend is running at `http://localhost:8000`
- Check browser console for errors
- Ensure PDF processing completed successfully

---

## 📜 License

MIT License - Do whatever you want, just don't blame us when you start speaking exclusively in Gen-Z slang.

---

## 🙏 Credits

Built by people who understand that Gen-Z only learns things if delivered like a TikTok.

Powered by OpenAI, ElevenLabs, face-api.js, and questionable life choices.

---

**Made with 💀 and zero attention span**

*Now stop reading and start rotting.* 🔒✨
