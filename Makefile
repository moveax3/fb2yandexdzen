serverrun:
	DISPLAY=:99 xvfb-run -a -n 1 -l -s "-screen 0, 1024x768x8" python3 manage.py parse yes

localrun:
	python3 manage.py parse yes
