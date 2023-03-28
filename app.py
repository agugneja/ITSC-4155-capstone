# Start web scraper
print("Initializing web scraper")
from WebScraper.main import main as scrape
print("Web scraper started successfully")

# Start the web interface
import Interface.app as frontEnd
frontEnd.getFunctions(scrape)
frontEnd.app.run()
