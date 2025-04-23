import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=["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"],
)

# Brief delay to give you time to focus the correct window
time.sleep(2)

# Step 1: Click on the icon at (823, 739)
pyautogui.click(823, 739)
time.sleep(1)  # wait a moment after click

# Step 2: Move to (287, 115), drag to (1300, 655)
pyautogui.moveTo(287, 115, duration=0.5)
pyautogui.mouseDown()
pyautogui.moveTo(1300, 655, duration=1)
pyautogui.mouseUp()
time.sleep(0.5)  # small pause

# Step 3: Press Ctrl+C to copy
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # wait for clipboard

# Step 4: Get clipboard content
chat = pyperclip.paste()
print("Copied Content:")
print(chat)
#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



command = '''Want me to help you get set up .'''

completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you narrate the word shown and speak it like a person and you analyze the chat and respond as a person . output should be the next chat response.",
        },
        {
            "role": "user",
            "content": chat,
        }
    ],
    model="gpt-4o",
    temperature=1,
    max_tokens=4096,
    top_p=1
)

response = completion.choices[0].message.content

pyperclip.copy (response)

time.sleep(2)


pyautogui.click(838, 614)

time.sleep(0.5)  

#  Paste clipboard text 
pyautogui.hotkey('ctrl', 'v')

time.sleep(0.2)  

#  Press Enter
pyautogui.press('enter')