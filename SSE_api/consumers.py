from django_eventstream.consumers import EventsConsumer
import asyncio
class CustomEventConsumer(EventsConsumer):
    async def __call__(self, scope, receive, send):
        print(scope['url_route']['kwargs'])
        
        return await super().__call__(scope, receive, send) 