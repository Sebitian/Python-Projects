import speech_recognition
import pyttsx3
import openai

openai.api_key = "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"

recognizer = speech_recognition.Recognizer()
flag = True
engine = pyttsx3.init()

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].text

while flag:
    try:
        with speech_recognition.Microphone() as mic:
            audio = recognizer.listen(mic, timeout=5)
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print("Please speak now.")

            if text in ('stop', 'exit'):
                flag = False
                print("Program has ended.")
                engine.say("Program has ended.")
                engine.runAndWait()
            else:
                print(f"You said: {text}")
                engine.say(f"You said: {text}")
                # DALL-E
                image_resp = openai.Image.create(prompt=str(text), n=1, size="512x512")
                print(image_resp)
                # CHATGPT
                generated_text = generate_text(text)
                engine.say(f"CHAT-GPT said: {generated_text}")
                print(generated_text)
                engine.runAndWait()

    except speech_recognition.UnknownValueError:
        print("I am sorry, I didn't understand that.")
        engine.say("I am sorry, I didn't understand that.")
        engine.runAndWait()
    except speech_recognition.RequestError as e:
        print(f"I am having trouble recognizing your voice, please try again. {e}")
        engine.say(f"I am having trouble recognizing your voice, please try again.")
        engine.runAndWait()






