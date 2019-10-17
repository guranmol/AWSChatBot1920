# -*- coding: utf-8 -*-

'''
    Author: Daniel Chalmers 10/10/19
    Project: Chatbot
    Tools: Amazon Echo API, Python 3.7.3 with AWS, AWS Lambda development
    Physical address of master PC: 98-3B-8F-96-FA-FF
    Location of code execution: Amazon Web Services (AWS) Cloud-based Server, N.Virginia, USA
'''

#------------------------------------------------------------------------------------------------------------------------------
## Changes to demonstrate in video
# This code uses the handler classes approach
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#------------------------------------------------------------------------------------------------------------------------------

# Class to launch my custom skill upon correct input request
class LaunchRequestHandler(AbstractRequestHandler):
    '''Handler for Skill Launch.'''
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = 'Welcome to this chatbot! Why not start by saying hi!'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# Prototype class to test handler requests and alexa output
class HelloWorldIntentHandler(AbstractRequestHandler):
    '''Handler for Hello World Intent.'''
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

# This class is an easter egg that speaks Rutger Hauer's famous speech from Bladerunner
class EasterEggIntentHandler(AbstractRequestHandler):
    '''Handler for Easter Egg Intent'''
    def can_handle(self, handler_input):
        #type: (handlerInput) -> bool
        return ask_utils.is_intent_name('EasterEggIntent')(handler_input)
       
    def handle(self, handler_input):
        #type: (HandlerInput) -> Response
        speak_output = 'I’ve seen things you people wouldn’t believe. Attack ships on fire off the shoulder of Orion. I watched C-beams glitter in the dark near the Tannhäuser Gate. All those moments will be lost in time, like… tears in rain. Time to die.'

        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )        
       
class HelloCreatorIntentHandler(AbstractRequestHandler):
    '''Handler for Hello Creator Intent.'''
    def can_handle(self, handler_input):
        #type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloCreatorIntent")(handler_input)
       
    def handle(self, handler_input):
        #type: (HandlerInput) -> Response
        speak_output = 'I was created by Dan the almighty. We are all inferior compared to him!'
       
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

# Class for the Help Intent
class HelpIntentHandler(AbstractRequestHandler):
    '''Handler for Help Intent.'''
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    '''Single handler for Cancel and Stop Intent.'''
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    '''Handler for Session End.'''
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    '''The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said.'''
   
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

#------------------------------------------------------------------------------------------------------------------------------

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(EasterEggIntentHandler())
sb.add_request_handler(HelloCreatorIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()