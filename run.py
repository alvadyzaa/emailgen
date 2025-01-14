import random
import string
import datetime
from colorama import init, Fore, Style
import time
import sys

# Inisialisasi colorama
init()

def generate_username(base_username, length=8):
    # Menambahkan angka random di belakang username dasar
    random_digits = ''.join(random.choice(string.digits) for _ in range(4))
    return f"{base_username}{random_digits}"

def generate_password(base_password, length=12):
    # Memastikan ada minimal 1 huruf besar, 1 huruf kecil, 1 angka, dan 1 simbol
    symbols = "!@#$%^&*"
    
    # Tambahkan komponen wajib
    required_chars = [
        random.choice(string.ascii_uppercase),  # 1 huruf besar
        random.choice(string.ascii_lowercase),  # 1 huruf kecil
        random.choice(string.digits),           # 1 angka
        random.choice(symbols)                  # 1 simbol
    ]
    
    # Acak posisi komponen wajib
    random.shuffle(required_chars)
    
    # Gabungkan dengan password dasar
    enhanced_password = base_password + ''.join(required_chars)
    
    # Tambahkan karakter random jika panjang masih kurang dari yang diinginkan
    while len(enhanced_password) < length:
        enhanced_password += random.choice(
            string.ascii_letters + string.digits + symbols
        )
    
    return enhanced_password

def generate_email(username, domain):
    return f"{username}@{domain}"

def generate_account(base_username, base_password, domain, count=1):
    accounts = []
    for _ in range(count):
        username = generate_username(base_username)
        password = generate_password(base_password)
        email = generate_email(username, domain)
        
        account_info = {
            "username": username,
            "email": email,
            "password": password
        }
        accounts.append(account_info)
    
    return accounts

def save_to_file(accounts):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"accounts_{timestamp}.txt"
    
    with open(filename, "w") as file:
        file.write("=== Generated Accounts ===\n\n")
        for i, account in enumerate(accounts, 1):
            file.write(f"Account {i}:\n")
            file.write(f"Username: {account['username']}\n")
            file.write(f"Email: {account['email']}\n")
            file.write(f"Password: {account['password']}\n")
            file.write("-" * 30 + "\n")
    
    return filename

def print_banner():
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║  ███████╗███╗   ███╗ █████╗ ██╗██╗     ██████╗ ███████╗███╗  ║
    ║  ██╔════╝████╗ ████║██╔══██╗██║██║    ██╔════╝ ██╔════╝████║ ║
    ║  █████╗  ██╔████╔██║███████║██║██║    ██║  ███╗█████╗ ██╔██║ ║
    ║  ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║    ██║   ██║██╔══╝ ╚═╝██║ ║
    ║  ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗╚██████╔╝███████╗███║ ║
    ║  ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚══════╝╚══╝ ║
    ║                                                              ║
    ║              Email Generator Tool v1.0                       ║
    ║                 made by: alvadyza                            ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    # Warna gradien untuk banner
    colors = [Fore.CYAN, Fore.LIGHTCYAN_EX, Fore.BLUE]
    lines = banner.split('\n')
    
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        print(color + line + Style.RESET_ALL)
    
    # Menambahkan informasi tambahan
    print(Fore.YELLOW + "\n[*] Tool untuk generate akun email secara otomatis")
    print("[*] Pastikan gunakan dengan bijak\n" + Style.RESET_ALL)
    print(Fore.WHITE + "=" * 60 + Style.RESET_ALL)

def validate_password(password):
    """Validasi password memenuhi kriteria minimum"""
    if len(password) < 8:
        return False, "Password harus minimal 8 karakter!"
    if not any(c.isdigit() for c in password):
        return False, "Password harus mengandung minimal 1 angka!"
    if not any(c.isupper() for c in password):
        return False, "Password harus mengandung minimal 1 huruf besar!"
    if not any(c.islower() for c in password):
        return False, "Password harus mengandung minimal 1 huruf kecil!"
    if not any(c in "!@#$%^&*" for c in password):
        return False, "Password harus mengandung minimal 1 simbol (!@#$%^&*)!"
    return True, "Password valid!"

def loading_animation():
    chars = "/—\\|"
    for char in chars:
        sys.stdout.write('\r' + Fore.CYAN + 'Loading... ' + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)

def main():
    print_banner()
    
    # Menambahkan jeda waktu untuk efek loading
    print(Fore.CYAN + "\nMemulai program..." + Style.RESET_ALL)
    time.sleep(1)
    
    print(Fore.YELLOW + "\n[+] Silakan masukkan informasi yang diperlukan:" + Style.RESET_ALL)
    
    # Input username
    base_username = input(Fore.GREEN + "Masukkan username dasar: " + Style.RESET_ALL)
    
    # Input dan validasi password
    while True:
        base_password = input(Fore.GREEN + "Masukkan password dasar: " + Style.RESET_ALL)
        is_valid, message = validate_password(base_password)
        if is_valid:
            print(Fore.GREEN + "✓ " + message + Style.RESET_ALL)
            break
        print(Fore.RED + "✗ " + message + Style.RESET_ALL)
        print(Fore.YELLOW + "Password harus mengandung minimal:\n" +
              "- 8 karakter\n" +
              "- 1 huruf besar\n" +
              "- 1 huruf kecil\n" +
              "- 1 angka\n" +
              "- 1 simbol (!@#$%^&*)" + Style.RESET_ALL)
    
    # Lanjutkan dengan input domain dan jumlah akun
    domain = input(Fore.GREEN + "Masukkan domain email (contoh: gmail.com): " + Style.RESET_ALL)
    
    while True:
        try:
            jumlah_akun = int(input(Fore.GREEN + "Masukkan jumlah akun yang ingin dibuat: " + Style.RESET_ALL))
            if jumlah_akun > 0:
                break
            print(Fore.RED + "Jumlah akun harus lebih dari 0!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Masukkan angka yang valid!" + Style.RESET_ALL)

    # Generate akun dan simpan ke file
    print(Fore.YELLOW + "\nMembuat akun..." + Style.RESET_ALL)
    accounts = generate_account(base_username, base_password, domain, jumlah_akun)
    filename = save_to_file(accounts)

    print(Fore.GREEN + f"\n✓ Berhasil membuat {jumlah_akun} akun!" + Style.RESET_ALL)
    print(Fore.GREEN + f"✓ Data telah disimpan dalam file: {filename}" + Style.RESET_ALL)

    # Tampilkan hasil generate
    print(Fore.CYAN + "\nDetail Akun yang Dibuat:" + Style.RESET_ALL)
    for i, account in enumerate(accounts, 1):
        print(Fore.YELLOW + f"\nAkun {i}:" + Style.RESET_ALL)
        print(Fore.WHITE + f"Username: " + Fore.GREEN + f"{account['username']}" + Style.RESET_ALL)
        print(Fore.WHITE + f"Email: " + Fore.GREEN + f"{account['email']}" + Style.RESET_ALL)
        print(Fore.WHITE + f"Password: " + Fore.GREEN + f"{account['password']}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()