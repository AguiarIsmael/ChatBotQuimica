
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        return []

class ActionEjemplo(Action):

    def name(self) -> Text:
        return "action_ejemp"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        modulo = tracker.get_slot("nModulo")
        if(modulo != None):
            if(modulo == "1"):
                dispatcher.utter_message(text="Estos ejercicios corresponden al modulo 1 http://www.exa.unicen.edu.ar/catedras/quimica/Quimica%20ISistemas/P1%20Sistemas.pdf")
            if(modulo == "2"):
                dispatcher.utter_message(text="Estos ejercicios corresponden al modulo 2 http://www.exa.unicen.edu.ar/catedras/quimica/Quimica%20ISistemas/P2%20ISistemas.pdf")
            if(modulo == "3"):
                dispatcher.utter_message(text="Estos ejercicios corresponden al modulo 3 http://www.exa.unicen.edu.ar/catedras/quimica/Quimica%20ISistemas/P3%20%20ISistemas.pdf")
            if(modulo == "4"):
                dispatcher.utter_message(text="Estos ejercicios corresponden al modulo 4 http://www.exa.unicen.edu.ar/catedras/quimica/Quimica%20ISistemas/P4%20ISistemas.pdf")
        dispatcher.utter_message(text="Ese modulo no corresponde a un abonado en servicio")
        return []
