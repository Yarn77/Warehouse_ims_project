from warehouse_core.products import TechItem, FreshItem
from warehouse_core.security import get_api_key
from warehouse_core.products import BaseProduct

def main():
    api_key = get_api_key()
    print(f'=== WAREHOUSE IMS (Auth: {api_key[:4]}****) ===')
    
    inventory = [
        TechItem('Laptop', 999.0, 'Aisle A-1'),
        FreshItem('Organic Milk', 4.0, 'Cold-Room B')
    ]
    
    print('\n--- WAREHOUSE STORAGE FEE INVENTORY REPORT ---')
    for item in inventory:
        fee = item.calc_fee(days=3)
        print(f'[{item.name}] Rack: {item.loc.rack} | 3-Day Holding Fee: ${fee:.2f}')

try:
  test_product = BaseProduct('Generic', 10.0, 'A1')
except TypeError as error:
  print('Test 2 passed because it crashed correctly with error:', error)

if __name__ == '__main__':
    main()