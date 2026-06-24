**1. Proses:**
        1. Membuat template struktur Data bernama "Order"
        2. Untuk informasi, Intialize pesanan private attribute seperti orderid, customer name, order date dan total amount
        3. Membuat fungsi  `calculate_tax` untuk proses perhitungan pajak dari total amount yang diisi (*10%)
        4. Membuat fungsi display total amount, karena attribute total_amount adalah private attribute
        5. Membuat fungsi display order yang berisi attribute yang nantinya diisii

**2. Encapsulation** -> Proteksi data — mencegah data diubah sembarangan dari luar class. Jadi attribute di Class Order & OrderProcessor saya buat private dengan menambahkan __ didepan nama attribute. Seperti `self._order_id = order_id` . Dengan begitu, attribute tidak bisa di akses secara di kelas lain. Untuk bisa mengaksesnya seperti private attribute `total_amount` di function `calculate_revenue`. Karena attribute tsb private, saya membuat function lagi yaitu `get_total_amount`

**3. Cara saya mengujinya:**

Saya membuat 3 pesanan:

1. pesanan1: Giwang → Rp 100.000
2. pesanan2: Dwi → Rp 50.000
3. pesanan3: Kintan → Rp 150.000

**Total revenue** = 100.000 + 50.000 + 150.000 = Rp 300.000

Pajak 10% dari masing-masing pesanan:

100.000 × 10% = 10.000
50.000 × 10% = 5.000
150.000 × 10% = 15.000

**Total pajak** = 10.000 + 5.000 + 15.000 = Rp 30.000

Saat calculate_total_tax() dijalankan, hasilnya 30000 → sesuai ekspektasi.
        
