from twilio.rest import Client


def make_call():
    # Get these credentials from http://twilio.com/user/account
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    # Make the call
    name_to_number = {'edu': '+44'}
    try:
        call = client.api.account.calls\
            .create(to=name_to_number['edu'],  # Any phone number
                    from_="+44",  # Must be a valid Twilio number
                    url='http://pablopg.dte.us.es:5000')
    except:
        pass
