📦 Panduan Lengkap Deploy Otomatis ke EC2 dengan GitHub Actions

1. Upload seluruh isi folder ini ke GitHub repo (branch: main)

2. Tambahkan Secrets di repo GitHub:
   - DEPLOY_SERVER_IP = IP publik EC2 lo
   - DEPLOY_USER_UBUNTU = ubuntu
   - SSH_KEY_UBUNTU = isi dari private key (.pem), TANPA password

3. Pastikan EC2 lo aktif dan port 5000 terbuka (Security Group)

4. Jalankan `ssh-keygen` (opsional) jika lo mau pakai deploy key sendiri.

5. Cek hasil deploy di GitHub tab `Actions`, lalu akses app via:
   http://<IP_EC2>:5000
