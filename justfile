install:
	python3 install.py --name MakeDoc

close-set:
	pkill -x Ableton Live 12 Suite

open-set:
	open ./set/set.als

reload:
	just install && just close-set && sleep 1 && just open-set