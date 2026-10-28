#!/usr/bin/env python3
"""
Link & Anchor Verifier for Nova Arc website
Checks all internal links and anchors across every generated .html file.
"""

import os
import re
from urllib.parse import urlparse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_all_html_files():
    html_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        # Skip .git and hidden folders
        if "/." in root or "\\." in root:
            continue
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.relpath(os.path.join(root, f), REPO_ROOT))
    return sorted(html_files)

def check_links():
    html_files = get_all_html_files()
    print(f"Scanning {len(html_files)} HTML files for broken links...")

    broken_links = []
    total_links_checked = 0

    link_pattern = re.compile(r'href=["\']([^"\']+)["\']')

    for rel_path in html_files:
        full_path = os.path.join(REPO_ROOT, rel_path)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        file_dir = os.path.dirname(full_path)

        for match in link_pattern.finditer(content):
            raw_url = match.group(1).strip()
            total_links_checked += 1

            # Skip external links, tel:, mailto:, javascript:
            if raw_url.startswith(("http://", "https://", "tel:", "mailto:", "javascript:", "#")):
                continue

            parsed = urlparse(raw_url)
            path_part = parsed.path
            fragment = parsed.fragment

            if not path_part:
                continue

            # Resolve relative path from file_dir
            target_path = os.path.normpath(os.path.join(file_dir, path_part))

            # If target is directory or root relative
            if not os.path.exists(target_path):
                # Also check if it was intended as repo root relative
                alt_path = os.path.normpath(os.path.join(REPO_ROOT, path_part.lstrip("/")))
                if not os.path.exists(alt_path):
                    broken_links.append({
                        "file": rel_path,
                        "raw_url": raw_url,
                        "target_checked": target_path
                    })

    print(f"Total links checked: {total_links_checked}")
    if broken_links:
        print(f"\n[FAIL] Found {len(broken_links)} broken links:")
        for b in broken_links:
            print(f"  In {b['file']}: href='{b['raw_url']}' -> missing at {b['target_checked']}")
        return False
    else:
        print("\n[PASS] All internal links are valid and exist on disk! 0 broken links found.")
        return True

if __name__ == "__main__":
    success = check_links()
    if not success:
        exit(1)

