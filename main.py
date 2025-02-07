import argparse
import asyncio
import sys
from pathlib import Path
from dormai.async_api import AsyncDormAI
from openai_wrapper import get_async_openai_client, get_async_openai_text_api


async def main():
    async with AsyncDormAI(Path("./dormai.yml")) as dormai:
        while True:
            inputs, context = await dormai.receive_event()
            if inputs is None:
                continue
            text: str = inputs.text
            prompt: str = dormai.settings["PROMPT"]
            print("Received: ", text,
                  file=sys.stderr)
            client = get_async_openai_client(dormai.settings["OPENAI_API_KEY"])
            output_text = await get_async_openai_text_api(client, prompt, text)
            print("Sending: ", output_text, "Context: ", context,
                  file=sys.stderr)
            await dormai.send_event(dormai.OutputData(text=output_text),
                                    context)


if __name__ == "__main__":
    asyncio.run(main())
