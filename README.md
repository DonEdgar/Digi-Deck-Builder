# Digi-Deck-Builder
As I recently started getting into the Digimon(2020) tcg, I wanted a mininalistic approach to keeping track of decks I am building.

I am building a TUI app that will help in building a deck for digimon tcg.

# Flow 
1. The way this will work is that when the user starts this program, they can search for cards from the database - Python will used to call the API
2. The results will then be stored in a JSON file
3. Rust will be used in the backend to parse the JSON file
4. Once the data is parsed, the results will then be presented on screen

# Goals
1. Build URL to make API call - DONE
2. Load results from API into JSON file - 50% (Results are currently stored in a JSON string)
3. Map out functions needed for parsing data in RUST

# Future
If this works out will like I plan, then I would like to extend this to other TCGs like Pokemon or Magic