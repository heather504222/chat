# 檔案讀取
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding= 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 資料轉換
def convert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_pic_count = 0
	viki_pic_count = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_pic_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_pic_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print('Allen 說了' , allen_word_count , '個字')
	print('Allen 貼了', allen_sticker_count, '張貼圖')
	print('Allen 貼了', allen_pic_count, '張圖片')
	print('Viki 說了' , viki_word_count , '個字')
	print('Viki 貼了', viki_sticker_count, '張貼圖')
	print('Viki 貼了', viki_pic_count, '張圖片')


# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding= 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

# 執行程式
def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()
