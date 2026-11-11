#!/usr/bin/env python3
import asyncio
import json
import os
import subprocess
import time
import urllib.request
import websockets
import base64

REPO_ROOT = "/Users/bhargav/Nova-Arc"
ARTIFACTS_DIR = "/Users/bhargav/.gemini/antigravity/brain/f636bf8f-f544-4373-841a-2418ec5a64ad"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

pages = [
    ("services/digital-commerce.html", "verified-hero-digital-commerce-desktop.png", "verified-hero-digital-commerce-mobile.png"),
    ("technology/agentic-ai.html", "verified-hero-tech-agentic-desktop.png", "verified-hero-tech-agentic-mobile.png"),
    ("industries/foodtech.html", "verified-hero-ind-foodtech-desktop.png", "verified-hero-ind-foodtech-mobile.png")
]

async def capture_page(rel_path, desk_name, mob_name):
    file_url = f"file://{os.path.join(REPO_ROOT, rel_path)}"
    
    proc = subprocess.Popen([
        CHROME,
        "--headless",
        "--remote-debugging-port=9227",
        "--disable-gpu",
        file_url
    ])
    
    await asyncio.sleep(2)
    
    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9227/json").read())
        ws_url = tabs[0]["webSocketDebuggerUrl"]
        
        async with websockets.connect(ws_url, max_size=25*1024*1024) as ws:
            # 1. Desktop Screenshot (1440x900)
            await ws.send(json.dumps({
                "id": 1,
                "method": "Emulation.setDeviceMetricsOverride",
                "params": {
                    "width": 1440,
                    "height": 900,
                    "deviceScaleFactor": 1,
                    "mobile": False
                }
            }))
            await ws.recv()
            await asyncio.sleep(0.5)
            
            await ws.send(json.dumps({
                "id": 2,
                "method": "Page.captureScreenshot",
                "params": {
                    "format": "png",
                    "clip": {
                        "x": 0, "y": 0, "width": 1440, "height": 900, "scale": 1
                    }
                }
            }))
            resp = json.loads(await ws.recv())
            b64_data = resp["result"]["data"]
            with open(os.path.join(ARTIFACTS_DIR, desk_name), "wb") as f:
                f.write(base64.b64decode(b64_data))
            print(f"Captured Desktop: {rel_path} -> {desk_name}")
            
            # 2. Mobile Screenshot (430x932) - Real mobile device emulation
            await ws.send(json.dumps({
                "id": 3,
                "method": "Emulation.setDeviceMetricsOverride",
                "params": {
                    "width": 430,
                    "height": 932,
                    "deviceScaleFactor": 2,
                    "mobile": True
                }
            }))
            await ws.recv()
            await asyncio.sleep(0.5)
            
            await ws.send(json.dumps({
                "id": 4,
                "method": "Page.captureScreenshot",
                "params": {
                    "format": "png",
                    "clip": {
                        "x": 0, "y": 0, "width": 430, "height": 932, "scale": 2
                    }
                }
            }))
            resp = json.loads(await ws.recv())
            b64_data = resp["result"]["data"]
            with open(os.path.join(ARTIFACTS_DIR, mob_name), "wb") as f:
                f.write(base64.b64decode(b64_data))
            print(f"Captured Mobile: {rel_path} -> {mob_name}")
            
    finally:
        proc.kill()
        await asyncio.sleep(0.5)

async def main():
    for rel_path, desk_name, mob_name in pages:
        await capture_page(rel_path, desk_name, mob_name)

if __name__ == "__main__":
    asyncio.run(main())
