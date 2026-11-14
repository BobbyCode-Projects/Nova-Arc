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

async def capture_clean_views():
    file_url = f"file://{os.path.join(REPO_ROOT, 'index.html')}"
    
    # 1. Desktop Footer (Separate process for 100% clean state)
    proc1 = subprocess.Popen([
        CHROME,
        "--headless",
        "--remote-debugging-port=9232",
        "--disable-gpu",
        file_url
    ])
    await asyncio.sleep(2)
    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9232/json").read())
        ws_url = tabs[0]["webSocketDebuggerUrl"]
        async with websockets.connect(ws_url, max_size=25*1024*1024) as ws:
            await ws.send(json.dumps({"id": 1, "method": "Emulation.setDeviceMetricsOverride", "params": {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False}}))
            await ws.recv()
            await asyncio.sleep(0.3)
            
            # Scroll footer into view
            await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {"expression": "document.querySelector('.site-footer').scrollIntoView();"}}))
            await ws.recv()
            await asyncio.sleep(0.5)
            
            await ws.send(json.dumps({"id": 3, "method": "Page.captureScreenshot", "params": {"format": "png"}}))
            resp = json.loads(await ws.recv())
            with open(os.path.join(ARTIFACTS_DIR, "verified-desktop-footer-clean.png"), "wb") as f:
                f.write(base64.b64decode(resp["result"]["data"]))
            print("Captured: verified-desktop-footer-clean.png")
    finally:
        proc1.kill()

    # 2. Mobile Header & Mobile Drawer (Separate process)
    proc2 = subprocess.Popen([
        CHROME,
        "--headless",
        "--remote-debugging-port=9233",
        "--disable-gpu",
        file_url
    ])
    await asyncio.sleep(2)
    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9233/json").read())
        ws_url = tabs[0]["webSocketDebuggerUrl"]
        async with websockets.connect(ws_url, max_size=25*1024*1024) as ws:
            await ws.send(json.dumps({"id": 1, "method": "Emulation.setDeviceMetricsOverride", "params": {"width": 412, "height": 915, "deviceScaleFactor": 2, "mobile": True}}))
            await ws.recv()
            await asyncio.sleep(0.5)
            
            # Mobile Header
            await ws.send(json.dumps({"id": 2, "method": "Page.captureScreenshot", "params": {"format": "png", "clip": {"x": 0, "y": 0, "width": 412, "height": 100, "scale": 2}}}))
            resp = json.loads(await ws.recv())
            with open(os.path.join(ARTIFACTS_DIR, "verified-mobile-navbar-clean.png"), "wb") as f:
                f.write(base64.b64decode(resp["result"]["data"]))
            print("Captured: verified-mobile-navbar-clean.png")
            
            # Click mobile toggle
            await ws.send(json.dumps({"id": 3, "method": "Runtime.evaluate", "params": {"expression": "document.querySelector('.mobile-toggle').click();"}}))
            await ws.recv()
            await asyncio.sleep(0.5)
            
            # Drawer topbar
            await ws.send(json.dumps({"id": 4, "method": "Page.captureScreenshot", "params": {"format": "png", "clip": {"x": 0, "y": 0, "width": 412, "height": 200, "scale": 2}}}))
            resp = json.loads(await ws.recv())
            with open(os.path.join(ARTIFACTS_DIR, "verified-mobile-drawer-clean.png"), "wb") as f:
                f.write(base64.b64decode(resp["result"]["data"]))
            print("Captured: verified-mobile-drawer-clean.png")
    finally:
        proc2.kill()

if __name__ == "__main__":
    asyncio.run(capture_clean_views())
