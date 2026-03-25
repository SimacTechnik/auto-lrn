"""LLM provider factory — priorita: Azure > Gemini > Claude."""

import os


def create_llm():
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_key = os.getenv("AZURE_OPENAI_KEY")
    azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    google_key = os.getenv("GOOGLE_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")

    if azure_endpoint and azure_key:
        from browser_use.llm.azure.chat import ChatAzureOpenAI
        print(f"LLM: Azure OpenAI ({azure_deployment})")
        return ChatAzureOpenAI(
            model=azure_deployment or "gpt-5-mini",
            api_key=azure_key,
            azure_endpoint=azure_endpoint,
            azure_deployment=azure_deployment,
        )

    if google_key and google_key != "TVUJ-GOOGLE-API-KLIC-ZDE":
        from browser_use.llm.google.chat import ChatGoogle
        print("LLM: Gemini 2.5 Flash")
        return ChatGoogle(
            model="gemini-2.5-flash",
            api_key=google_key,
        )

    if anthropic_key and anthropic_key != "sk-ant-TVUJ-KLIC-ZDE":
        from browser_use import ChatAnthropic
        print("LLM: Claude Sonnet")
        return ChatAnthropic(
            model="claude-sonnet-4-6",
            api_key=anthropic_key,
            max_tokens=4096,
        )

    print("=" * 60)
    print("CHYBA: Nastav API klic v souboru .env")
    print()
    print("Moznost 1 - Azure OpenAI (firemni billing):")
    print("  AZURE_OPENAI_ENDPOINT=https://...")
    print("  AZURE_OPENAI_KEY=...")
    print("  AZURE_OPENAI_DEPLOYMENT=gpt-5-mini")
    print()
    print("Moznost 2 - Gemini: GOOGLE_API_KEY=...")
    print("Moznost 3 - Claude: ANTHROPIC_API_KEY=...")
    print("=" * 60)
    return None
