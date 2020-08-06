import PySimpleGUI as sg

from ui.AbstractUI import UI

"""
Summary: This class is the main body layout of the GUI
"""


class Login_UI(UI):

    # initiate the layout
    def __init__(self):
        login_ioc_base64 = b"iVBORw0KGgoAAAANSUhEUgAAAPgAAAAdCAIAAAAIOjZtAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAARqSURBVHhe7dxtbFNVGADgu952pevadWvLWruu+146oW4CQxxjMxAUvxLmQsAAcZrIYgT/mKg/hjHGKImRH/qDIQnG7YcaEgKJMgxqNiTiIJFtSvkYbGUdpV9ZP9Yvbkt9u3PSNGzpXC0/dvs+uTk55z3v7v689+25WbO8eDzOMMwN69h3g0cmbNe9fg8sEVruFPKSaq2xs/WNer0JlolC/2Gw98TQ8cLiFQVKkUjMkjyEljUuEvM5g2FvdGd7d0drV961OyM937ypqpCKpSKaghBfRAKcc3L2k65jrHqNwPfAIVNJ6A5CPCLMZ7n7nN1pZys2yGWafFYooDsI8YtILLTfdQjg7RPP5YjHoLyhyLGRo5yAhY5yAhY6yglY6Cgn5G0/uMbwhIquUFrPGnc/Z9ztCTk/OrOHhlLsbf6gUtmgkKhhzsXuuwO2oVun/pj4iewSnY1vP65dn5pzeuyY2X4Jlg/dfP+mz6tUq2AyYO4/a+6HCUHiDwVRepYRF3b07HhvS29TWZtYKLnt+huue36LUqrd0XQAKptmzD0JLVUvJnOgyjVyQ9dTPepCHc1YSEvVC3SG/gcs9CyACoaShWZ8+Ld3vhx6F64vft1/cvQIbDUbtpI6NpaugycBungy59C5fdDLw9FAW832udsswBWwycTF0MXpGmUKCz0L4MQC48XJs87ZaRIBcGi557OI2PxtDXth2VrzMozQ6VNzjl7oOfjjrhNXvqLreS7f+cUfmdEX18FzQkMoI1joWUDO3PMPzTbfJIxFK5QwqgvLYPzH9mdi4z+rUzeeudoHT8uOJw/QEMoIFvojZPdP0RnDCAVCOpvz4ba+wx0D5II5jS4EPhmmPDfhWUo97qOlwkJ/hEplejpjmDAXhFEmVpDlhPtq4p3VZyHL9PqGP4PDffK4jzKAhZ4F8MoI4/yOq5VXwOgNu2GcCTlgLC+pT2wwzLfDn8L76JXp82SZHhzrhy0/wwFmT/P7NISWCAs9C6ZmbsBo0rWkdtwNlc9r5IYQNws1Dcvz46ehK2tkBoiTBJBs8IuCF1ZPyKlX1JZIS2kILQVrbHtMoSmgK5RWjdoEV5yJN2ia1xu2kgt67cj07426VqVUs7Z8M9naWP3SuvItD+KxU2NfWz034WddgbvaogqdorpuZdNq3dNr9ZufqX2lVt3ICliz/TLcgdw8HA0Ojp+EfLhJccHKmaAD7j/3yxmH32rSbZTmy2E+7hq95RolcbQorz2IHX3JJKLCKtWq5EWCh87t+8s6GImGSBA6tztgO37x49S/jEJrHzD3w0kGGjPkFEmUkHP0Qg9p+Ysy2y+Rjw6UAfwKAOI//AoAyhVY6CgnCBTyEi4SoyuEeAfKu0imENSVrfY5AzSGEO/4nMHy0hpBR8trIW8sEuBoGCEegcIOe6Ovtr+V6Oi72rtdk7Nuqx/PMIg3oJjdVh8Uduem1+v1Jvq/F69PjX4/1Hvbds3n95I8hJY1OJdXaut3tnVDK2cY5l8LN8I2Wxi2PgAAAABJRU5ErkJggg=="
        cross_ioc_base64 = b"R0lGODlhEAAQAHAAACwAAAAAEAAQAIT/////bW3/trb/Skr/AAD/AgL/mpr/cXH/BQX/oaH/u7v/AQH/qqr/Cgr/lZX/p6f/BAT/tbX/nJz/sLD/AwMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFUSAABIpomkpgDgRhnKLRDsDRtq8p34dytwwR40coDX+G3S0oJBKZKGerBAMob7nqFVcFHJ3QmHRp+uK2L9+Pqr6lfmGzikUINwk0Ua8LUBxEIQA7"

        title = [
            [sg.Text("WELCOME", font=("Helvetica", 15), size=(10, 1), background_color="light gray",
                     text_color="red", justification="center")]
        ]

        column1 = [
            [sg.Text("Username:", font=("arial", 10), background_color="light gray", text_color="black"),
             sg.InputText(key="_USERNAME_", size=(25, 1), enable_events=True)]
        ]

        column2 = [
            [sg.Text("Password: ", font=("arial", 10), background_color="light gray", text_color="black"),
             sg.InputText(key="_PASSWORD_", password_char="*", size=(25, 1), enable_events=True)]
        ]

        buttons = [
            [sg.Button(image_data=login_ioc_base64, border_width=0, size=(20, 1), button_color=("black", "light gray"),
                       key="_LOGIN_")]
        ]

        column_cross = [
            [sg.Button(image_data=cross_ioc_base64, border_width=0, size=(20, 1), button_color=("black", "light gray"),
                       key="_LG_CROSS_")]
        ]

        column_all = [
            [sg.Column(title, background_color="light gray", key="_TITLE_COLUMN_", justification="center")],
            [sg.Column(column1, background_color="light gray", key="_NAME_COLUMN_", pad=(10, 10),
                       justification="center")],
            [sg.Column(column2, background_color="light gray", key="_DATE_COLUMN_", pad=(10, 10),
                       justification="center")],
            [sg.Column(buttons, pad=(10, 20), background_color="light gray", justification="center")],
        ]

        self._layout = [
            [sg.Column(column_cross, background_color="light gray", justification="right")],
            [sg.Column(column_all, pad=(20, 10), background_color="light gray", justification="center")]
        ]
