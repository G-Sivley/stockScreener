from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import webbrowser


def main():
   # A script that uses my stock screener to open the user requested number of tickers
   url = "https://finviz.com/screener.ashx?v=111&f=an_recom_buybetter,sh_avgvol_o200,sh_price_o1,ta_beta_o1,ta_rsi_os40,targetprice_a50&ft=4&o=price"
   r = render_page(url)
   soup = BeautifulSoup(r, "html.parser")

   # Prints all the lines with the ticker in it
   lines = soup.findAll(class_="screener-link-primary")
   
   # Creates a list of tickers from the lines 
   tickers = []
   for line in lines:
      tickers.append(line.getText())
   num_of_results = num_to_open()
   open_tickers(tickers, num_of_results)
   
      
def render_page(url):
   # Gets the HTML after allowing the page to render
   driver = webdriver.Chrome()
   driver.get(url)
   time.sleep(3)
   r = driver.page_source
   driver.quit()
   return r


def num_to_open():
   # Returns the user requested number of tickers
   num = int(input("How many results do you want: "))
   return num 


def open_tickers(tickers, num_to_open):
   # Check to make sure that the number to open is not longer than tickers 
   if num_to_open > len(tickers):
      num_to_open = len(tickers)
      print("Less tickers than number requested")

   # Opens webbrowser of each ticker in the number of tickers
   for ticker in tickers[0:num_to_open]:
      webbrowser.open(f"https://finviz.com/quote.ashx?t={ticker}")


main()