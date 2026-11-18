# [OOP CONCEPT 4: POLYMORPHISM IN ACTION & SECURE PRACTICES]
# A single loop computes fees across diverse objects without type checks!
# =====================================================================
import os

def get_api_key():
    return os.getenv('WAREHOUSE_API_KEY', 'FALLBACK_DEV_KEY_SECURE')

