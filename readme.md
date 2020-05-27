# Autocomplete Audit

This code lets you store autocomplete suggestions from different services, using Selenium and Tor.

The file concepts.py contains the phrases to be tested.

The results are stored in a sqlite database.

## Usage

Install tor:

    sudo apt install tor

Start tor:

	tor --HTTPTunnelPort 8118

Run script:

	python3 scrape.py

To test for different countries, add this line at the end of ´/etc/tor/torrc´
	
	ExitNodes {fr}

replacing 'fr' with the country you want your TOR connection to exit in.