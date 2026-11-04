import re
import os

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
contact_path = os.path.join(repo_root, "contact.html")

with open(contact_path, "r", encoding="utf-8") as f:
    text = f.read()

pattern = re.compile(
    r'(?:<!--\s*={5,}\s*PAGE HERO / HEADER.*?-->\s*)?<section class="page-hero page-hero-dark">.*?</section>\s*(?:<!--\s*={5,}\s*MAIN CONTACT SECTION.*?-->\s*)?<section class="section subpage-section-light-alt" id="contact-main"[^>]*>',
    re.DOTALL
)

replacement = """<!-- ========================================================================
       MAIN CONTACT SECTION (FORM + SIDEBAR)
       ======================================================================== -->
  <section class="section subpage-section-light-alt" id="contact-main" style="background: #F8FAFC; padding-top: 104px; padding-bottom: var(--space-4xl);">"""

new_text, count = pattern.subn(replacement, text)
print(f"Substitutions made in contact.html: {count}")

if count == 1:
    with open(contact_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully updated contact.html")
else:
    print("Pattern did not match!")
