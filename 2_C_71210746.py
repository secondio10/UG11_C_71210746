def check_data_type(d1,d2):
    if (type(d1).__name__.lower()==d2.lower()):
        print("Jawaban Anda benar")
        return True
    print("Jawaban Anda salah, seharusnya adalah: ", type(d1).__name__)
    return False


print(check_data_type(True,"Bool"))
print(check_data_type(True,"bool"))
print(check_data_type({},"TUPLE"))
print(check_data_type({},"DIct"))
print(check_data_type([],""))
