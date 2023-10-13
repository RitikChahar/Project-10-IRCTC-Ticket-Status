# Project-10-IRCTC-Ticket-Status
This repository contains a Django project which will help to update you about your railway ticket status in real time.
### Base URL
```http://127.0.0.1:8000/```
### Endpoints

#### 1. ```/ticket-status/?pnr_number=2631313275/```
  #### Method: GET
  #### Response
  ```json
  {
      "success": true,
      "message": "All good, here if your data!",
      "data": {
          "PNR": "2631313275",
          "TrainNo": "15012",
          "TrainName": "CDG LJN EXPRESS",
          "DateOfJourney": "22-10-2023",
          "BookingDate": "05-10-2023",
          "Quota": "GN",
          "From": "Chandigarh",
          "To": "Lucknow Junction",
          "Class": "2A",
          "ChartPrepared": false,
          "PassengerCount": 1,
          "TicketFare": "1515",
          "Prediction": null,
          "PredictionPercentage": "100",
          "Coach": "A2",
          "Berth": 19,
          "BookingStatus": "CNF A2 19",
          "CurrentStatus": "CNF",
          "CoachPosition": "L SLR GS GS GS GS S1 S2 S3 B3 B1 B2 A1 GS GS GS GS MZM"
      }
  }
  ```

#### 2. ```/send-status/```
  #### Method: POST
  #### Request
  ```json
  {
      "PNR": "2631313275",
      "TrainNo": "15012",
      "TrainName": "CDG LJN EXPRESS",
      "DateOfJourney": "22-10-2023",
      "BookingDate": "05-10-2023",
      "Quota": "GN",
      "From": "Chandigarh",
      "To": "Lucknow Junction",
      "Class": "2A",
      "ChartPrepared": false,
      "PassengerCount": 1,
      "TicketFare": "1515",
      "Prediction": null,
      "PredictionPercentage": "100",
      "Coach": "A2",
      "Berth": 19,
      "BookingStatus": "CNF A2 19",
      "CurrentStatus": "CNF",
      "CoachPosition": "L SLR GS GS GS GS S1 S2 S3 B3 B1 B2 A1 GS GS GS GS MZM",
      "nameOfPassenger":"Ritik Chahar",
      "passengerEmail": "ritikchahar54@gmail.com"
  }
  ```
  #### Response
  ```json
  {
      "success": true,
      "message": "All good, your mail is sent!"
  }
  ```