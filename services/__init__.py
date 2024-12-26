from django.conf import settings
import redis
from functools import lru_cache

class ServiceRegistry:
    def __init__(self):
        self.redis_client = redis.Redis.from_url(settings.CACHES['default']['LOCATION'])
        
    @lru_cache(maxsize=None)
    def get_service(self, service_name):
        service_map = {
            'product': 'services.product_service',
            'order': 'services.order_service',
            'payment': 'services.payment_service',
            'shipment': 'services.shipment_service'
        }
        return __import__(service_map[service_name], fromlist=['*'])
    
    def publish_event(self, event_type, data):
        self.redis_client.publish(event_type, str(data))
    
    def subscribe_to_events(self, event_type, callback):
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe(event_type)
        for message in pubsub.listen():
            if message['type'] == 'message':
                callback(message['data'])

registry = ServiceRegistry()