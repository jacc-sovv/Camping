import requests
import json
from datetime import datetime

# Rec.gov api key - bb76ad61-c8ba-42b1-935f-d1e574aec492
# orgid of NPS is 128

weekends = True
allow_group_sites = False


campgrounds = {232462 : "Rocky Mountain National Park Glacier Basin Campground",
               233187 : "Rocky Mountain National Park Aspenglen Campground",
               232463 : "Rocky Mountain National Park Moraine Park Campground",
               }
id = [232462]
ids = [232462, 233187, 232463]



headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

for month in [6,7,8]:
    full_camp_data = []
    for camp_id in ids:
        url = "https://www.recreation.gov/api/camps/availability/campground/" + str(camp_id) + "/month?start_date=2023-0" + str(month) + "-01T00%3A00%3A00.000Z"
        response = requests.get(url, headers=headers)
        camp_data = json.loads(response.text)
        full_camp_data.append(camp_data)

    avaiable_sites = {}
    id_counter = 0
    for campground in full_camp_data:
        local_id = ids[id_counter]
        id_counter += 1
        avaiable_sites[campgrounds[local_id]] = []
        for campsite in campground["campsites"]:
            name = campground["campsites"][campsite]["site"]
            availability = campground["campsites"][campsite]["availabilities"]
            free_days = []
            for date in availability:
                if "Available" in availability[date]:
                    free_days.append(date)
            sites_days_array = []
            if(free_days):
                for day in free_days:
                    dict_answer = [name, day]
                    sites_days_array.append(dict_answer)
            if(sites_days_array):
                avaiable_sites[campgrounds[local_id]].append(sites_days_array)



availability_as_string = ""
for campground in avaiable_sites:

    availability_as_string += campground + " Availability (" + "https://www.recreation.gov/camping/campgrounds/" + "):\n"
    for sites_array in avaiable_sites[campground]:
        for date in sites_array:
            if(date[0][0] == "G" and allow_group_sites == False):  #Group site, needs like 25 ppl
                continue
            pretty_date = date[1]
            pretty_date = pretty_date[:-10]
            if(weekends):
                date_time_obj = datetime.strptime(pretty_date, '%Y-%m-%d')
                day_no = date_time_obj.weekday()
                if(day_no > 3):     #Fridays, Saturdays, Sundays
                    single_availability = "Campsite " + date[0] + " is available on " + pretty_date + '\n'
                    availability_as_string += single_availability
            else:
                single_availability = "Campsite " + date[0] + " is available on " + pretty_date + '\n'
                availability_as_string += single_availability
    availability_as_string += "\n"

print(availability_as_string)

SERVER = "smtp.gmail.com"
FROM = "jsguitarrocks3@gmail.com"
TO = ["jsguitarrocks@gmail.com"] # must be a list

import smtplib, ssl
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content(availability_as_string)
msg["Subject"] = "An Email Alert"
msg["From"] = FROM
msg["To"] = TO

context=ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
    smtp.starttls(context=context)
    smtp.login(msg["From"], "inrdumfthceztgnd")
    smtp.send_message(msg)



