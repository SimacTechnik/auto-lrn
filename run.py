"""
Auto-LRN Training Bot
=====================
Automaticky prochází školení na různých platformách:
  1. CIVOP  — BOZP, Požární bezpečnost (app.civop.cz)
  2. LRN    — Compliance školení (simac-console.lrn.com)
  3. Cisco  — Black Belt certifikace

Použití:
  python run.py              # interaktivní výběr platformy
  python run.py civop        # přímo CIVOP
  python run.py lrn          # přímo LRN
  python run.py cisco        # přímo Cisco Black Belt
"""

import asyncio
import sys
import os
from dotenv import load_dotenv
from browser_use import Agent, Browser

load_dotenv()


def select_platform():
    from platforms import PLATFORMS

    # Argument z příkazové řádky
    if len(sys.argv) > 1:
        key = sys.argv[1].lower()
        if key in PLATFORMS:
            return PLATFORMS[key]()
        print(f"Neznama platforma: '{key}'")
        print(f"Dostupne: {', '.join(PLATFORMS.keys())}")
        sys.exit(1)

    # Interaktivní výběr
    print("=" * 60)
    print("Auto-LRN Training Bot")
    print("=" * 60)
    print()
    items = list(PLATFORMS.items())
    for i, (key, cls) in enumerate(items, 1):
        print(f"  {i}. [{key}] {cls.name} — {cls.description}")
    print()

    choice = input("Vyber platformu (cislo nebo nazev): ").strip().lower()

    # Číslo
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(items):
            return items[idx][1]()
        print("Neplatna volba.")
        sys.exit(1)

    # Název
    if choice in PLATFORMS:
        return PLATFORMS[choice]()

    print(f"Neznama platforma: '{choice}'")
    sys.exit(1)


async def run_training(platform, llm, training):
    """Spustí jedno školení v čerstvém prohlížeči."""
    browser = Browser(headless=False, highlight_elements=True)

    try:
        if platform.manual_login:
            await browser.start()
            page = await browser.get_current_page()
            await page.goto(platform.manual_login_url)
            input(f">>> Prihlas se v prohlizeci a stiskni ENTER... ")
            print()

        agent = Agent(
            task=training["task"],
            llm=llm,
            browser_session=browser,
            max_actions_per_step=3,
            use_vision=False,
        )

        return await agent.run(max_steps=platform.max_steps)

    finally:
        try:
            await browser.stop()
        except Exception:
            pass


async def main():
    from llm import create_llm

    platform = select_platform()
    llm = create_llm()
    if not llm:
        return

    trainings = platform.get_trainings()
    training_names = ", ".join(t["name"] for t in trainings)

    print()
    print("=" * 60)
    print(f"{platform.name}")
    print(f"Skoleni: {training_names}")
    print("=" * 60)
    print()

    results = {}

    for idx, training in enumerate(trainings):
        label = f"[{idx + 1}/{len(trainings)}]"
        print(f"{label} Spoustim: {training['name']}")
        print("Pro preruseni stiskni Ctrl+C")
        print()

        try:
            result = await run_training(platform, llm, training)
            results[training["name"]] = result
            print()
            print(f"{label} '{training['name']}' dokonceno.")
            print("-" * 60)
        except KeyboardInterrupt:
            print("\nPreruseno uzivatelem.")
            break
        except Exception as e:
            print(f"\nChyba pri '{training['name']}': {e}")
            import traceback
            traceback.print_exc()
            results[training["name"]] = f"CHYBA: {e}"

    print()
    print("=" * 60)
    print("HOTOVO!")
    print("=" * 60)
    for name, result in results.items():
        print(f"\n--- {name} ---")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
