'''
Соберите информацию о судебных заседаниях в деле № А40-183194/2015 (дело о
банкротстве ООО «ТрансИнвестХолдинга»).
На сайте https://kad.arbitr.ru/ в каждом деле приложен .ics файл (стандартное
расширение файлов для программ календарей), в котором присутствует информация о
дате и времени судебных заседаний (вы можете открыть его, кликнув по дате
заседания в карточке). Однако в них присутствует и «пустая» информация,
дублирующая информацию о событиях по делу, но не относящуюся к конкретным
судебным заседаниям.
'''

from ics import Calendar
import json

def clean_events(events):
    cleaned_events = []
    unique_descriptions = set()
    for event in events:
        event_info = event.name.split(":")
        if len(event_info) > 1:
            case_number = event_info[1].strip()
        else:
            case_number = "А65-19059/2022"
        if event.description not in unique_descriptions and str(event.begin) != "0001-01-01T00:00:00+00:00":
            cleaned_events.append({
                "case_number": case_number,
                "start": str(event.begin),
                "end": str(event.end),
                "location": event.location,
                "description": event.description
            })
            unique_descriptions.add(event.description)
    return cleaned_events


with open('А65-19059-2022.ics', 'r', encoding='utf-8') as f:
    c = Calendar(f.read())

cleaned_events = clean_events(c.events)

with open('court_dates.json', 'w', encoding='utf-8') as json_file:
    json.dump(cleaned_events, json_file, ensure_ascii=False, indent=4)
