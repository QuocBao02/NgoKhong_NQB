import pygame
from pygame import mixer
import random
pygame.init()


score = 0 
highest_score = 0
volume = 1
screen = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Tây Du Ký_NQB.")
clock = pygame.time.Clock()
White = (255,255,255)

background = pygame.image.load("background0.png")
background = pygame.transform.scale(background,(1200, 720))
play_ima = pygame.image.load("Play.png")
play_ima = pygame.transform.scale(play_ima, (300,175))
ngokhong = pygame.image.load("ngokhong.png")
ngokhong = pygame.transform.scale(ngokhong, (100, 100))
background1 = pygame.image.load("background1.png")
background1 = pygame.transform.scale(background1,(1200, 720))
background2 = pygame.image.load("background2.png")
background2 = pygame.transform.scale(background2, (1200, 720))
background3 = pygame.image.load("background3.png")
background3 = pygame.transform.scale(background3, (1200, 720))
end = pygame.image.load("end.png")
end = pygame.transform.scale(end,(1200, 720))
# vat can level 1
ongduoi = pygame.image.load("ongduoi.png")
ongtren = pygame.image.load("ongtren.png")
#vat can level 2
onggo = pygame.image.load("onggo.png")
nuilua = pygame.image.load("nuilua.png")
# vat can level 3
kiemtren = pygame.image.load("kiemtren.png")
kiemduoi = pygame.image.load("kiemduoi.png")
# tao font diem 
font_score = pygame.font.SysFont("Corel", 35)
font_gameover = pygame.font.SysFont("Corel", 100)
font_runagain = pygame.font.SysFont("Corel", 35)
# tao font highest score
font_highest_score = pygame.font.SysFont("Corel", 35)
# tao font end game
font_end = pygame.font.SysFont("Corel", 100)
# toa do button play
x_pl = 900
y_pl = 575
# toa do ngo khong
x_nk = 0
y_nk = 300
level = 0
# toa do vat can 
x_og1 = 200
x_og2 = 400
x_og3 = 600
x_og4 = 800
x_og5 = 1000
x_og6 = 1200
# do rong cua ong
og_width = 100 
# random toa do cua vat can
og_height1 = random.randint(200, 320)
og_height2 = random.randint(200, 320)
og_height3 = random.randint(200, 320)
og_height4 = random.randint(200, 320)
og_height5 = random.randint(200, 320)
og_height6 = random.randint(200, 320)	
# trong luc
gravity = 0.2
# toc do roi cua ngo khong
nk_drop_velocity  = 0
# toc do di chuyen cua ong go
og_velocity = 5
# dung chuong trinh khi va cham
pausing = False
# Load am thanh nen
sound = mixer.Sound("musicbackground.wav")
# bien chay xuyen suot chuong trinh
running = True
while running:
	clock.tick(60)
	mixer.Sound.play(sound)
	screen.fill(White)

	check_1 = False
	check_2 = False
	check_3 = False
	check_4 = False
	check_5 = False
	check_6 = False
	
	if(level == 0):
		# tao backgground vao game
		background_rect = screen.blit(background, (0, 0))
		play_ima_rect = screen.blit(play_ima, (x_pl, y_pl))
	else:
	# Level 	
		if level == 1:
			d_2o = 370
			# vẽ background 
			background1_rect = screen.blit(background1, (0,0))
			ngokhong_rect = screen.blit(ngokhong, (x_nk, y_nk))
			y_nk += nk_drop_velocity 
			nk_drop_velocity += gravity

			# chuyển đổi kích thước của gỗ trên 
			ongtren_1 = pygame.transform.scale(ongtren, (og_width, og_height1))
			ongtren_2 = pygame.transform.scale(ongtren, (og_width, og_height2))
			ongtren_3 = pygame.transform.scale(ongtren, (og_width, og_height3))
			ongtren_4 = pygame.transform.scale(ongtren , (og_width, og_height4))
			ongtren_5 = pygame.transform.scale(ongtren, (og_width, og_height5))
			ongtren_6 = pygame.transform.scale(ongtren, (og_width, og_height6))
			# chuyen doi kich thuoc cua go duoi
			ongduoi_1 = pygame.transform.scale(ongduoi, (og_width,720 - d_2o - og_height1))
			ongduoi_2 = pygame.transform.scale(ongduoi, (og_width,720 - d_2o - og_height2))
			ongduoi_3 = pygame.transform.scale(ongduoi, (og_width,720 - d_2o - og_height3))
			ongduoi_4 = pygame.transform.scale(ongduoi , (og_width,720 - d_2o - og_height4))
			ongduoi_5 = pygame.transform.scale(ongduoi, (og_width,720 - d_2o - og_height5))
			ongduoi_6 = pygame.transform.scale(ongduoi, (og_width,720 - d_2o - og_height6))
			# ve ong tren
			ongtren_1_rect = screen.blit(ongtren_1, (x_og1,0))
			ongtren_2_rect = screen.blit(ongtren_2, (x_og2,0))
			ongtren_3_rect = screen.blit(ongtren_3, (x_og3,0))
			ongtren_4_rect = screen.blit(ongtren_4, (x_og4,0))
			ongtren_5_rect = screen.blit(ongtren_5, (x_og5,0))
			ongtren_6_rect = screen.blit(ongtren_6, (x_og6,0))
			# ve ong duoi
			ongduoi_1_rect = screen.blit(ongduoi_1, (x_og1,og_height1 + d_2o))
			ongduoi_2_rect = screen.blit(ongduoi_2, (x_og2,og_height2 + d_2o))
			ongduoi_3_rect = screen.blit(ongduoi_3, (x_og3,og_height3 + d_2o))
			ongduoi_4_rect = screen.blit(ongduoi_4, (x_og4,og_height4 + d_2o))
			ongduoi_5_rect = screen.blit(ongduoi_5, (x_og5,og_height5 + d_2o))
			ongduoi_6_rect = screen.blit(ongduoi_6, (x_og6,og_height6 + d_2o))
			# ve score
			score_ = font_score.render("Score: " + str(score), True,(0,0,255) )
			screen.blit(score_, (0,0))
			# ống chạy sang trái
			x_og1-= og_velocity 
			x_og2-= og_velocity
			x_og3-= og_velocity
			x_og4-= og_velocity
			x_og5-= og_velocity
			x_og6-= og_velocity
			# cong diem
			if (x_nk >= x_og1 + og_width and check_1 == False):
				check_1 = True
				score += 1
			if (x_nk >= x_og2 + og_width and check_2 == False):
				check_2 = True
				score += 1
			if (x_nk >= x_og3 + og_width and check_3 == False):
				check_3 = True
				score += 1
			if (x_nk >= x_og4 + og_width and check_4 == False):
				check_4 = True
				score += 1
			if (x_nk >= x_og5 + og_width and check_5 == False):
				check_5 = True
				score += 1
			if (x_nk >= x_og6 + og_width and check_6 == False):
				check_6 = True 
				score += 1
			
			# kiem tra va cham 
			Arr = [ongtren_1_rect,ongtren_2_rect,ongtren_3_rect,ongtren_4_rect,ongtren_5_rect,ongtren_6_rect,
				   ongduoi_1_rect, ongduoi_2_rect,ongduoi_3_rect,ongduoi_4_rect,ongduoi_5_rect,ongduoi_6_rect,]
			for a in Arr:
				if ngokhong_rect.colliderect(a):
					mixer.Sound.stop(sound)
					og_velocity = 0
					nk_drop_velocity = 0
					gameover_text = font_gameover.render("GAME OVER ! SCORE : " + str(score), True, (255, 0, 0))
					font_gameover_ = screen.blit(gameover_text, (250, 300))
					runagain_text = font_runagain.render(" Press Space to Play again!", True, (255, 0, 0))
					font_runagain_ = screen.blit(runagain_text, (400, 400))
					pausing = True
					
			# tao ong moi
			if x_og1 < -og_width:
				x_og1 = 1200 - og_width
				og_height1 = random.randint(200, 320)

			if x_og2 < -og_width:
				x_og2 = 1200 - og_width
				og_height2 = random.randint(200, 320)
			if x_og3 < -og_width:
				x_og3 = 1200 - og_width
				og_height3 = random.randint(200, 320)
			if x_og4 < -og_width:
				x_og4 = 1200 - og_width
				og_height4 = random.randint(200, 320)
			if x_og5 < -og_width:
				x_og5 = 1200 - og_width
				og_height5 = random.randint(200, 320)
			if x_og6 < -og_width:
				x_og6 = 1200 - og_width
				og_height6 = random.randint(200, 320)
		# tang level 2
		if level == 2:
			d_2o = 350
			# vẽ background 
			background2_rect = screen.blit(background2, (0,0))
			ngokhong_rect = screen.blit(ngokhong, (x_nk, y_nk))
			y_nk += nk_drop_velocity 
			nk_drop_velocity += gravity

			# chuyển đổi kích thước của gỗ trên 
			ongtren_1 = pygame.transform.scale(onggo, (og_width, og_height1))
			ongtren_2 = pygame.transform.scale(onggo, (og_width, og_height2))
			ongtren_3 = pygame.transform.scale(onggo, (og_width, og_height3))
			ongtren_4 = pygame.transform.scale(onggo , (og_width, og_height4))
			ongtren_5 = pygame.transform.scale(onggo, (og_width, og_height5))
			ongtren_6 = pygame.transform.scale(onggo, (og_width, og_height6))
			# chuyen doi kich thuoc cua go duoi
			ongduoi_1 = pygame.transform.scale(nuilua, (og_width,720 - d_2o - og_height1))
			ongduoi_2 = pygame.transform.scale(nuilua, (og_width,720 - d_2o - og_height2))
			ongduoi_3 = pygame.transform.scale(nuilua, (og_width,720 - d_2o - og_height3))
			ongduoi_4 = pygame.transform.scale(nuilua , (og_width,720 - d_2o - og_height4))
			ongduoi_5 = pygame.transform.scale(nuilua, (og_width,720 - d_2o - og_height5))
			ongduoi_6 = pygame.transform.scale(nuilua, (og_width,720 - d_2o - og_height6))
			# ve ong tren
			ongtren_1_rect = screen.blit(ongtren_1, (x_og1,0))
			ongtren_2_rect = screen.blit(ongtren_2, (x_og2,0))
			ongtren_3_rect = screen.blit(ongtren_3, (x_og3,0))
			ongtren_4_rect = screen.blit(ongtren_4, (x_og4,0))
			ongtren_5_rect = screen.blit(ongtren_5, (x_og5,0))
			ongtren_6_rect = screen.blit(ongtren_6, (x_og6,0))
			# ve ong duoi
			ongduoi_1_rect = screen.blit(ongduoi_1, (x_og1,og_height1 + d_2o))
			ongduoi_2_rect = screen.blit(ongduoi_2, (x_og2,og_height2 + d_2o))
			ongduoi_3_rect = screen.blit(ongduoi_3, (x_og3,og_height3 + d_2o))
			ongduoi_4_rect = screen.blit(ongduoi_4, (x_og4,og_height4 + d_2o))
			ongduoi_5_rect = screen.blit(ongduoi_5, (x_og5,og_height5 + d_2o))
			ongduoi_6_rect = screen.blit(ongduoi_6, (x_og6,og_height6 + d_2o))
			# ve score
			score_ = font_score.render("Score: " + str(score), True,(0,0,255) )
			screen.blit(score_, (0,0))
			# ống chạy sang trái
			x_og1-= og_velocity 
			x_og2-= og_velocity
			x_og3-= og_velocity
			x_og4-= og_velocity
			x_og5-= og_velocity
			x_og6-= og_velocity
			# cong diem
			if (x_nk >= x_og1 + og_width and check_1 == False):
				check_1 = True
				score += 1
			if (x_nk >= x_og2 + og_width and check_2 == False):
				check_2 = True
				score += 1
			if (x_nk >= x_og3 + og_width and check_3 == False):
				check_3 = True
				score += 1
			if (x_nk >= x_og4 + og_width and check_4 == False):
				check_4 = True
				score += 1
			if (x_nk >= x_og5 + og_width and check_5 == False):
				check_5 = True
				score += 1
			if (x_nk >= x_og6 + og_width and check_6 == False):
				check_6 = True 
				score += 1	
			# kiem tra va cham 
			Arr = [ongtren_1_rect,ongtren_2_rect,ongtren_3_rect,ongtren_4_rect,ongtren_5_rect,ongtren_6_rect,
				   ongduoi_1_rect, ongduoi_2_rect,ongduoi_3_rect,ongduoi_4_rect,ongduoi_5_rect,ongduoi_6_rect,]
			for a in Arr:
				if ngokhong_rect.colliderect(a):
					mixer.Sound.stop(sound)
					og_velocity = 0
					nk_drop_velocity = 0
					gameover_text = font_gameover.render("GAME OVER ! SCORE : " + str(score), True, (255, 0, 0))
					font_gameover_ = screen.blit(gameover_text, (250, 300))
					runagain_text = font_runagain.render(" Press Space to Play again!", True, (255, 0, 0))
					font_runagain_ = screen.blit(runagain_text, (400, 400))
					pausing = True
			# tao ong moi
			if x_og1 < -og_width:
				x_og1 = 1200 - og_width
				og_height1 = random.randint(200, 320)

			if x_og2 < -og_width:
				x_og2 = 1200 - og_width
				og_height2 = random.randint(200, 320)
			if x_og3 < -og_width:
				x_og3 = 1200 - og_width
				og_height3 = random.randint(200, 320)
			if x_og4 < -og_width:
				x_og4 = 1200 - og_width
				og_height4 = random.randint(200, 320)
			if x_og5 < -og_width:
				x_og5 = 1200 - og_width
				og_height5 = random.randint(200, 320)
			if x_og6 < -og_width:
				x_og6 = 1200 - og_width
				og_height6 = random.randint(200, 320)

		# tang level 3
		if level == 3:
			d_2o = 300
			# vẽ background 
			background2_rect = screen.blit(background3, (0,0))
			ngokhong_rect = screen.blit(ngokhong, (x_nk, y_nk))
			y_nk += nk_drop_velocity 
			nk_drop_velocity += gravity

			# chuyển đổi kích thước của gỗ trên 
			ongtren_1 = pygame.transform.scale(kiemtren, (og_width, og_height1))
			ongtren_2 = pygame.transform.scale(kiemtren, (og_width, og_height2))
			ongtren_3 = pygame.transform.scale(kiemtren, (og_width, og_height3))
			ongtren_4 = pygame.transform.scale(kiemtren , (og_width, og_height4))
			ongtren_5 = pygame.transform.scale(kiemtren, (og_width, og_height5))
			ongtren_6 = pygame.transform.scale(kiemtren, (og_width, og_height6))
			# chuyen doi kich thuoc cua go duoi
			ongduoi_1 = pygame.transform.scale(kiemduoi, (og_width+30,720 - d_2o - og_height1))
			ongduoi_2 = pygame.transform.scale(kiemduoi, (og_width+30,720 - d_2o - og_height2))
			ongduoi_3 = pygame.transform.scale(kiemduoi, (og_width+30,720 - d_2o - og_height3))
			ongduoi_4 = pygame.transform.scale(kiemduoi , (og_width+30,720 - d_2o - og_height4))
			ongduoi_5 = pygame.transform.scale(kiemduoi, (og_width+30,720 - d_2o - og_height5))
			ongduoi_6 = pygame.transform.scale(kiemduoi, (og_width+30,720 - d_2o - og_height6))
			# ve ong tren
			ongtren_1_rect = screen.blit(ongtren_1, (x_og1,0))
			ongtren_2_rect = screen.blit(ongtren_2, (x_og2,0))
			ongtren_3_rect = screen.blit(ongtren_3, (x_og3,0))
			ongtren_4_rect = screen.blit(ongtren_4, (x_og4,0))
			ongtren_5_rect = screen.blit(ongtren_5, (x_og5,0))
			ongtren_6_rect = screen.blit(ongtren_6, (x_og6,0))
			# ve ong duoi
			ongduoi_1_rect = screen.blit(ongduoi_1, (x_og1,og_height1 + d_2o))
			ongduoi_2_rect = screen.blit(ongduoi_2, (x_og2,og_height2 + d_2o))
			ongduoi_3_rect = screen.blit(ongduoi_3, (x_og3,og_height3 + d_2o))
			ongduoi_4_rect = screen.blit(ongduoi_4, (x_og4,og_height4 + d_2o))
			ongduoi_5_rect = screen.blit(ongduoi_5, (x_og5,og_height5 + d_2o))
			ongduoi_6_rect = screen.blit(ongduoi_6, (x_og6,og_height6 + d_2o))
			# ve score
			score_ = font_score.render("Score: " + str(score), True,(0,0,255) )
			screen.blit(score_, (0,0))
			# ống chạy sang trái
			x_og1-= og_velocity 
			x_og2-= og_velocity
			x_og3-= og_velocity
			x_og4-= og_velocity
			x_og5-= og_velocity
			x_og6-= og_velocity
			# cong diem
			if (x_nk >= x_og1 + og_width and check_1 == False):
				check_1 = True
				score += 1
			if (x_nk >= x_og2 + og_width and check_2 == False):
				check_2 = True
				score += 1
			if (x_nk >= x_og3 + og_width and check_3 == False):
				check_3 = True
				score += 1
			if (x_nk >= x_og4 + og_width and check_4 == False):
				check_4 = True
				score += 1
			if (x_nk >= x_og5 + og_width and check_5 == False):
				check_5 = True
				score += 1
			if (x_nk >= x_og6 + og_width and check_6 == False):
				check_6 = True 
				score += 1	
			# kiem tra va cham 
			Arr = [ongtren_1_rect,ongtren_2_rect,ongtren_3_rect,ongtren_4_rect,ongtren_5_rect,ongtren_6_rect,
				   ongduoi_1_rect, ongduoi_2_rect,ongduoi_3_rect,ongduoi_4_rect,ongduoi_5_rect,ongduoi_6_rect,]
			for a in Arr:
				if ngokhong_rect.colliderect(a):
					mixer.Sound.stop(sound)
					og_velocity = 0
					nk_drop_velocity = 0
					gameover_text = font_gameover.render("GAME OVER ! SCORE : " + str(score), True, (255, 0, 0))
					font_gameover_ = screen.blit(gameover_text, (250, 300))
					runagain_text = font_runagain.render(" Press Space to Play again!", True, (255, 0, 0))
					font_runagain_ = screen.blit(runagain_text, (400, 400))
					pausing = True
			# tao ong moi
			if x_og1 < -og_width:
				x_og1 = 1200 - og_width
				og_height1 = random.randint(200, 320)

			if x_og2 < -og_width:
				x_og2 = 1200 - og_width
				og_height2 = random.randint(200, 320)
			if x_og3 < -og_width:
				x_og3 = 1200 - og_width
				og_height3 = random.randint(200, 320)
			if x_og4 < -og_width:
				x_og4 = 1200 - og_width
				og_height4 = random.randint(200, 320)
			if x_og5 < -og_width:
				x_og5 = 1200 - og_width
				og_height5 = random.randint(200, 320)
			if x_og6 < -og_width:
				x_og6 = 1200 - og_width
				og_height6 = random.randint(200, 320)
		if level == 4:
			end_rect = screen.blit(end, (0,0))
			end_text = font_end.render(" COMPLETED GAME!", True, (255, 0, 0))
			ennd_text = screen.blit(end_text, (0, 100))
			score_text = font_gameover.render(" SCORE : " + str(score), True, (255, 0, 0))
			score_text = screen.blit(score_text, (0, 200))
			mixer.Sound.stop(sound)
			og_velocity = 0
			nk_drop_velocity = 0

	if score > highest_score:
		highest_score = score
	# tăng độ khó game
	if score > 0 and score % 30 ==0   :
		og_velocity +=0.02
	# tang level 2
	if score == 100:
		level = 2
	if score == 200:
		level = 3
	if score == 350:
		level = 4
	# font highest score
	if level != 0 and level != 4:
		hg_score = font_highest_score.render("Highest Score: " + str(highest_score), True, (255,0,0))
		hg_score = screen.blit(hg_score, (950, 0))
	# cai dat am thanh
	sound.set_volume(volume)
	# sau khi va cham nhat space khoi tao lai level 1
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				nk_drop_velocity  = 0
				nk_drop_velocity  -= 5
				nhay = mixer.music.load("nhay.wav");
				mixer.music.set_volume(volume)
				mixer.music.play()
				if pausing:
					mixer.Sound.play(sound)
					pausing = False					
					x_og1 = 200
					x_og2 = 400
					x_og3 = 600
					x_og4 = 800
					x_og5 = 1000
					x_og6 = 1200
					nk_drop_velocity = 0
					score = 0 
					og_velocity = 5
					y_nk = 435
					level = 1
			if event.key == pygame.K_p:
				if volume == 1:
					continue
				else :
					volume += 0.1
			if event.key == pygame.K_s:
				if volume == 0:
					continue
				else:
					volume -= 0.1
		# Kich Play de chay
		if event.type == pygame.MOUSEBUTTONDOWN:
			if x_pl < mouse[0] < x_pl + 300 and y_pl < mouse[1] < y_pl+175:
				level = 1
		if event.type == pygame.QUIT:
			running = False
	mouse = pygame.mouse.get_pos() 
	pygame.display.update()
pygame.quit()

