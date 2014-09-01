kill $(ps aux | grep '[p]ython' | awk '{print $2}')
kill $(ps aux | grep '[m]ongod' | awk '{print $2}')