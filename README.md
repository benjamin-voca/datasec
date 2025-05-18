# Aplikacion GUI për Enkriptim dhe Dekriptim me Triple DES (3DES-2KEY CBC)

## 📌 Përmbledhje e Projektit

Ky projekt paraqet një aplikacion desktop me ndërfaqe grafike të ndërtuar në Python, i cili implementon algoritmin e kriptimit **Triple DES (3DES)** në mënyrën **2-Key CBC (Cipher Block Chaining)**. Përdoruesit mund të enkriptojnë dhe dekriptojnë skedarë binarë përmes një ndërfaqeje të thjeshtë, duke specifikuar çelësin (në format hexadecimal) dhe vlerën inicializuese (IV).

Aplikacioni u zhvillua me qëllim demonstrimi të aplikimit praktik të algoritmeve simetrikë të sigurisë dhe ofron një mënyrë të lehtë për të kuptuar procesin e enkriptimit dhe dekriptimit të të dhënave me 3DES.

---
### Përshkrim i Shkurtër i Komponentëve:

- **main.py** – Përmban klasën `TripleDESApp` që ndërton GUI-në me Tkinter, trajton inputin nga përdoruesi dhe ekzekuton procesin e enkriptimit/dekriptimit.
- **README.md** – Ky dokument që përshkruan funksionalitetin, qëllimin dhe strukturën e projektit.

---

## ⚙️ Si Funksionon

Aplikacioni funksionon në katër hapa kryesorë:

1. **Zgjedhja e Skedarit**
   - Përdoruesi zgjedh një skedar binar përmes butonit “Browse”.

2. **Vendosja ose Gjenerimi e Çelësit dhe IV-së**
   - Çelësi është 16 bajtë (32 karaktere hexadecimal).
   - IV-ja është 8 bajtë (16 karaktere hexadecimal).
   - Mund të futen manualisht ose të gjenerohen automatikisht.

3. **Zgjedhja e Veprimit**
   - Përdoruesi zgjedh mes opsioneve: `Encrypt` ose `Decrypt`.

4. **Ekzekutimi dhe Ruajtja e Rezultatit**
   - Aplikacioni lexon skedarin, aplikon 3DES-CBC, dhe ruan rezultatin në një skedar të ri me prapashtesën `.enc` ose `.dec`.

> **Shënim:** Gjatë dekriptimit, nëse emri i skedarit bie ndesh me origjinalin, krijohet automatikisht një emër alternativ për të shmangur mbivendosjen.

---

##  Qëllimi i Projektit

Ky projekt është zhvilluar për të:

- Demonstruar përdorimin praktik të **kriptografisë simetrike**, në veçanti **Triple DES (3DES)** me dy çelësa.
- Edukuar përdoruesit dhe studentët mbi procesin e **enkriptimit dhe dekriptimit të të dhënave** përmes ndërfaqes grafike.
- Ilustruar funksionimin e modalitetit **CBC (Cipher Block Chaining)** dhe rëndësinë e përdorimit të një **IV-je unike**.
- Ofruar një mjet të thjeshtë, të përdorshëm dhe të kuptueshëm për të eksperimentuar me algoritme të sigurisë të cilat, ndonëse të vjetra, ende përdoren në disa kontekste të trashëguara.

---

> Ky aplikacion mund të shërbejë si bazë për projekte më të avancuara në fushën e sigurisë së informacionit, përfshirë implementimin e algoritmeve më të sigurt si **AES**, dhe mund të integrohet me module për **kontrollin e integritetit të të dhënave**.
> 
## Punuan:
- Benjamin Voca
- Bledion Zymberi
- Bleron Baftiu
- Blertin Hamza
