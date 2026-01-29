import requests
from typing import Dict, List

class MultiPlatformConnector:
    """Multi-Platform API Connector for eBay, Whatnot, etc.
    
    Part of Quiqly's REPOSITORY Intelligence
    Single interface for all marketplace APIs
    """
    
    def __init__(self, api_keys: Dict):
        self.connectors = {
            "ebay": EbayConnector(api_keys.get("ebay_key")),
            "whatnot": WhatnnotConnector(api_keys.get("whatnot_key")),
            "amazon": AmazonConnector(api_keys.get("amazon_key")),
            "etsy": EtsyConnector(api_keys.get("etsy_key")),
            "shopify": ShopifyConnector(api_keys.get("shopify_key"))
        }
    
    def list_product_all_platforms(self, product_data: Dict) -> Dict:
        """List a product on all platforms with one call"""
        results = {}
        for platform_name, connector in self.connectors.items():
            try:
                result = connector.create_listing(product_data)
                results[platform_name] = {
                    "status": "✅ Listed",
                    "listing_id": result.get("id"),
                    "url": result.get("url")
                }
            except Exception as e:
                results[platform_name] = {"status": "❌ Failed", "error": str(e)}
        return results
    
    def sync_inventory(self, product_id: str, quantity: int) -> Dict:
        """Sync inventory across all platforms"""
        results = {}
        for platform_name, connector in self.connectors.items():
            try:
                connector.update_inventory(product_id, quantity)
                results[platform_name] = f"✅ Synced: {quantity} units"
            except Exception as e:
                results[platform_name] = f"❌ Error: {str(e)}"
        return results
    
    def fetch_orders_all_platforms(self) -> List:
        """Get all orders from all platforms"""
        all_orders = []
        for platform_name, connector in self.connectors.items():
            try:
                orders = connector.get_orders()
                for order in orders:
                    order["platform"] = platform_name
                    all_orders.append(order)
            except Exception as e:
                print(f"⚠️ {platform_name} fetch failed: {str(e)}")
        return sorted(all_orders, key=lambda x: x.get("created_at"), reverse=True)
    
    def unified_fulfillment(self, order_id: str, platform: str, tracking_number: str) -> str:
        """Mark order as shipped on the specified platform"""
        connector = self.connectors.get(platform)
        if connector:
            connector.mark_shipped(order_id, tracking_number)
            return f"✅ Order {order_id} marked shipped on {platform.upper()}"
        return "❌ Platform not supported"

# Connector Implementations
class EbayConnector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.ebay.com"
    
    def create_listing(self, product_data):
        # eBay API call
        return {"id": "ebay_123", "url": "https://ebay.com/..."}
    
    def update_inventory(self, product_id, quantity):
        pass
    
    def get_orders(self):
        return []
    
    def mark_shipped(self, order_id, tracking):
        pass

class WhatnnotConnector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.whatnot.com"
    
    def create_listing(self, product_data):
        return {"id": "whatnot_456", "url": "https://whatnot.com/..."}
    
    def update_inventory(self, product_id, quantity):
        pass
    
    def get_orders(self):
        return []
    
    def mark_shipped(self, order_id, tracking):
        pass

class AmazonConnector:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def create_listing(self, product_data):
        return {"id": "amazon_789", "url": "https://amazon.com/..."}
    
    def update_inventory(self, product_id, quantity):
        pass
    
    def get_orders(self):
        return []
    
    def mark_shipped(self, order_id, tracking):
        pass

class EtsyConnector:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def create_listing(self, product_data):
        return {"id": "etsy_012", "url": "https://etsy.com/..."}
    
    def update_inventory(self, product_id, quantity):
        pass
    
    def get_orders(self):
        return []
    
    def mark_shipped(self, order_id, tracking):
        pass

class ShopifyConnector:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def create_listing(self, product_data):
        return {"id": "shopify_345", "url": "https://shopify.com/..."}
    
    def update_inventory(self, product_id, quantity):
        pass
    
    def get_orders(self):
        return []
    
    def mark_shipped(self, order_id, tracking):
        pass

# Example Usage:
# connector = MultiPlatformConnector({
#     "ebay_key": "YOUR_KEY",
#     "whatnot_key": "YOUR_KEY",
#     "amazon_key": "YOUR_KEY"
# })
# results = connector.list_product_all_platforms({
#     "name": "Vintage Rolex",
#     "price": 5000,
#     "condition": "Mint"
# })
# orders = connector.fetch_orders_all_platforms()
