import asyncio
import inspect
from sanic import Sanic, Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse
from typing import Text, Dict, Any, Optional, Callable, Awaitable, NoReturn

import rasa.utils.endpoints
from rasa.core.channels.channel import (
    InputChannel,
    CollectingOutputChannel,
    UserMessage,
)

class MyIO(InputChannel):
    def name(self) -> Text:
        """Name of your custom channel."""
        return "myio"

    def blueprint(
        self, on_new_message: Callable[[UserMessage], Awaitable[None]]
    ) -> Blueprint:

        custom_webhook = Blueprint(
            "custom_webhook_{}".format(type(self).__name__),
            inspect.getmodule(self).__name__,
        )

        @custom_webhook.route("/", methods=["GET"])
        async def health(request: Request) -> HTTPResponse:
            return response.json({"status": "ok"})

        @custom_webhook.route("/webhook", methods=["POST"])
        async def auth_token(request: Request):
            if not request.json:
                return response.json({"error":"Missing sender"}, 400)
            # sender_id = await self._extract_sender(request)

            sender_id = request.json.get("sender_id") # method to get sender_id 
            text = request.json.get("text") # method to fetch text
            headers = request.headers
            try:
                auth_key = headers['authorization']
                if auth_key != "thisismysecret":
                    return response.json({"status":"not_authorized","message":"Sorry. You are not an authorized user"})
            except:
                return response.json({"status":"not_authorized","message":"Sorry. You are not an authorized user"})
            input_channel = self.name()
            collector = CollectingOutputChannel()
            await on_new_message(
                UserMessage(
                    text,
                    collector,
                    sender_id,
                    input_channel=input_channel,
                )
            )            
            # return response.json({"bot_token":decoded_token}, 200)
            return response.json({"reply":collector.messages}, 200)
        return custom_webhook