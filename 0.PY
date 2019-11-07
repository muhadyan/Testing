# checkpoint 1
x = 12
print(x+x)

# git add . ==> untuk nge add semua file disebuah folder
# git add NAMAFILE  ==> untuk nge add sebagian file disebuah folder
# Selama masih diadd dan belum dicommit maka masih bisa ditambahin file baru untuk dicommit
# git rm --cached NAMAFILE   ==> untuk remove file dari add
# git commit -m "MESSAGENYA"    ==> untuk menambah commit file@ yg udah diadd
# git log   ==> cara cek info lengkap commit yg udah ada
# git log --online  ==> cara cek info singkat commit yg udah ada
# git checkout ID-NYA   ==> buat liat chekckpoint yg pernah ada
# git checkout master   ==> balik lagi ke yg terbaru
# git reset ID-NYA      ==> untuk kembali ke checkpoint tertentu terus hapus checkpoint2 setelahnya (tapi file2nya masih ada)
# git reset ID-NYA --hard   ==> untuk kembali ke checkpoint tertentu terus hapus checkpoint2 setelahnya (termasuk file2nya)
# git branch NAMA_BRANCH_NYA    ==> untuk bikin cabang
# git branch -a     ==> untuk ngeliat ada cabang apa aja
# git checkout NAMA_BRANCH_NYA      ==> untuk pindah ke branch dari master atau branch lain
# git branch -D NAMA_BRANCH_NYA     ==> untuk ngehapus cabang
print('Halo')