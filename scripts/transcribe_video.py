"""
Batch script to transcribe all TikTok videos using OpenAI's Whisper API.

This script processes all video files in the tiktok/ directory,
skips already transcribed videos, and saves results in tiktok/transcriptions/
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, List
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configuration
VIDEO_DIRECTORY = "tiktok"
TRANSCRIPTION_DIRECTORY = "tiktok/transcriptions"
SUPPORTED_VIDEO_EXTENSIONS = [".mp4", ".mov", ".avi", ".mkv"]


def get_video_files(directory: str) -> List[Path]:
    """
    Get all video files from the specified directory.
    
    Args:
        directory: Directory to search for video files
        
    Returns:
        List of video file paths
    """
    video_dir = Path(directory)
    if not video_dir.exists():
        print(f"❌ Video directory not found: {directory}")
        return []
    
    video_files = []
    for extension in SUPPORTED_VIDEO_EXTENSIONS:
        video_files.extend(video_dir.glob(f"*{extension}"))
    
    return sorted(video_files)


def get_transcript_path(video_file: Path) -> Path:
    """
    Get the expected transcript file path for a video file.
    
    Args:
        video_file: Path to the video file
        
    Returns:
        Path where the transcript should be saved
    """
    transcript_dir = Path(TRANSCRIPTION_DIRECTORY)
    transcript_filename = f"{video_file.stem}_transcript.json"
    return transcript_dir / transcript_filename


def is_already_transcribed(video_file: Path) -> bool:
    """
    Check if a video has already been transcribed.
    
    Args:
        video_file: Path to the video file
        
    Returns:
        True if transcript already exists, False otherwise
    """
    transcript_path = get_transcript_path(video_file)
    return transcript_path.exists()


def transcribe_video(video_path: Path) -> Dict[str, Any]:
    """
    Transcribe a video file using OpenAI's Whisper API.
    
    Args:
        video_path: Path to the video file
        
    Returns:
        Dictionary containing transcription and metadata
    """
    print(f"📹 Processing: {video_path.name}")
    print(f"📁 Size: {video_path.stat().st_size / 1024 / 1024:.2f} MB")
    
    try:
        # Open and transcribe the video file
        with open(video_path, "rb") as audio_file:
            print("🎤 Sending to Whisper API...")
            
            # Call Whisper API
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
            
        print("✅ Transcription completed!")
        
        # Create result dictionary with video metadata
        result = {
            "video_file": video_path.name,
            "video_path": str(video_path.absolute()),
            "transcript": transcript.strip(),
            "word_count": len(transcript.strip().split()),
            "character_count": len(transcript.strip()),
            # Placeholder for manual stats - you can fill these later
            "video_stats": {
                "views": None,
                "likes": None,
                "comments": None,
                "shares": None,
                "saves": None,
                "video_description": None
            }
        }
        
        return result
        
    except Exception as e:
        print(f"❌ Error transcribing {video_path.name}: {str(e)}")
        raise


def save_transcription(result: Dict[str, Any], video_file: Path) -> str:
    """
    Save the transcription result to a JSON file.
    
    Args:
        result: Dictionary containing transcription and metadata
        video_file: Original video file path
        
    Returns:
        Path to the saved file
    """
    # Ensure transcription directory exists
    transcript_dir = Path(TRANSCRIPTION_DIRECTORY)
    transcript_dir.mkdir(parents=True, exist_ok=True)
    
    # Get output file path
    output_file = get_transcript_path(video_file)
    
    # Save to JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Saved: {output_file.name}")
    return str(output_file)


def main():
    """
    Main function to process all videos in the tiktok directory.
    """
    print("🚀 Starting batch video transcription...")
    print("=" * 60)
    
    # Get all video files
    video_files = get_video_files(VIDEO_DIRECTORY)
    
    if not video_files:
        print(f"📁 No video files found in '{VIDEO_DIRECTORY}' directory")
        print(f"📝 Supported formats: {', '.join(SUPPORTED_VIDEO_EXTENSIONS)}")
        return
    
    print(f"📹 Found {len(video_files)} video file(s)")
    
    # Check which videos are already transcribed
    already_transcribed = []
    to_process = []
    
    for video_file in video_files:
        if is_already_transcribed(video_file):
            already_transcribed.append(video_file)
        else:
            to_process.append(video_file)
    
    # Show status
    if already_transcribed:
        print(f"✅ Already transcribed: {len(already_transcribed)} file(s)")
        for video in already_transcribed:
            print(f"   ⏭️  {video.name}")
    
    if not to_process:
        print("🎉 All videos are already transcribed! Nothing to do.")
        return
    
    print(f"🔄 To process: {len(to_process)} file(s)")
    print("-" * 60)
    
    # Process each video
    successful = 0
    failed = 0
    
    for i, video_file in enumerate(to_process, 1):
        try:
            print(f"\n[{i}/{len(to_process)}] Processing: {video_file.name}")
            
            # Transcribe the video
            result = transcribe_video(video_file)
            
            # Save the result
            save_transcription(result, video_file)
            
            # Show preview
            preview = result['transcript'][:150] + "..." if len(result['transcript']) > 150 else result['transcript']
            print(f"📝 Preview: {preview}")
            
            successful += 1
            
        except Exception as e:
            print(f"💥 Failed to process {video_file.name}: {str(e)}")
            failed += 1
            continue
    
    # Final summary
    print("\n" + "=" * 60)
    print("🎬 BATCH PROCESSING COMPLETE!")
    print(f"✅ Successfully processed: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"⏭️  Already existed: {len(already_transcribed)}")
    print(f"📁 Transcriptions saved in: {TRANSCRIPTION_DIRECTORY}")
    
    if successful > 0:
        print("\n🎯 Next steps:")
        print("1. Add video statistics manually to the JSON files")
        print("2. Use these transcriptions to build your RAG database")


if __name__ == "__main__":
    main()
