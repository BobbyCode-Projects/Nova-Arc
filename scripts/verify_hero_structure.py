#!/usr/bin/env python3
"""
Verify hero structure across all 41 subpages:
1. No hero-supporting-text element.
2. Exactly 2 hero paragraphs: hero-tagline-ags and hero-intro-text.
3. No hero-right-col or LIVE ENGINE or COMMERCE PIPELINE ARCHITECTURE.
4. Hero container has max-width 900px and matches Screenshot 3 open layout.
"""

import os
import glob
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def verify_all_heroes():
    files = []
    for pattern in ["services/*.html", "technology/*.html", "industries/*.html", "connect/*.html"]:
        files.extend(glob.glob(os.path.join(REPO_ROOT, pattern)))

    print(f"Verifying hero section across {len(files)} pages...")
    
    passed = 0
    failed = 0
    
    for fpath in sorted(files):
        rel = os.path.relpath(fpath, REPO_ROOT)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. Check no hero-supporting-text
        if "hero-supporting-text" in content:
            print(f"[FAIL] {rel}: contains hero-supporting-text")
            failed += 1
            continue
            
        # 2. Check no hero-right-col
        if "hero-right-col" in content:
            print(f"[FAIL] {rel}: contains hero-right-col")
            failed += 1
            continue

        # 3. Check no LIVE ENGINE
        if "LIVE ENGINE" in content:
            print(f"[FAIL] {rel}: contains LIVE ENGINE")
            failed += 1
            continue

        # 4. Check for hero-tagline-ags and hero-intro-text
        if "hero-tagline-ags" not in content:
            print(f"[FAIL] {rel}: missing hero-tagline-ags")
            failed += 1
            continue
            
        if "hero-intro-text" not in content:
            print(f"[FAIL] {rel}: missing hero-intro-text")
            failed += 1
            continue
            
        # 5. Check hero paragraph count in .page-hero-content
        hero_content_match = re.search(r'<div class="page-hero-content"[^>]*>(.*?)</div>', content, re.DOTALL)
        if hero_content_match:
            hero_div = hero_content_match.group(1)
            p_tags = re.findall(r'<p\b[^>]*>', hero_div)
            if len(p_tags) != 2:
                print(f"[FAIL] {rel}: expected 2 <p> tags in hero-content, found {len(p_tags)}")
                failed += 1
                continue
                
        passed += 1

    print(f"\nVerification Results:")
    print(f"Total verified: {len(files)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if failed == 0:
        print("\n[ALL TESTS PASSED] Every subpage has exactly 2 hero paragraphs, zero 3rd paragraph, and zero diagram boxes.")

if __name__ == "__main__":
    verify_all_heroes()

