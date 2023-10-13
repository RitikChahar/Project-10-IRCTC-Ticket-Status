import requests
import re
import json
from bs4 import BeautifulSoup

def checkTicketStatus(pnr_number):
    url = f'https://www.confirmtkt.com/pnr-status/{pnr_number}?'
    header = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        }
    response = requests.get(url,headers=header)
    soup = BeautifulSoup(response.content, 'html.parser').find_all('script', type='text/javascript')
    script = ''
    for i in soup:
        if 'var data' in i.text:
            script = i.text
    passenger_data =  json.loads(str(re.findall(r'(?<=data =).*?(?=};)', script)[0])+'}')
    
    output ={
        'PNR':passenger_data['Pnr'],
        'TrainNo':passenger_data['TrainNo'],
        'TrainName':passenger_data['TrainName'],
        'DateOfJourney':passenger_data['Doj'],
        'BookingDate':passenger_data['BookingDate'],
        'Quota':passenger_data['Quota'],
        'From':passenger_data['BoardingStationName'],
        'To':passenger_data['ReservationUptoName'],
        'Class':passenger_data['Class'],
        'ChartPrepared':passenger_data['ChartPrepared'],
        'PassengerCount':passenger_data['PassengerCount'],
        'TicketFare':passenger_data['TicketFare'],
        'Prediction':passenger_data['PassengerStatus'][0]['Prediction'],
        'PredictionPercentage':passenger_data['PassengerStatus'][0]['PredictionPercentage'],
        'Coach':passenger_data['PassengerStatus'][0]['Coach'],
        'Berth':passenger_data['PassengerStatus'][0]['Berth'],
        'BookingStatus':passenger_data['PassengerStatus'][0]['BookingStatus'],
        'CurrentStatus':passenger_data['PassengerStatus'][0]['CurrentStatus'],
        'CoachPosition':passenger_data['CoachPosition'],
    }

    return output