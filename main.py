import l1
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_s = alphabet + " "
ffile = None
ffile_s = None
with open("doktor-zhivago.txt", "r",encoding="utf") as f:
    ffile = l1.f_filter(f, alphabet)
    ffile_s = l1.f_filter(f, alphabet_s)
single = l1.count_single(ffile, alphabet)
single_space = l1.count_single(ffile_s, alphabet_s)
double1, double2 = l1.count_double(ffile, alphabet)
double_space1, double_space2 = l1.count_double(ffile_s, alphabet_s)
l1.generatecsv([single,single_space, double1,double2, double_space1, double_space2])
l1.printentropy([single,single_space, double1,double2, double_space1, double_space2])
ffile.close()
ffile_s.close()