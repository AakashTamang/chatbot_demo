# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import base64
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class Greeting(Action):
	def name(self):
		return "action_greeting"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Hi there. It's such a pleasure to have you here 🤗. How can I help you.",
					"Hello 👋😃 How can I assist you."]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class Goodbye(Action):
	def name(self):
		return "action_goodbye"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ['Thank you, I am happy to help you 😎',
					'I hope I was helpful for you 🤗']
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class ShowButtons(Action):
	def name(self):
		return "action_show_buttons"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Do you want to see an image or cards?","Would you like to see an image or cards?"]
		reply = random.choice(messages)
		buttons = [
			{"title":"Image","payload":"image"},
			{"title":"Cards","payload":"cards"},
			{"title":"Nothing","payload":"no"}
		]
		attachment = {
			"query_response": reply,
			"data":[{"buttons":buttons}],
			"type":"message_with_buttons",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []


class ShowImages(Action):
	def name(self):
		return "action_show_images"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Here is an image for you."]
		reply = random.choice(messages)
		with open("images/astronut.png","rb") as image_file:
			image_base64 = base64.b64encode(image_file.read())
		image = [str(image_base64)]
		attachment = {
			"query_response": reply,
			"data":[{"image":image}],
			"type":"message_with_image",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class ShowCards(Action):
	def name(self):
		return "action_show_cards"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Here is a card for you."]
		reply = random.choice(messages)
		with open("images/astronut.png","rb") as image_file:
			image_base64_1 = base64.b64encode(image_file.read())
		with open("images/chatbot.png","rb") as image_file:
			image_base64_2 = base64.b64encode(image_file.read())
		image_1 = str(image_base64_1)
		image_2 = str(image_base64_2)
		cards = {
			"card_1":image_1,
			"card_2":image_2
		}
		attachment = {
			"query_response": reply,
			"data":[{"cards":cards}],
			"type":"message_with_card",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class Nothing(Action):
	def name(self):
		return "action_nothing"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["It's ok if you don't want to see anything.","I am ok if you do not want to see anything."]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return []

class ActionDefaultFallback(Action):
	def name(self) -> Text:
		return "action_handle_fallback"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
				"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return [UserUtteranceReverted()]

class ActionOutofScope(Action):
	def name(self) -> Text:
		return "action_out_of_scope"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Sorry 😕, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it 🧐. Would you repeat it please?",
				"I find it quite ambiguous. 😕 Can you tell me again a bit clearly? 🧐"]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[],
			"type":"normal_message",
			"data_fetch_status": "success"
		}
		dispatcher.utter_message(attachment=attachment)
		return [UserUtteranceReverted()]