install:
	python3 install.py --name MakeDoc

install-builder:
	python3 install.py --name MakeDoc_Build --mode build

close-set:
	pkill -x Ableton Live 12 Suite

open-set:
	open ./set/set.als

reload:
	just install && just close-set && sleep 1 && just open-set

watch:
	python3 watch.py --version 'Live 12.1.5'