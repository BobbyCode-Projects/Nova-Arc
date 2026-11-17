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

async def capture_hero(out_filename, is_mobile=False):
    file_url = f"file://{os.path.join(REPO_ROOT, 'index.html')}"
    port = 9240
    proc = subprocess.Popen([
        CHROME,
        "--headless",
        f"--remote-debugging-port={port}",
        "--disable-gpu",
        file_url
    ])
    
    await asyncio.sleep(2)
    try:
        tabs = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{port}/json").read())
        ws_url = tabs[0]["webSocketDebuggerUrl"]
        async with websockets.connect(ws_url, max_size=30*1024*1024) as ws:
            width = 390 if is_mobile else 1440
            height = 844 if is_mobile else 900
            
            await ws.send(json.dumps({
                "id": 1,
                "method": "Emulation.setDeviceMetricsOverride",
                "params": {
                    "width": width,
                    "height": height,
                    "deviceScaleFactor": 2,
                    "mobile": is_mobile
                }
            }))
            await ws.recv()
            await asyncio.sleep(0.5)

            # Get .hero-orchestrated-grid rect
            await ws.send(json.dumps({
                "id": 2,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": """
                    (() => {
                        const el = document.querySelector('.hero-orchestrated-content');
                        if (!el) return null;
                        const rect = el.getBoundingClientRect();
                        return {
                            x: rect.x + window.pageXOffset,
                            y: rect.y + window.pageYOffset,
                            width: rect.width,
                            height: rect.height
                        };
                    })()
                    """,
                    "returnByValue": True
                }
            }))
            res2 = json.loads(await ws.recv())
            val = res2.get("result", {}).get("result", {}).get("value")
            
            if val and val.get("height", 0) > 0:
                clip = {
                    "x": max(0, val["x"] - 20),
                    "y": max(0, val["y"] - 20),
                    "width": val["width"] + 40,
                    "height": val["height"] + 40,
                    "scale": 1
                }
                shot_params = {"format": "png", "clip": clip, "captureBeyondViewport": True}
            else:
                shot_params = {"format": "png", "captureBeyondViewport": True}

            await ws.send(json.dumps({
                "id": 3,
                "method": "Page.captureScreenshot",
                "params": shot_params
            }))
            res3 = json.loads(await ws.recv())
            data = res3["result"]["data"]
            out_path = os.path.join(ARTIFACTS_DIR, out_filename)
            with open(out_path, "wb") as f:
                f.write(base64.b64decode(data))
            print(f"[OK] Captured: {out_filename} ({len(data)} bytes b64)")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except:
            proc.kill()

async def main():
    await capture_hero("verified-hero-5pills-desktop.png", is_mobile=False)
    await asyncio.sleep(1)
    await capture_hero("verified-hero-5pills-mobile.png", is_mobile=True)

if __name__ == "__main__":
    asyncio.run(main())
