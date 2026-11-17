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

async def main():
    file_url = f"file://{os.path.join(REPO_ROOT, 'services/healthcare-rcm.html')}"
    
    proc = subprocess.Popen([
        CHROME,
        "--headless",
        "--remote-debugging-port=9231",
        "--disable-gpu",
        file_url
    ])
    
    await asyncio.sleep(2)
    
    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9231/json").read())
        ws_url = tabs[0]["webSocketDebuggerUrl"]
        
        async with websockets.connect(ws_url, max_size=25*1024*1024) as ws:
            # 1. Desktop Screenshot of Desktop Mega Menu (1440x900)
            await ws.send(json.dumps({
                "id": 1,
                "method": "Emulation.setDeviceMetricsOverride",
                "params": {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False}
            }))
            await ws.recv()
            await asyncio.sleep(0.5)

            # Trigger display on services mega menu
            await ws.send(json.dumps({
                "id": 2,
                "method": "Runtime.evaluate",
                "params": {"expression": """
                var p = document.getElementById('servicesMegaMenu');
                if (p) {
                    p.classList.add('open');
                }
                """}
            }))
            await ws.recv()
            await asyncio.sleep(0.5)

            await ws.send(json.dumps({
                "id": 3,
                "method": "Page.captureScreenshot",
                "params": {"format": "png", "clip": {"x": 0, "y": 0, "width": 1440, "height": 650, "scale": 1}}
            }))
            res = json.loads(await ws.recv())
            with open(os.path.join(ARTIFACTS_DIR, "verified-rcm-mega-menu-desktop.png"), "wb") as f:
                f.write(base64.b64decode(res["result"]["data"]))
            print("Captured verified-rcm-mega-menu-desktop.png")

            # 2. Mobile Drawer Screenshot (412x915)
            await ws.send(json.dumps({
                "id": 4,
                "method": "Emulation.setDeviceMetricsOverride",
                "params": {"width": 412, "height": 915, "deviceScaleFactor": 2, "mobile": True}
            }))
            await ws.recv()
            await asyncio.sleep(0.5)

            # Open mobile menu
            await ws.send(json.dumps({
                "id": 5,
                "method": "Runtime.evaluate",
                "params": {"expression": "document.querySelector('.mobile-toggle').click();"}
            }))
            await ws.recv()
            await asyncio.sleep(0.5)

            # Click Services Accordion
            await ws.send(json.dumps({
                "id": 6,
                "method": "Runtime.evaluate",
                "params": {"expression": "document.getElementById('mobileServicesToggle').click();"}
            }))
            await ws.recv()
            await asyncio.sleep(0.5)

            # Click Healthcare RCM nested accordion
            await ws.send(json.dumps({
                "id": 7,
                "method": "Runtime.evaluate",
                "params": {"expression": "document.getElementById('toggleSubcatRCM').click();"}
            }))
            await ws.recv()
            await asyncio.sleep(0.6)

            # Scroll down slightly inside drawer to show Healthcare RCM in view
            await ws.send(json.dumps({
                "id": 8,
                "method": "Runtime.evaluate",
                "params": {"expression": "document.getElementById('mobileDrawer').scrollTop = 380;"}
            }))
            await ws.recv()
            await asyncio.sleep(0.3)

            await ws.send(json.dumps({
                "id": 9,
                "method": "Page.captureScreenshot",
                "params": {"format": "png", "clip": {"x": 0, "y": 0, "width": 412, "height": 915, "scale": 2}}
            }))
            res = json.loads(await ws.recv())
            with open(os.path.join(ARTIFACTS_DIR, "verified-rcm-mobile-drawer.png"), "wb") as f:
                f.write(base64.b64decode(res["result"]["data"]))
            print("Captured verified-rcm-mobile-drawer.png")

    finally:
        proc.kill()

if __name__ == "__main__":
    asyncio.run(main())
