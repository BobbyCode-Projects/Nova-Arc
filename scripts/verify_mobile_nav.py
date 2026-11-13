#!/usr/bin/env python3
import asyncio
import json
import os
import subprocess
import urllib.request
import websockets
import base64

REPO_ROOT = "/Users/bhargav/Nova-Arc"
ARTIFACTS_DIR = "/Users/bhargav/.gemini/antigravity/brain/f636bf8f-f544-4373-841a-2418ec5a64ad"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

async def test_and_capture():
    file_url = f"file://{os.path.join(REPO_ROOT, 'services/digital-commerce.html')}"
    
    proc = subprocess.Popen([
        CHROME,
        "--headless",
        "--remote-debugging-port=9228",
        "--disable-gpu",
        file_url
    ])
    
    await asyncio.sleep(2)
    
    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9228/json").read())
        ws_url = tabs[0]["webSocketDebuggerUrl"]
        
        async with websockets.connect(ws_url, max_size=25*1024*1024) as ws:
            # Set mobile viewport 412x915 (standard modern Android/iPhone screen)
            await ws.send(json.dumps({
                "id": 1,
                "method": "Emulation.setDeviceMetricsOverride",
                "params": {
                    "width": 412,
                    "height": 915,
                    "deviceScaleFactor": 2,
                    "mobile": True
                }
            }))
            await ws.recv()
            await asyncio.sleep(0.5)
            
            # 1. Capture Hero Section (showing Discuss Your Project gap and Subtopic pills with arrows)
            await ws.send(json.dumps({
                "id": 2,
                "method": "Page.captureScreenshot",
                "params": {
                    "format": "png",
                    "clip": {
                        "x": 0, "y": 0, "width": 412, "height": 850, "scale": 2
                    }
                }
            }))
            resp = json.loads(await ws.recv())
            b64_data = resp["result"]["data"]
            with open(os.path.join(ARTIFACTS_DIR, "verified-mobile-hero-buttons-and-pills.png"), "wb") as f:
                f.write(base64.b64decode(b64_data))
            print("Captured: verified-mobile-hero-buttons-and-pills.png")
            
            # 2. Click mobile hamburger to open drawer
            await ws.send(json.dumps({
                "id": 3,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": "document.querySelector('.mobile-toggle').click();"
                }
            }))
            await ws.recv()
            await asyncio.sleep(0.5)
            
            # 3. Click Services Accordion toggle
            await ws.send(json.dumps({
                "id": 4,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": "document.getElementById('mobileServicesToggle').click();"
                }
            }))
            await ws.recv()
            await asyncio.sleep(0.5)
            
            # Capture mobile drawer with Services showing the 4 service categories
            await ws.send(json.dumps({
                "id": 5,
                "method": "Page.captureScreenshot",
                "params": {
                    "format": "png",
                    "clip": {
                        "x": 0, "y": 0, "width": 412, "height": 915, "scale": 2
                    }
                }
            }))
            resp = json.loads(await ws.recv())
            b64_data = resp["result"]["data"]
            with open(os.path.join(ARTIFACTS_DIR, "verified-mobile-services-collapsed.png"), "wb") as f:
                f.write(base64.b64decode(b64_data))
            print("Captured: verified-mobile-services-collapsed.png")
            
            # 4. Click the first nested service domain (Digital Commerce & Supply Chain)
            await ws.send(json.dumps({
                "id": 6,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": "document.getElementById('toggleSubcatDC').click();"
                }
            }))
            await ws.recv()
            await asyncio.sleep(0.5)
            
            # Capture mobile drawer with Digital Commerce subtopics expanded
            await ws.send(json.dumps({
                "id": 7,
                "method": "Page.captureScreenshot",
                "params": {
                    "format": "png",
                    "clip": {
                        "x": 0, "y": 0, "width": 412, "height": 915, "scale": 2
                    }
                }
            }))
            resp = json.loads(await ws.recv())
            b64_data = resp["result"]["data"]
            with open(os.path.join(ARTIFACTS_DIR, "verified-mobile-services-expanded.png"), "wb") as f:
                f.write(base64.b64decode(b64_data))
            print("Captured: verified-mobile-services-expanded.png")

    finally:
        proc.kill()

if __name__ == "__main__":
    asyncio.run(test_and_capture())
