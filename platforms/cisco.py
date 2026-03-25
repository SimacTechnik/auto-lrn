"""Cisco Black Belt Collaboration — certifikační školení."""

CISCO_URL = "https://partnerlearning.cisco.com/new/ui/learner/page/1900218232916036096/Black%20Belt%20Collaboration%20Catalog"

TASK_INSTRUCTIONS = """
You are on the Cisco Partner Learning platform (partnerlearning.cisco.com).
The user has already logged in. You are on the Black Belt Collaboration Catalog page.
Your task is to complete all available/assigned Black Belt Collaboration training modules.

Follow these steps:

1. FIND TRAINING MODULES:
   - You should see a catalog of Black Belt Collaboration courses
   - Look for modules that are not yet completed (no checkmark, "Start", "Resume", "Enroll")
   - Click on the first available/incomplete module to open it

2. FOR EACH TRAINING MODULE:
   a) ENROLL if needed:
      - If you see "Enroll", "Register", or "Start" button, click it
      - Wait for the course to load

   b) NAVIGATING CONTENT:
      - Click "Next", "Continue", right arrow, "Start", or similar buttons to progress
      - Read the content of each page/slide carefully
      - If there are videos, wait for them to finish or look for a skip/next button
      - Some content may be in iframes or embedded players — interact with them
      - Go through ALL pages — do not skip any content

   c) QUIZZES AND ASSESSMENTS:
      - Read each question carefully
      - Select the CORRECT answer based on the training content
      - Topics include: Cisco Webex, Webex Calling, Webex Contact Center,
        Cisco collaboration hardware (Room Kit, Board, Desk), UCM Cloud,
        hybrid work solutions, Webex Suite, licensing, deployment models
      - For multiple-choice: select the best answer
      - Click "Submit", "Check", "Confirm", or similar to confirm your answer
      - If you get an answer wrong, read the feedback and try again
      - You may need a passing score (typically 80%) to complete

   d) COMPLETION:
      - After going through all content, look for "Complete", "Finish", "Done",
        "Mark as Complete", or a completion confirmation
      - Note any badge or certificate earned

   e) RETURN TO CATALOG:
      - After completing a module, go back to the catalog
      - Navigate to the catalog URL or click "Back", "Home", "Catalog" link
      - Continue with the next incomplete module

3. IMPORTANT RULES:
   - Never skip content — go through every page
   - For quizzes, prefer answers that align with Cisco's recommended solutions
   - If a popup/dialog/cookie banner appears, close/accept it
   - Watch for progress indicators and completion status
   - Some modules may have prerequisites — skip those and come back later
   - After completing all available modules, write a summary

4. IF YOU ENCOUNTER A PROBLEM:
   - Describe what you see on the page
   - Try alternative navigation (menu, breadcrumbs, back button)
   - If an element doesn't respond, wait a few seconds and try again
   - If stuck in an iframe, try to find navigation controls within it
"""


class CiscoBlackBeltPlatform:
    name = "Cisco Black Belt Collaboration"
    description = "Black Belt Collaboration certifikace (partnerlearning.cisco.com) — rucni prihlaseni"
    manual_login = True
    manual_login_url = CISCO_URL
    max_steps = 200

    @staticmethod
    def get_trainings():
        return [{"name": "Black Belt Collaboration moduly", "task": TASK_INSTRUCTIONS}]
