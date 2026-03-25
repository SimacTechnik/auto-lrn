"""LRN — Compliance školení (simac-console.lrn.com)."""

LRN_URL = "https://simac-console.lrn.com/"

TASK_INSTRUCTIONS = """
You are on the LRN compliance training platform. The user has already logged in.
Your task is to complete ALL items in the "My Queue List" (task list).

Follow these steps:

1. FIND THE TASK LIST:
   - Look for "My Queue List", "My Assignments", "To Do", or a similar list of assigned trainings
   - If you're on a dashboard, find the link to the task list

2. FOR EACH ITEM IN THE LIST:
   a) Click on the item/training to open it

   b) NAVIGATING CONTENT:
      - Click "Next", "Continue", right arrow, or similar buttons to progress
      - Read the content of each page/slide
      - If there's a video on the page, wait for it to play (watch the progress bar) or look for a "Skip"/"Next" button that activates after some time

   c) QUIZZES AND QUESTIONS:
      - Read the question carefully
      - Based on the training content, select the CORRECT answer
      - For multiple-choice questions, select the best answer
      - For true/false questions, select the correct option
      - After selecting an answer, click "Submit", "Confirm", or a similar button
      - If the answer is wrong, read the feedback and correct it

   d) INTERACTIVE SCENARIOS:
      - Read the scenario/situation
      - Choose the ethically correct/compliance answer
      - When in doubt, choose the more conservative/ethical option

   e) COMPLETION:
      - After going through all pages/slides, look for "Complete", "Finish", "Done", "Mark as Complete"
      - Confirm completion if a dialog appears

   f) RETURN TO THE LIST:
      - After completing an item, return to the task list
      - Continue with the next item

3. IMPORTANT RULES:
   - Never skip content — go through every page
   - For quizzes, prefer ethical and compliance-correct answers
   - If you get stuck, try clicking on various interactive elements on the page
   - If a popup/dialog appears, read it and respond (close, confirm)
   - Watch the training progress bar
   - After completing all items, write a summary of what was completed

4. IF YOU ENCOUNTER A PROBLEM:
   - Describe what you see on the page
   - Try alternative navigation (menu, breadcrumbs, back button)
   - If an element doesn't respond, wait a few seconds and try again
"""


class LrnPlatform:
    name = "LRN Compliance"
    description = "Compliance skoleni (simac-console.lrn.com) — vyzaduje rucni prihlaseni (SSO/AD)"
    manual_login = True
    manual_login_url = LRN_URL
    max_steps = 200

    @staticmethod
    def get_trainings():
        return [{"name": "Všechna přiřazená školení", "task": TASK_INSTRUCTIONS}]
