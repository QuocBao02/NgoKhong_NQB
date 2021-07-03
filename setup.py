import cx_Freeze
executables = [cx_Freeze.Executable("NgoKhong.py")]
cx_Freeze.setup(
name="đặt_tên_gì_cũng_được",
options={"build_exe": {"packages": ["pygame"],
"include_files": [("background0.png"),("Play.png"), ("ngokhong.png"), ("background1.png"), ("background2.png") , ("background3.png"), ("end.png"), ("ongduoi.png"),
 ("ongtren.png"), ("onggo.png"), ("nuilua.png"), ("kiemtren.png"), ("kiemduoi.png"), ("musicbackground.wav"), ("nhay.wav"), ("tutorial.png")]}},
executables = executables
)