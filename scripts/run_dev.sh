CONFIG=DATA/confs/dev.cfg

INIT=0
if (($INIT == 1 )); then
	echo "INITING BACKEND"
	python sleek@slack.py -cfg $CONFIG -init -surveys DATA/surveys/
fi
python sleek@slack.py -cfg $CONFIG -connect -dbg