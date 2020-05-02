

function subiect_4(){

	if [[ $# -eq 0 || $# -gt 9 ]]; then
		echo "numar de parametri invalid"
		exit 2
	fi

	if [[ -d $1 ]]; then
		echo "exista un director cu acelasi nume"
		exit 0
	elif [[ -f $1 ]]; then
		echo "exista un fisier cu acelasi nume"
		exit 1
	fi

	mkdir $1
	cd $1
	pwd

	echo "$@"

	for arg in "$@"; do 
		if [[ $arg == $1 ]]; then
			continue
		fi

		touch $arg
	done


	echo "script terminat cu succes"
}





subiect_4 $@
