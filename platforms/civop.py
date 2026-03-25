"""CIVOP E-learning — BOZP a Požární bezpečnost."""

import os

CIVOP_URL = "https://app.civop.cz/elearning"

TASK_TEMPLATE = """
You are on the CIVOP E-learning platform (app.civop.cz/elearning).
Your task is to log in and complete the training "{training_name}".

Follow these steps:

1. LOGIN - COMPANY CREDENTIALS:
   - You should see a login form for the e-learning system
   - Enter the company login name (firemní přihlašovací jméno): simactcr
   - Enter the company password (firemní heslo): skoleni398
   - Click the login/submit button

2. SELECT GROUP:
   - After company login, you need to select a group
   - Look for and select: "STD - Zaměstnanci"
   - Click to confirm the selection

3. LOGIN - PERSONAL CREDENTIALS:
   - Enter personal login name (přihlašovací jméno / ID): ptucek
   - Enter personal password: {personal_password}
   - Click the login/submit button

4. FIND THE TRAINING:
   - After logging in, look for the training called "{training_name}"
   - Alternative names to look for: {training_aliases}
   - It may be in a list of assigned/required trainings
   - Click on it to start the training

5. GO THROUGH THE TRAINING CONTENT:
   - Read each page/slide of the training material
   - To advance to the next page, click "Další" button at the bottom of the page
   - To advance to the next chapter, click "Další kapitola" button
   - DO NOT scroll excessively — use the navigation buttons instead of scrolling
   - DO NOT click chapter overview buttons (K1, K2, K3, etc.) — use "Další kapitola" to progress sequentially
   - If there are videos, wait for them to finish or look for a skip/next button
   - Go through ALL pages — do not skip any content

6. QUIZZES AND TESTS:
   - Read each question carefully
   - Based on the training content you've read, select the CORRECT answer
   - For multiple-choice: select the best answer
   - For true/false: select the correct option
   - Click "Odeslat", "Potvrdit", "Submit", or similar to confirm your answer
   - If you get an answer wrong, read the feedback and try again
{topic_hints}

7. IMPORTANT RULES:
   - Always prefer the safe, legal, and compliant answer
   - Never skip content — go through every page
   - If a popup or dialog appears, read it and respond appropriately
   - Watch for progress indicators
   - If you encounter a "referenční číslo" (reference number) or certificate, note it down
   - After completing the training, confirm completion if prompted
   - NAVIGATION EFFICIENCY: Each chapter has multiple pages. Use "Další" to go to the next page
     and "Další kapitola" to go to the next chapter. Do not waste time scrolling — click buttons.
   - If the page seems unresponsive, wait 3-5 seconds, then try clicking the button again

8. IF YOU ENCOUNTER A PROBLEM:
   - Describe what you see on the page
   - Try alternative navigation (menu, breadcrumbs, back button)
   - If an element doesn't respond, wait a few seconds and try again
   - If the login fails, describe the error message

9. COMPLETION:
   - After finishing the training and any final test, look for a completion confirmation
   - Write a summary of the result (pass/fail, score if shown)
"""

TRAININGS = [
    {
        "name": "BOZP",
        "aliases": "BOZP, Bezpečnost a ochrana zdraví při práci, Bezpečnost práce",
        "topic_hints": (
            "   - Common topics: workplace safety, personal protective equipment (PPE/OOPP),\n"
            "     risk assessment, reporting injuries and near-misses, ergonomics,\n"
            "     employer and employee obligations, safe work procedures,\n"
            "     first aid at workplace, hazardous substances, electrical safety"
        ),
    },
    {
        "name": "Požární bezpečnost",
        "aliases": "Požární bezpečnost, Požární ochrana, PO, Požární prevence",
        "topic_hints": (
            "   - Common topics: fire prevention, fire extinguisher types and usage (ABC, CO2, foam),\n"
            "     evacuation procedures, fire alarm systems, emergency exits,\n"
            "     reporting fires, fire escape routes, fire hazards in workplace,\n"
            "     flammable materials handling, fire safety inspection, emergency phone numbers (150, 112)"
        ),
    },
]


class CivopPlatform:
    name = "CIVOP E-learning"
    description = "BOZP a Požární bezpečnost (app.civop.cz)"
    manual_login = False
    max_steps = 150

    @staticmethod
    def get_trainings():
        personal_password = os.getenv("CIVOP_PERSONAL_PASSWORD", "")
        if not personal_password:
            import getpass
            print("CIVOP osobni heslo neni nastaveno v .env")
            personal_password = getpass.getpass("Heslo: ")
            if not personal_password:
                raise SystemExit("Heslo nebylo zadano.")

        tasks = []
        for training in TRAININGS:
            task_text = TASK_TEMPLATE.format(
                training_name=training["name"],
                training_aliases=training["aliases"],
                topic_hints=training["topic_hints"],
                personal_password=personal_password,
            )
            tasks.append({"name": training["name"], "task": task_text})
        return tasks
