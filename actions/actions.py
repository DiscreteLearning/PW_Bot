
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import requests
from rasa_sdk.events import SlotSet


class ActionGreetUser(Action):

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="greet")

        return [UserUtteranceReverted()]

# class HandleOptionSelection(Action):
#     def name(self) -> Text:
#         return "action_handle_option_selection"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Check which option the user selected
#         selected_option = tracker.latest_message['text']
#         print(selected_option)
        
#         if "Explore Features" in selected_option:
#             dispatcher.utter_message(template="utter_subsequent_options")
#         elif "Report the Issue" in selected_option:
#             # Perform an action or provide a response based on Option 2 selection
#             dispatcher.utter_message(template="utter_report_the_issue")
#         else:
#             dispatcher.utter_message("Please select one of the initial options.")

#         return []

# class IssueResolutionAction(Action):
#     def name(self) -> Text:
#         return "action_resolve_issue"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         issue_type = tracker.latest_message['intent'].get('name')

#         if issue_type in ['order_issue', 'playback_issue', 'batch_access_issue']:
#             dispatcher.utter_message("Here are some general suggestions for resolving this issue.")

#             # You can provide specific suggestions for each issue type here

#             # Check if the user is still experiencing the issue
#             dispatcher.utter_message("Is the issue resolved?")
#             return [SlotSet("issue_type", issue_type)]

#         dispatcher.utter_message("I'm not sure how to help with this issue. Please provide more details.")

#         return []

# class CreateTicketAction(Action):
#     def name(self) -> Text:
#         return "action_create_ticket"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         issue_type = tracker.get_slot("issue_type")
#         user_input = tracker.latest_message.get("text")

#         # Create a ticket in Google Sheets or your preferred ticketing system
#         # You can use the Google Sheets API or any other suitable method for this

#         dispatcher.utter_message("A ticket has been created for your issue. Our team will get back to you shortly.")

#         return [SlotSet("issue_type", None)]
# class ActionCorona(Action):

#     def name(self) -> Text:
#         return "action_corona_tracker"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         response = requests.get("https://api.covid19india.org/data.json").json()

#         entitites = tracker.latest_message['entities']
#         print("message", entitites)
#         state = None

#         for e in entitites:
#             if e['entity'] == 'state':
#                 state = e['value']

#         message = "please enter correct state"
#         if state == "india":
#             state = "total"

#         for data in response["statewise"]:
#             if data["state"] == state.title():
#                 print(data)
#                 message = "Active: " + data["active"] + "\n Confirmed: " + data["confirmed"]+"\n Recovered:  " + data["recovered"]
#                 mess = "\n state notes:  " + data["statenotes"]

#         print(message)
#         dispatcher.utter_message(text=message)
#         dispatcher.utter_message(text=mess)

#         return []


