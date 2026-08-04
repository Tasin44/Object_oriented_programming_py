class Shop:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    def add_to_cart(self,item,price,quantity):
        self.cart.append({'ITEM':item,'PRICE':price,'QUANTITY':quantity})

    def chekout(self,amount):
        # print(self.cart)

        Tprice=0
        
        for i in self.cart:
           Tprice+=i['PRICE']*i['QUANTITY']#cart e jevabe item gular name thakbe,seivabe []er moddhe hobe
           
        #Tprice = sum(i['PRICE'] * i['QUANTITY'] for i in self.cart)#using list comprehension 

        if amount<Tprice:
            return f'Need more money:{Tprice-amount}'
        elif amount>Tprice:
            return f'Extra money:{amount-Tprice}'
        else:
            #item_list= "\n".join(f"item:{i+1}: {i['item']}\n Price: {i['price']}\n Quantity: {i['quantity']}" for i in self.cart)
            # item_list = "\n".join([f"Item{i + 1}: {item['item']}, Price: {item['price']}, Quantity: {item['quantity']}" for i, item in enumerate (self.cart)])
            item_list = "\n".join(f"Item{j + 1}: {i['ITEM']}, Price: {i['PRICE']},Quantity: {i['QUANTITY']}" for j,i in enumerate (self.cart))
            return f'Here are the items:\n{item_list}'


shopping=Shop("Tasin")
shopping.add_to_cart("Shirt",500,3)
shopping.add_to_cart("Pant",300,2)
shopping.add_to_cart("Shoe",999,1)

print(shopping.chekout(3099))