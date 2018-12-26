def crypt(s):
	random_string = "LoremipsumdolorsitametconsecteturadipiscingelitseddoeiusmodtemporincididuntutlaboreetdoloremagnaaliquaUtenimadminimveniamquisnostrudexercitationullamcolaborisnisiutaliquipexeacommodoconsequatDuisauteiruredolorinreprehenderitinvoluptatevelitessecillumdoloreeufugiatnullapariaturExcepteursintoccaecatcupidatatnonproidentsuntinculpaquiofficiadeseruntmollitanimidestlaborum"
	random_string_len = len(random_string)
	tmp = 0
	xor_string = ""
	for i in range(0, len(s)):
		xor_string = xor_string + random_string[i]
		tmp = (tmp + 1) % random_string_len
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s, xor_string))
