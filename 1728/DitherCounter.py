# https://community.topcoder.com/stat?c=problem_statement&pm=1728
class DitherCounter:
	def count(self, dithered: str, screen: [str]) -> int:
		screen = "".join(screen)
		dithered_pixels = 0
		for l in dithered:
			dithered_pixels += screen.count(l)
		return dithered_pixels
		
d = DitherCounter()
print(d.count('BW',["AAAAAAAA", "ABWBWBWA", "AWBWBWBA", "ABWBWBWA", "AWBWBWBA", "AAAAAAAA"]) == 24)
print(d.count('BW',["BBBBBBBB", "BBWBWBWB", "BWBWBWBB", "BBWBWBWB", "BWBWBWBB", "BBBBBBBB"]) == 48)
print(d.count('ACEGIKMOQSUWY',["ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX", "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX", "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX", "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX", "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX", "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX"]) == 150)
print(d.count('CA',["BBBBBBB", "BBBBBBB", "BBBBBBB"]) == 0)
print(d.count('DCBA',["ACBD"]) == 4)