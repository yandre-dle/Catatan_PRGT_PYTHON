# Definisikan function validate 

    # Tambahkan control flow berdasarkan nilai hand
    

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Kertas', 'Gunting']
    print(name + ' memilih: ' + hands[hand])

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('masukkan nomor (0-2): '))

# Tambahkan control flow berdasarkan nilai return dari function validate 

print_hand(player_hand, player_name)
