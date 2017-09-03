CONFIG=DATA/confs/beta.cfg
API_TOKEN_ID="SLEEK_BETA_TOKEN"
INIT=0
if (($INIT == 1 )); then
	echo "INITING BACKEND"
	python main.py -cfg $CONFIG -init -surveys DATA/surveys/
else
	python main.py -cfg $CONFIG -api_token_id $API_TOKEN_ID -connect -dbg 
fi
