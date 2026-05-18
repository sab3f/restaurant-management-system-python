class Menu:
    def __init__(self):
        self.items = []
        
    def add_menu(self,item_name):
        self.items.append(item_name)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
             return item
        return None

    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
             self.items.remove(item_name)
             print('Item deleted')
        else:
            print('Item not found')     
    
    def show_menu(self):
        print('*****Menu*****')
        print('Name\tPrice\tQuantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
