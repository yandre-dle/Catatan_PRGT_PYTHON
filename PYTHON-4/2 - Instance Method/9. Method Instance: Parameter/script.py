class MenuItem:
    def info(self):
        return self.name + ': $' + str(self.price)

    # Definiskan method get_total_price
    


menu_item1 = MenuItem()
menu_item1.name = 'Roti Lapis'
menu_item1.price = 5

print(menu_item1.info())

# Panggil method get_total_price 


# Cetak 'Total harga adalah $____'


