# Berikan 20 ke variable money


items = {'apel': 2, 'pisang': 4, 'jeruk': 6}
for item_name in items:
    print('--------------------------------------------------')
    # Menggunakan variable money, cetak 'Anda memiliki ___ dolar di dompet Anda'
    
    
    print('Harga setiap ' + item_name + ' ' + str(items[item_name]) + ' dolar')
    
    input_count = input('Mau berapa ' + item_name + '?:')
    print('Anda akan membeli ' + input_count + ' ' + item_name)
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('Harga total adalah ' + str(total_price) + ' dolar')
    
    # Tambahkan control flow berdasarkan perbandingan dari money dan total_price
    
