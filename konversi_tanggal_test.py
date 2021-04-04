from HijriahMasehiKonverter import HijriahKeMasehi, MasehiKeHijriah


test = HijriahKeMasehi(1421, 1, 1)
test2 = HijriahKeMasehi(1444, 10, 12)
test3 = HijriahKeMasehi(1342, 2, 29)
test4 = MasehiKeHijriah(1991, 8, 13)
test5 = MasehiKeHijriah(2000, 28, 1)
test6 = MasehiKeHijriah(2020, 1, 15)
                    
print("Hijriah ke Masehi")
print(test.convert_to_gregorian())
print(test2.convert_to_gregorian())
print(test3.convert_to_gregorian())
print("\nMasehi ke Hijriah")
print(test4.convert_to_hijriah())
print(test5.convert_to_hijriah())
print(test6.convert_to_hijriah())
# print(test6.hitung_variabel())