"""
LRN Training Bot
================
Automaticky prochází compliance školení na platformě LRN (simac-console.lrn.com)
pomocí knihovny browser-use a Claude AI.

Použití:
  1. Nastav ANTHROPIC_API_KEY v souboru .env
  2. Spusť: python run_training.py
  3. Přihlas se ručně v prohlížeči (SSO/AD)
  4. Stiskni Enter v terminálu
  5. Agent převezme řízení a projde školení
"""

import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatAnthropic

load_dotenv()

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


async def main():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or api_key == "sk-ant-TVUJ-KLIC-ZDE":
        print("=" * 60)
        print("CHYBA: Nastav svuj Anthropic API klic v souboru .env")
        print()
        print("1. Jdi na: https://console.anthropic.com/settings/keys")
        print("2. Vytvor novy klic")
        print("3. Vloz ho do souboru .env jako:")
        print("   ANTHROPIC_API_KEY=sk-ant-tvuj-skutecny-klic")
        print("=" * 60)
        return

    print("=" * 60)
    print("LRN Training Bot")
    print("=" * 60)
    print()
    print(f"Oteviram prohlizec na: {LRN_URL}")
    print("Prihlas se pomoci sveho firemniho uctu (SSO/AD).")
    print()

    browser = Browser(
        headless=False,
        highlight_elements=True,
    )

    try:
        # Spust prohlizec a otevri stranku
        await browser.start()
        page = await browser.get_current_page()
        await page.goto(LRN_URL)

        input(">>> Az se prihlasis, stiskni ENTER zde pro spusteni agenta... ")
        print()
        print("Agent prebyra rizeni. Sleduj prohlizec.")
        print("Pro preruseni stiskni Ctrl+C")
        print()

        llm = ChatAnthropic(
            model="claude-sonnet-4-6",
            api_key=api_key,
            max_tokens=8192,
        )

        agent = Agent(
            task=TASK_INSTRUCTIONS,
            llm=llm,
            browser_session=browser,
            max_actions_per_step=3,
            use_vision=True,
        )

        result = await agent.run(max_steps=200)
        print()
        print("=" * 60)
        print("HOTOVO!")
        print("=" * 60)
        print(result)

    except KeyboardInterrupt:
        print("\nPreruseno uzivatelem.")
    except Exception as e:
        print(f"\nChyba: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await browser.stop()


if __name__ == "__main__":
    asyncio.run(main())
