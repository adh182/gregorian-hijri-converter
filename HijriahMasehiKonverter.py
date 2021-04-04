class HijriahKeMasehi:

	def __init__(self, tahun, bulan, tanggal):
		self.tahun = tahun
		self.bulan = bulan
		self.tanggal = tanggal

	def hitung_variabel(self):
		N = self.tanggal + int(29.5001*(self.bulan - 1) + 0.99)
		Q = int(self.tahun/30)
		R = self.tahun%30
		A = int((11*R + 3) / 30)
		W = 404*Q + 354*R + 208 + A
		Q1 = int(W/1461)
		Q2 = W%1461
		G = 621 + 4 * int(7*Q + Q1)
		K = int(Q2 / 365.2422)
		E = int(365.2422*K)
		self.julian_day_num = Q2 - E + N - 1
		self.julian_year = G + K

		return self.julian_year, self.julian_day_num
                
	def gregorian(self):
		self.julian_year, self.julian_day_num = self.hitung_variabel()

		if self.julian_day_num > 366 and self.julian_year % 4 == 0:
			self.julian_year = self.tahun - 366
			self.julian_day_num = self.julian_day_num + 1
		elif self.julian_day_num > 365 and self.julian_year % 4 == 0:
			self.julian_year = self.tahun - 365
			self.julian_day_num = self.julian_day_num + 1

		return self.julian_year, self.julian_day_num

	def convert_to_gregorian(self):
		tahun_julian, jumlah_hari = self.gregorian()
		julian_day = int(365.25*(tahun_julian - 1)) + 1721423 + jumlah_hari
		alpha = int((julian_day - 1867216.25)/36524.25)
		beta = julian_day + 1 + alpha - int(alpha/4)

		if julian_day < 2299161:
			beta = julian_day

		b = beta + 1524
		c = int((b-122.1) / 365.25)
		d = int(365.25*c)
		e = int((b-d)/30.6001)

		self.hari = b - d - int(30.6001*e)
		self.no_bulan = 0
		if e < 14:
			self.no_bulan = e - 1
		elif e > 13:
			self.no_bulan = e - 13

		self.year = 0
		if self.no_bulan > 2:
			self.year = c - 4716
		elif self.no_bulan < 3:
			self.year = c - 4715

		# print(julian_day, alpha, beta, b, c, d, e)

		hasil = "{}/{}/{}".format(self.year, self.no_bulan, self.hari)
		return hasil

class MasehiKeHijriah:

	def __init__(self, tahun, bulan, tanggal):
		self.tahun = tahun
		self.bulan = bulan 
		self.tanggal = tanggal 

	def hitung_variabel(self):
		if self.bulan < 3:
			self.tahun = self.tahun - 1
			self.bulan = self.bulan + 12
			
		# print(self.tahun, self.bulan)
		alpha = int(self.tahun/100)
		beta = 2 - alpha + int(alpha/4)
		b = int(365.25*self.tahun) + int(30.6001*(self.bulan+1)) + self.tanggal + 1722519 + beta
		c = int((b-122.1) / 365.25)
		d = int(365.25*c)
		e = int((b-d)/30.6001)

		self.hari = b - d - int(30.6001*e)
		self.no_bulan = 0
		if e < 14:
			self.no_bulan = e - 1
		elif e > 13:
			self.no_bulan = e - 13

		self.year = 0
		if self.no_bulan > 2:
			self.year = c - 4716
		elif self.no_bulan < 3:
			self.year = c - 4715

		# print(self.year, self.no_bulan, self.hari)
		return self.year, self.no_bulan, self.hari

	def to_hijriah(self):
		tahun, bulan, tanggal = self.hitung_variabel()

		
		if tahun%4 == 0:
			W = 1
		else:
			W = 2

		N = int((275*bulan)/9) - W * int((bulan+9)/12) + tanggal - 30
		A = tahun -  623
		B = int(A/4)
		C = A%4
		C1 = 365.2501*C
		C2 = int(C1)

		if C1 - C2 > 0.5:
			C2 = C2 + 1

		D = 1461*B + 170 + C2
		Q = int(D/10631)
		R = D%10631
		J = int(R/354)
		K = R%354
		O = int((11*J + 4)/30)
		self.year = 30*Q + J + 1
		self.day_number = K - O + N -1

		return self.year, self.day_number

	def isLeap(self):
		self.year, self.day_number = self.to_hijriah()

		if self.day_number > 354: 
			CL = self.year%30
			DL = (11*CL + 3)%30

			if DL < 19:
				self.day_number = self.day_number - 354
				self.year = self.year + 1
			elif DL > 18:
				self.day_number = self.day_number - 355
				self.year = self.year + 1

			if self.day_number == 0:
				self.day_number = 355
				self.year = self.year - 1

		return self.year, self.day_number

	def convert_to_hijriah(self):
		self.year, self.day_number = self.isLeap()

		S = int((self.day_number - 1) / 29.5)
		self.no_bulan = 1 + S 
		self.hari = int(self.day_number - 29.5*S)

		hasil = "{}/{}/{}".format(self.year, self.no_bulan, self.hari)

		return hasil 
