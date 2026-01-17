"""
Skibidi-fication 3000 Backend API
==================================
FastAPI backend for processing PDFs into brainrot videos.
"""

from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import shutil
from pathlib import Path
from brainrot_turbo import generate_brainrot_turbo
import uuid
import time

app = FastAPI(title="Skibidi-fication 3000 API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directories
UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Store processing status
processing_status = {}


@app.get("/")
def root():
    return {"message": "Skibidi-fication 3000 API - Ready to cook 🔥"}


@app.post("/api/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """Upload a PDF file and start processing"""

    # Validate file type
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # Generate unique ID for this job
    job_id = str(uuid.uuid4())

    # Save uploaded file
    pdf_path = UPLOAD_DIR / f"{job_id}.pdf"
    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Initialize status
    processing_status[job_id] = {
        "status": "uploaded",
        "progress": 0,
        "filename": file.filename
    }

    return JSONResponse({
        "job_id": job_id,
        "message": "PDF uploaded successfully. Ready to skibidi-fy!",
        "filename": file.filename
    })


def process_pdf_background(job_id: str):
    """Background task for processing PDF"""

    pdf_path = UPLOAD_DIR / f"{job_id}.pdf"
    start_time = time.time()

    try:
        # Update status: Starting
        processing_status[job_id].update({
            "status": "processing",
            "progress": 5,
            "step": "🔍 Extracting text from PDF...",
            "start_time": start_time,
            "eta_seconds": 180  # Estimated 3 minutes
        })

        # Define output paths
        output_video = OUTPUT_DIR / f"{job_id}.mp4"

        # Step 1: Extract text (5-15%)
        from brainrot_turbo import extract_text_from_pdf
        processing_status[job_id].update({
            "progress": 10,
            "step": "📄 Extracting text from PDF...",
            "eta_seconds": 170
        })
        pdf_text = extract_text_from_pdf(str(pdf_path))

        # Step 2: Translate to brainrot (15-35%)
        from brainrot_turbo import brainrot_translate_turbo
        processing_status[job_id].update({
            "progress": 20,
            "step": "🔥 Translating to Gen Z brainrot (GPT-5-nano)...",
            "eta_seconds": 150
        })
        brainrot_text = brainrot_translate_turbo(pdf_text, os.getenv("OPENAI_API_KEY"))

        # Step 3: Generate audio (35-60%)
        from brainrot_turbo import generate_tts_audio
        processing_status[job_id].update({
            "progress": 40,
            "step": "🎤 Generating voice narration (OpenAI TTS)...",
            "eta_seconds": 120
        })
        audio_path = str(OUTPUT_DIR / f"{job_id}_audio.mp3")
        generate_tts_audio(brainrot_text, audio_path, None, os.getenv("OPENAI_API_KEY"))

        # Step 4: Create video (60-95%)
        from brainrot_turbo import create_video_with_audio_ffmpeg
        processing_status[job_id].update({
            "progress": 65,
            "step": "🎬 Creating video with text overlays...",
            "eta_seconds": 90
        })

        # Update progress periodically during video creation
        def update_video_progress():
            for i in range(65, 95, 5):
                if processing_status[job_id]["status"] != "processing":
                    break
                time.sleep(5)
                processing_status[job_id].update({
                    "progress": i,
                    "step": f"🎬 Rendering video... ({i}%)",
                    "eta_seconds": max(10, 90 - (i - 65))
                })

        import threading
        progress_thread = threading.Thread(target=update_video_progress)
        progress_thread.start()

        create_video_with_audio_ffmpeg(
            "subway.mp4",
            audio_path,
            brainrot_text,
            str(output_video)
        )

        # Complete
        elapsed_time = time.time() - start_time
        processing_status[job_id].update({
            "status": "completed",
            "progress": 100,
            "step": "✅ Completed!",
            "video_url": f"/api/video/{job_id}",
            "eta_seconds": 0,
            "elapsed_time": int(elapsed_time)
        })

        print(f"✅ Job {job_id} completed in {elapsed_time:.1f}s")

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"\n❌ ERROR in video processing for job {job_id}:")
        print(error_details)
        processing_status[job_id].update({
            "status": "failed",
            "error": str(e),
            "step": "❌ Failed"
        })


@app.post("/api/process/{job_id}")
async def process_pdf(job_id: str, background_tasks: BackgroundTasks):
    """Start processing the uploaded PDF (async with background task)"""

    if job_id not in processing_status:
        raise HTTPException(status_code=404, detail="Job ID not found")

    pdf_path = UPLOAD_DIR / f"{job_id}.pdf"
    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail="PDF file not found")

    # Initialize status
    processing_status[job_id].update({
        "status": "queued",
        "progress": 0,
        "step": "Starting...",
        "eta_seconds": 180
    })

    # Start background processing
    background_tasks.add_task(process_pdf_background, job_id)

    return JSONResponse({
        "job_id": job_id,
        "status": "queued",
        "message": "Processing started! Check /api/status/{job_id} for updates."
    })


@app.get("/api/status/{job_id}")
async def get_status(job_id: str):
    """Get processing status for a job"""

    if job_id not in processing_status:
        raise HTTPException(status_code=404, detail="Job ID not found")

    return JSONResponse(processing_status[job_id])


@app.get("/api/video/{job_id}")
async def get_video(job_id: str):
    """Retrieve the generated video"""

    video_path = OUTPUT_DIR / f"{job_id}.mp4"

    if not video_path.exists():
        raise HTTPException(status_code=404, detail="Video not found")

    return FileResponse(
        video_path,
        media_type="video/mp4",
        filename=f"brainrot_{job_id}.mp4"
    )


@app.delete("/api/cleanup/{job_id}")
async def cleanup(job_id: str):
    """Clean up files for a completed job"""

    pdf_path = UPLOAD_DIR / f"{job_id}.pdf"
    video_path = OUTPUT_DIR / f"{job_id}.mp4"
    audio_path = OUTPUT_DIR / f"{job_id}_audio.mp3"

    # Remove files
    if pdf_path.exists():
        pdf_path.unlink()
    if video_path.exists():
        video_path.unlink()
    if audio_path.exists():
        audio_path.unlink()

    # Remove from status
    if job_id in processing_status:
        del processing_status[job_id]

    return JSONResponse({"message": "Cleanup completed"})


# Mount frontend static files AFTER all routes
app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")
app.mount("/meme", StaticFiles(directory="meme"), name="meme")


if __name__ == "__main__":
    import uvicorn

    # Set API keys from environment
    if not os.getenv("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = "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"
    if not os.getenv("ELEVENLABS_API_KEY"):
        os.environ["ELEVENLABS_API_KEY"] = "sk_d8a8306ae597845eafb1155a962a2311111ab229dce8453e"

    print("\n" + "="*60)
    print("SKIBIDI-FICATION 3000 - SERVER STARTING")
    print("="*60)
    print(f"API Server: http://localhost:8000")
    print(f"Frontend: http://localhost:8000/frontend/app.html")
    print(f"API Docs: http://localhost:8000/docs")
    print("="*60 + "\n")

    uvicorn.run(app, host="0.0.0.0", port=8000)
